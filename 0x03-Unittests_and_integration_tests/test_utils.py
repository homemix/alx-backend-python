#!/usr/bin/env python3
"""
a class to test the utils.py file
"""
from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    a class to test the utils.py file
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        a test to test the access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        a test to test the access_nested_map function
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    a class to test get json method
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, payload):
        """
        a test to test the get_json function
        """
        with patch("utils.requests.get") as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(get_json(test_url), payload)
            self.assertEqual(mock_get.call_count, 1)


if __name__ == "__main__":
    unittest.main()
