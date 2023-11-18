# coding: utf-8

"""
    😸 Cheshire-Cat API

    Open source and customizable AI architecture

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import cheshire_cat_api
from cheshire_cat_api.api.large_language_model_api import LargeLanguageModelApi  # noqa: E501
from cheshire_cat_api.rest import ApiException


class TestLargeLanguageModelApi(unittest.TestCase):
    """LargeLanguageModelApi unit test stubs"""

    def setUp(self):
        self.api = cheshire_cat_api.api.large_language_model_api.LargeLanguageModelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_llm_settings(self):
        """Test case for get_llm_settings

        Get Llm Settings  # noqa: E501
        """
        pass

    def test_get_llms_settings(self):
        """Test case for get_llms_settings

        Get Llms Settings  # noqa: E501
        """
        pass

    def test_upsert_llm_setting(self):
        """Test case for upsert_llm_setting

        Upsert Llm Setting  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()