import unittest
from http import HTTPStatus
from typing import List
from unittest.mock import patch

from fiddler.core_objects import BaselineType
from fiddler.exceptions import (
    BadRequest,
    NotFound,
)
from fiddler.schema.baseline import Baseline
from tests.fiddler.base import BaseTestCase
from tests.fiddler.helper import (
    get_404_error_response,
    get_base_api_response_body,
    get_base_paginated_api_response_body,
)


class TestBaseline(BaseTestCase):
    def setUp(self):
        super(TestBaseline, self).setUp()
        self._project_name = 'test_project'
        self._baseline_name = 'test_baseline'
        self._model_name = 'test_model'
        self._dataset_name = 'test-dataset'

    def _get_url_query_params(
        self,
        organization_name: str = None,
        project_name: str = None,
        baseline_name: str = None,
        model_name: str = None,
    ) -> str:
        base_url = f'{self._url}/baselines/'
        if organization_name and project_name and model_name and baseline_name:
            return f'{base_url}?organization_name={organization_name}&project_name={project_name}&model_name={model_name}&baseline_name={baseline_name}'

        if organization_name and project_name and model_name:
            return f'{base_url}?organization_name={organization_name}&project_name={project_name}&model_name={model_name}'

        if organization_name and project_name:
            return f'{base_url}?organization_name={organization_name}&project_name={project_name}'

        if organization_name:
            return f'{base_url}?organization_name={organization_name}'

        return base_url

    def _get_paginated_response_json(self, item_count=3):
        response = get_base_paginated_api_response_body(
            items=[
                self._create_baseline_dict(
                    id=i,
                    name=f'baseline_{i}',
                    type=BaselineType.PRE_PRODUCTION.value,
                    dataset_id=self._dataset_name,
                )
                for i in range(item_count)
            ],
            item_count=item_count,
        )
        return response

    def _create_baseline_dict(
        self,
        id: int,
        name: str,
        type: str,
        dataset_id: str = None,
        start_time=None,
        end_time=None,
        offset=None,
        window_size=None,
    ):
        return {
            'id': id,
            'name': name,
            'organization_name': self._org,
            'project_name': self._project_name,
            'type': type,
            'model_name': self._model_name,
            'dataset_name': dataset_id,
            'start_time': start_time,
            'end_time': end_time,
            'offset': offset,
            'window_size': window_size,
        }

    def test_add_baseline(self):
        id = 0
        response_body = get_base_api_response_body(
            data=self._create_baseline_dict(
                id=id,
                name=self._baseline_name,
                type=BaselineType.PRE_PRODUCTION,
                dataset_id=self._dataset_name,
            ),
        )

        url = self._get_url_query_params()

        self.requests_mock.post(url, json=response_body)

        baseline = self.client.add_baseline(
            self._project_name,
            self._model_name,
            self._baseline_name,
            type=BaselineType.PRE_PRODUCTION,
            dataset_name=self._dataset_name,
        )

        self.assertIsInstance(baseline, Baseline)
        self.assertEqual(baseline.id, id)
        self.assertEqual(baseline.name, self._baseline_name)
        self.assertEqual(baseline.type, BaselineType.PRE_PRODUCTION)
        self.assertEqual(baseline.dataset_name, self._dataset_name)

    @patch('fiddler.api.baseline_mixin.RequestClient.post')
    def test_baseline_construction_add_baseline(self, post_request):
        test_ds_id = self._dataset_name
        baseline = self.client.add_baseline(
            self._project_name,
            self._model_name,
            self._baseline_name,
            type=BaselineType.PRE_PRODUCTION,
            dataset_name=test_ds_id,
        )
        post_request.assert_called_once_with(
            url='baselines/',
            data={
                'project_name': self._project_name,
                'organization_name': self._org,
                'name': self._baseline_name,
                'dataset_name': test_ds_id,
                'start_time': None,
                'end_time': None,
                'window_size': None,
                'offset': None,
                'model_name': self._model_name,
                'type': BaselineType.PRE_PRODUCTION.value,
                'run_async': True,
            },
        )

    def test_add_baseline_twice_nofail(self):
        id = 0
        response_body = get_base_api_response_body(
            data=self._create_baseline_dict(
                id=id,
                name=self._baseline_name,
                type=BaselineType.PRE_PRODUCTION,
                dataset_id=self._dataset_name,
            ),
        )

        url = self._get_url_query_params()

        self.requests_mock.post(url, json=response_body)

        baseline = self.client.add_baseline(
            self._project_name,
            self._model_name,
            self._baseline_name,
            type=BaselineType.PRE_PRODUCTION,
            dataset_name=self._dataset_name,
        )

        baseline = self.client.add_baseline(
            self._project_name,
            self._model_name,
            self._baseline_name,
            type=BaselineType.PRE_PRODUCTION,
            dataset_name=self._dataset_name,
        )

    def test_add_baseline_different_fail(self):
        id = 0
        response_body = get_base_api_response_body(
            data=self._create_baseline_dict(
                id=id,
                name=self._baseline_name,
                type=BaselineType.PRE_PRODUCTION,
                dataset_id=self._dataset_name,
            ),
        )

        url = self._get_url_query_params()

        self.requests_mock.post(url, json=response_body)
        baseline = self.client.add_baseline(
            self._project_name,
            self._model_name,
            self._baseline_name,
            type=BaselineType.PRE_PRODUCTION,
            dataset_name=self._dataset_name,
        )

        self.requests_mock.post(url, json=response_body, status=HTTPStatus.BAD_REQUEST)
        with self.assertRaises(BadRequest):
            baseline = self.client.add_baseline(
                self._project_name,
                self._model_name,
                self._baseline_name,
                type=BaselineType.PRE_PRODUCTION,
                dataset_name='test_dataset_2',
            )

    def test_add_baseline_no_dataset_name_fail(self):
        id = 0
        response_body = get_base_api_response_body(
            data=self._create_baseline_dict(
                id=id,
                name=self._baseline_name,
                type=BaselineType.PRE_PRODUCTION,
            ),
        )

        url = self._get_url_query_params()

        self.requests_mock.post(url, json=response_body, status=HTTPStatus.BAD_REQUEST)
        with self.assertRaises(BadRequest):
            baseline = self.client.add_baseline(
                self._project_name,
                self._model_name,
                self._baseline_name,
                type=BaselineType.PRE_PRODUCTION,
                dataset_name='test_dataset_2',
            )

    def test_get_baselines(self):
        url = self._get_url_query_params(self._org, self._project_name)
        item_count = 4
        self.requests_mock.get(url, json=self._get_paginated_response_json(item_count))
        baselines = self.client.get_baselines(self._project_name)
        self.assertTrue(isinstance(baselines, List))
        self.assertIsInstance(baselines[0], Baseline)
        self.assertEqual(len(baselines), item_count)

    def test_get_baselines_empty_list(self):
        url = self._get_url_query_params(self._org, self._project_name)
        self.requests_mock.get(url, json=self._get_paginated_response_json(0))
        baselines = self.client.get_baselines(self._project_name)
        self.assertTrue(isinstance(baselines, List))
        self.assertListEqual(baselines, [])

    def test_get_baseline(self):
        id = 0
        response_body = self._get_paginated_response_json(1)

        url = self._get_url_query_params(
            self._org, self._project_name, self._baseline_name, self._model_name
        )

        self.requests_mock.get(url, json=response_body)

        baseline = self.client.get_baseline(
            self._project_name, self._model_name, self._baseline_name
        )

        self.assertIsInstance(baseline, Baseline)
        self.assertEqual(baseline.id, id)
        self.assertEqual(
            baseline.name, 'baseline_0'
        )  # get_paginated_response_json always generates baseline name of the form "baseline_{idx}"
        self.assertEqual(baseline.type, BaselineType.PRE_PRODUCTION)
        self.assertEqual(baseline.dataset_name, self._dataset_name)

    def test_delete_baseline(self):
        url = self._get_url_query_params(
            self._org, self._project_name, self._baseline_name, self._model_name
        )
        self.requests_mock.delete(url, status=HTTPStatus.OK)
        self.client.delete_baseline(
            self._project_name, self._model_name, self._baseline_name
        )

        with self.assertRaises(ValueError):
            self.client.delete_baseline(baseline_name=self._baseline_name)

        with self.assertRaises(ValueError):
            self.client.delete_baseline(project_name=self._project_name)

    def test_get_baseline_404(self):
        url = self._get_url_query_params(
            self._org, self._project_name, self._baseline_name, self._model_name
        )
        self.requests_mock.get(
            url, json=get_404_error_response(), status=HTTPStatus.NOT_FOUND
        )
        with self.assertRaises(NotFound) as e:  # noqa
            self.client.get_baseline(
                self._project_name, self._model_name, self._baseline_name
            )


if __name__ == '__main__':
    unittest.main()
