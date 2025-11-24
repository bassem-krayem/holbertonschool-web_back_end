#!/usr/bin/env python3
"""
a module for testing utils functions
"""
import unittest
from unittest.mock import patch
import utils
from utils import access_nested_map, get_json
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected: Any
    ) -> None:
        """ Test access_nested_map function with different inputs """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected: Any
    ) -> None:
        """ Test access_nested_map function for KeyError exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test get_json function
    """ 

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
        self,
        url: str,
        expected: Dict,
        mock_get: Callable
    ) -> None:
        """ Test get_json function with mocked requests.get """
        mock_get.return_value.json.return_value = expected
        self.assertEqual(get_json(url), expected)
        mock_get.assert_called_once_with(url)
