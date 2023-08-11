"""CLI getter for deployments"""
from __future__ import annotations

import argparse
from typing import Generator, List, Optional

from mcli import config
from mcli.api.exceptions import cli_error_handler
from mcli.api.model.inference_deployment import InferenceDeployment, InferenceDeploymentReplica
from mcli.cli.common.deployment_filters import get_deployments_with_filters
from mcli.cli.common.run_filters import configure_submission_filter_argparser
from mcli.cli.m_get.display import MCLIDisplayItem, MCLIGetDisplay, OutputDisplay, format_timestamp
from mcli.utils.utils_model import SubmissionType


class InferenceDeploymentDisplay(MCLIGetDisplay):
    """`mcli get deployments` display class
    """

    def __init__(self, deployments: List[InferenceDeployment], include_ids: bool = False):
        self.deployments = sorted(deployments, key=lambda x: x.created_at, reverse=True)
        self.include_ids = include_ids

    def __iter__(self) -> Generator[MCLIDisplayItem, None, None]:
        for deployment in self.deployments:
            dep_config = deployment.config
            yield MCLIDisplayItem({
                'name': deployment.name,
                'id': deployment.config.deployment_id if self.include_ids else None,
                'replicas': dep_config.replicas,
                'status': f'{deployment.get_ready_replicas()}/{dep_config.replicas} Ready',
                'user': deployment.created_by,
                'cluster': dep_config.cluster,
                'gpu type': dep_config.gpu_type,
                'gpu num': dep_config.gpu_num,
                'created time': format_timestamp(deployment.created_at),
            })


class InferenceDeploymentReplicaDisplay(MCLIGetDisplay):
    """Display information about a deployment replica
    """

    @property
    def index_label(self) -> str:
        return "deployment_name"

    def __init__(self, deployments: List[InferenceDeployment]) -> None:
        self.deployments = sorted(deployments, key=lambda x: x.created_at, reverse=True)

    def format_restarts(self, replica: InferenceDeploymentReplica) -> str:
        if replica.latest_restart_count > 0:
            return (f'{replica.latest_restart_count} restarts, '
                    f'Last restart at {format_timestamp(replica.latest_restart_time)}')
        else:
            return f'0 restarts, Started at {format_timestamp(replica.latest_restart_time)}'

    def __iter__(self) -> Generator[MCLIDisplayItem, None, None]:
        for deploy in self.deployments:
            for i, replica in enumerate(deploy.replicas):
                deploy_name = deploy.name
                if i > 0:
                    deploy_name = ''
                yield MCLIDisplayItem({
                    'deployment_name': deploy_name,
                    'replica': replica.name[-5:],
                    'status': replica.status,
                    'restarts': self.format_restarts(replica),
                })


@cli_error_handler('mcli get deployments')
def cli_get_deployments(
    name_filter: Optional[List[str]] = None,
    cluster_filter: Optional[List[str]] = None,
    before_filter: Optional[str] = None,
    after_filter: Optional[str] = None,
    gpu_type_filter: Optional[List[str]] = None,
    gpu_num_filter: Optional[List[int]] = None,
    status_filter: Optional[List[str]] = None,
    output: OutputDisplay = OutputDisplay.TABLE,
    include_ids: bool = False,
    compact: bool = False,
    **kwargs,
) -> int:
    """Get a table of ongoing and completed inference deployments
    """
    del kwargs

    deployments = get_deployments_with_filters(name_filter, cluster_filter, before_filter, after_filter,
                                               gpu_type_filter, gpu_num_filter, status_filter)

    if not compact and len(deployments) > 0:
        print('Inference Deployments Overview')
    display = InferenceDeploymentDisplay(deployments, include_ids=include_ids)
    display.print(output)

    deployments_with_replicas = [deploy for deploy in deployments if deploy.replicas]
    if not compact and len(deployments_with_replicas) > 0:
        print('\nReplica Details')
        replicas_display = InferenceDeploymentReplicaDisplay(deployments_with_replicas)
        replicas_display.print(OutputDisplay.TABLE)

    return 0


def get_deployments_argparser(subparsers: argparse._SubParsersAction):
    """Configures the ``mcli get deployments`` argparser
    """

    deployment_examples: str = """Examples:
    $ mcli get deployments
    NAME                          CLUSTER     GPU_TYPE    GPU_NUM          CREATED_TIME     STATUS
    deploy-foo                      c-1        g0-type       8            05/06/22 1:58pm    Ready
    deploy-bar                      c-2        g0-type       1            05/06/22 1:57pm   Pending
    """
    deployments_parser = subparsers.add_parser(
        'deployments',
        aliases=['deployment'],
        help='Get information on all of your existing deployments across all clusters.',
        epilog=deployment_examples,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    deployments_parser.add_argument('--compact',
                                    action='store_true',
                                    dest='compact',
                                    default=False,
                                    help='Hide detailed replica statuses and only show individual deployments')

    deployments_parser.add_argument(
        '--name',
        dest='name_filter',
        nargs='*',
        metavar='DEPLOYMENT',
        default=None,
        help='String or glob of the name(s) of the deployments to get',
    )

    configure_submission_filter_argparser('get',
                                          deployments_parser,
                                          include_all=False,
                                          submission_type=SubmissionType.INFERENCE)
    deployments_parser.set_defaults(func=cli_get_deployments)

    deployments_parser.add_argument('--ids',
                                    action='store_true',
                                    dest='include_ids',
                                    default=config.ADMIN_MODE,
                                    help='Include the deployment ids in the output')
    return deployments_parser
