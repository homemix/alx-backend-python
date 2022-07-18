#!/usr/bin/env python3
"""
a class to test the github_org_client.py file
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    a test to test the org function
    """

    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch('client.GithubOrgClient.org')
    def test_org(self, name, mock_org):
        """
        a method to test org method
        """

        github_org_client = GithubOrgClient(name)
        github_org_client.org()
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """
        a method to test public_repos_url method
        """
        with patch('client.GithubOrgClient.org') as mock_org:
            mock_org.return_value = "https://api.github.com/orgs/google"
            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client._public_repos_url,
                             "https://api.github.com/orgs/google")

    def test_public_repos(self):
        """
        a method to test public_repos method
        """
        with patch('client.GithubOrgClient.org') as mock_org:
            mock_org.return_value = "https://api.github.com/orgs/google"
            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client.public_repos(),
                             ["google-python-client", "google-python-examples"])
            mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()
