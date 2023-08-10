from typing import List

from deprecated import deprecated

from fiddler.libs.http_client import RequestClient
from fiddler.schema.project import Project


class CompatibilityMixin:
    client: RequestClient
    organization_name: str

    @deprecated(
        reason=f'list_datasets is deprecated and will be removed in future versions. '
               f'Use get_dataset_names instead.'
    )
    def list_datasets(self, project_id) -> List[str]:
        return self.get_dataset_names(project_name=project_id)  # noqa

    @deprecated(reason=f'create_project is deprecated and will be removed in future '
                       f'versions. Use add_project instead.')
    def create_project(self, project_id: str) -> Project:
        return self.add_project(project_name=project_id)  # noqa

    @deprecated(
        reason=f'list_projects is deprecated and will be removed in future versions. '
               f'Use get_project_names instead.'
    )
    def list_projects(self) -> List[str]:
        return self.get_project_names()  # noqa

    @deprecated(reason=f'list_models is deprecated and will be removed in future '
                       f'versions. Use get_model_names instead.')
    def list_models(self, project_id) -> List[str]:
        return self.get_model_names(project_name=project_id)  # noqa
