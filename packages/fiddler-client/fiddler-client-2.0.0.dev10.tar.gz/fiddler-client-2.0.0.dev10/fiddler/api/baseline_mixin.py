from http import HTTPStatus
from typing import List

from pydantic import parse_obj_as

from fiddler.core_objects import BaselineType, WindowSize
from fiddler.libs.http_client import RequestClient
from fiddler.schema.baseline import Baseline
from fiddler.utils.compatibility_helpers import (
    project_id_compat,
    model_id_compat,
    baseline_id_compat,
)
from fiddler.utils.decorators import handle_api_error_response
from fiddler.utils.logger import get_logger
from fiddler.utils.response_handler import (
    APIResponseHandler,
    PaginatedResponseHandler,
)

logger = get_logger(__name__)


class BaselineMixin:
    client: RequestClient
    organization_name: str

    @handle_api_error_response
    def get_baselines(
        self,
        project_id: str = None,
        model_id: str = None,
        project_name: str = None,
        model_name: str = None,
    ) -> List[Baseline]:
        """Get list of all Baselines at project or model level

        :param project_id: unique identifier for the project
        :type project_id: string
        :param model_id: (optional) unique identifier for the model
        :type model_id: string
        :param project_name: unique identifier for the project
        :type project_name: string
        :param model_name: (optional) unique identifier for the model
        :type model_name: string
        :returns: List containing Baseline objects
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        if model_id is not None and model_name is not None:
            raise ValueError('Pass either model_id or model_name')

        response = self.client.get(
            url='baselines/',
            params={
                'organization_name': self.organization_name,
                'project_name': project_name,
                'model_name': model_name or model_id,
            },
        )
        items = PaginatedResponseHandler(response).get_pagination_items()
        return parse_obj_as(List[Baseline], items)

    @handle_api_error_response
    def get_baseline(
        self,
        project_id: str = None,
        model_id: str = None,
        baseline_id: str = None,
        project_name: str = None,
        model_name: str = None,
        baseline_name: str = None,
    ) -> Baseline:
        """Get the details of a Baseline.

        :param project_id: unique identifier for the project
        :type project_id: string
        :param model_id: unique identifier for the model
        :type model_id: string
        :param baseline_id: unique identifier for the baseline
        :type baseline_id: string
        :param project_name: unique identifier for the project
        :type project_name: string
        :param model_name: unique identifier for the model
        :type model_name: string
        :param baseline_name: unique identifier for the baseline
        :type baseline_name: string

        :returns: Baseline object which contains the details
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )

        baseline_name = baseline_id_compat(
            baseline_id=baseline_id,
            baseline_name=baseline_name,
        )

        response = self.client.get(
            url='baselines/',
            params={
                'organization_name': self.organization_name,
                'project_name': project_name,
                'model_name': model_name,
                'baseline_name': baseline_name,
            },
        )
        items = PaginatedResponseHandler(response).get_pagination_items()

        # If a baseline exists, only a single baseline should be returned
        if len(items) == 1:
            return parse_obj_as(Baseline, items[0])
        else:
            return None

    @handle_api_error_response
    def add_baseline(
        self,
        project_id: str = None,
        model_id: str = None,
        baseline_id: str = None,
        type: BaselineType = None,
        dataset_name: str = None,
        start_time: int = None,
        end_time: int = None,
        offset: WindowSize = None,
        window_size: WindowSize = None,
        wait: bool = False,
        project_name: str = None,
        model_name: str = None,
        baseline_name: str = None,
    ) -> Baseline:
        """Function to add a Baseline to fiddler for monitoring

        :param project_id: unique identifier for the project
        :type project_id: string
        :param model_id: unique identifier for the model
        :type model_id: string
        :param baseline_id: unique identifier for the baseline
        :type baseline_id: string
        :param project_name: unique name for the project
        :type project_name: string
        :param model_name: unique name for the model
        :type model_name: string
        :param baseline_name: unique name for the baseline
        :type baseline_name: string
        :param type: type of the Baseline
        :type type: BaselineType
        :param dataset_name: (optional) dataset to be used as baseline
        :type dataset_name: string
        :param start_time: (optional) seconds since epoch to be used as start time for STATIC_PRODUCTION baseline
        :type start_time: int
        :param end_time: (optional) seconds since epoch to be used as end time for STATIC_PRODUCTION baseline
        :type end_time: int
        :param offset: (optional) offset in seconds relative to current time to be used for ROLLING_PRODUCTION baseline
        :type offset: WindowSize
        :param window_size: (optional) width of window in seconds to be used for ROLLING_PRODUCTION baseline
        :type window_size: WindowSize
        :type run_async: Boolean
        :type wait: Boolean


        :return: Baseline object which contains the Baseline details
        """
        if type is None:
            raise TypeError(f'Please make sure param `type` param is passed')

        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )

        baseline_name = baseline_id_compat(
            baseline_id=baseline_id,
            baseline_name=baseline_name,
        )

        if window_size:
            window_size = int(window_size)  # ensure enum is converted to int

        request_body = Baseline(
            organization_name=self.organization_name,
            project_name=project_name,
            name=baseline_name,
            type=str(type),
            model_name=model_name,
            dataset_name=dataset_name,
            start_time=start_time,
            end_time=end_time,
            offset=offset,
            window_size=window_size,
            run_async=True,
        ).dict()

        if 'id' in request_body:
            request_body.pop('id')

        response = self.client.post(
            url='baselines/',
            data=request_body,
        )

        if response.status_code == HTTPStatus.OK:
            logger.info(f'{baseline_name} setup successful')
            return Baseline.deserialize(APIResponseHandler(response))
        if response.status_code == HTTPStatus.ACCEPTED:
            data = APIResponseHandler(response).get_data()
            job_uuid = data['job_uuid']
            logger.info(
                'Model[%s/%s] - Submitted job (%s) for adding default baseline',
                project_name,
                model_name,
                job_uuid,
            )
            if wait:
                job_name = (
                    f'Model[{project_name}/{model_name}] - create Default Baseline'
                )
                self.wait_for_job(uuid=job_uuid, job_name=job_name)  # noqa
            return job_uuid

    @handle_api_error_response
    def delete_baseline(
        self,
        project_id: str = None,
        model_id: str = None,
        baseline_id: str = None,
        project_name: str = None,
        model_name: str = None,
        baseline_name: str = None,
    ) -> None:
        """Delete a Baseline

        :param project_id: unique identifier for the project
        :type project_id: string
        :param model_id: unique identifier for the model
        :type model_id: string
        :param baseline_id: unique identifier for the baseline
        :type baseline_id: string
        :param project_name: unique identifier for the project
        :type project_name: string
        :param model_name: unique identifier for the model
        :type model_name: string
        :param baseline_name: unique identifier for the baseline
        :type baseline_name: string

        :returns: None
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )

        model_name = model_id_compat(
            model_id=model_id,
            model_name=model_name,
        )

        baseline_name = baseline_id_compat(
            baseline_id=baseline_id,
            baseline_name=baseline_name,
        )

        response = self.client.delete(
            url='baselines/',
            params={
                'organization_name': self.organization_name,
                'project_name': project_name,
                'model_name': model_name,
                'baseline_name': baseline_name,
            },
        )

        if response.status_code == HTTPStatus.OK:
            logger.info(f'{baseline_name} delete request received.')
        else:
            # @TODO: Handle non 200 status response
            logger.info('Delete unsuccessful')
