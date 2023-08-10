"""
Copyright (c) 2023 Shu-Yu Huang

Licensed under the MIT License

Query info from Leetcode users
"""
import json
from typing import List, Union
import requests

__all__  = ["get_submissions"]

def get_submissions(
        username: str="syhaung",
        limit: int=12,
        title_only: bool=True
    )-> List[Union[str, dict]]:
    """
    Get submissions from user
    Args:
        username (str): username of the user
        limit (int): number of submissions to return
        title_only (bool): whether to return only title or not
    Returns:
        List[str | dict]: list of submissions, if title_only==False, then return a dictionary of query
    """
    url = "https://leetcode.com/graphql?"
    headers = {'Content-Type': 'application/json'}
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            title
            titleSlug
        }
    }
    """
    variables = {'username': username, 'limit': limit}
    payload = {
        'query': query,
        'operationName': 'recentAcSubmissions',
        'variables': variables
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload),
        timeout=2.0
    ).json()

    if title_only:
        return [x["title"] for x in response["data"]["recentAcSubmissionList"]]
    else:
        return [x for x in response["data"]["recentAcSubmissionList"]]
