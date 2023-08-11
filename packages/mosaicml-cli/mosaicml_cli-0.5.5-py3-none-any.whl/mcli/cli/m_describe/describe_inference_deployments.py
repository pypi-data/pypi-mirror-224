"""Implementation of mcli describe deployment"""
import logging
from typing import Dict, Generator, List, Optional

from rich.table import Table

from mcli.api.exceptions import MAPIException
from mcli.api.inference_deployments.api_get_inference_deployments import get_inference_deployment
from mcli.api.model.inference_deployment import InferenceDeployment
from mcli.cli.m_get.display import MCLIDisplayItem, MCLIGetDisplay, OutputDisplay, create_vertical_display_table
from mcli.utils.utils_logging import FAIL, FormatString, format_string

logger = logging.getLogger(__name__)


# Displays
class MCLIDescribeDeploymentMetadataDisplay(MCLIGetDisplay):
    """ Vertical table view of inference deployment metadata """

    def __init__(self, models: List[InferenceDeployment]):
        self.models = sorted(models, key=lambda x: x.created_at, reverse=True)

    @property
    def index_label(self) -> str:
        return ""

    def create_custom_table(self, data: List[Dict[str, str]]) -> Optional[Table]:
        return create_vertical_display_table(data=data[0])

    def __iter__(self) -> Generator[MCLIDisplayItem, None, None]:
        for model in self.models:
            config = model.config
            item = MCLIDisplayItem({
                'Inference Deployment Name': model.name,
                'Address': model.public_dns,
                'Image': config.image,
                'Cluster': config.cluster,
                'GPU Num': config.gpu_num,
                'GPU Type': config.gpu_type,
                'Replicas': config.replicas,
                'Metadata': config.metadata,
            })
            yield item


def describe_deploy(deployment_name: str, output: OutputDisplay = OutputDisplay.TABLE, **kwargs):
    """
    Fetches more details of a Inference Deployment
    """
    del kwargs

    try:
        deployment = get_inference_deployment(deployment_name)
    except MAPIException as e:
        logger.error(f'{FAIL} {e}')
        return 1

    # Deployment metadata section
    print(format_string('Inference Deployment Metadata', FormatString.BOLD))
    metadata_display = MCLIDescribeDeploymentMetadataDisplay([deployment])
    metadata_display.print(output)
    print()

    # Deployment original input section
    print(format_string('Submitted YAML', FormatString.BOLD))
    print(deployment.submitted_config)
