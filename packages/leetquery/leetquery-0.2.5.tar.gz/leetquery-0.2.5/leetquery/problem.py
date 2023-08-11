"""
Copyright (c) 2023 Shu-Yu Huang

Licensed under the MIT License

Query data from Leetcode problems
"""
import json
import requests


def get_discription(problemname: str) -> str:
    """
    Get list of all problems
    Args:
        problemname: titleSlug of the problem
    Returns:
        str: html code of the problem
    
    """
    url = "https://leetcode.com/graphql?"
    headers = {'Content-Type': 'application/json'}
    query ="""
    query questionContent($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            content
        }
    }
    """
    variables = {"titleSlug": problemname}

    payload = {
        'query': query,
        'operationName': 'questionContent',
        'variables': variables
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload),
        timeout=3.0
    ).json()

    return response["data"]["question"]["content"]

def get_stats(problemname: str) -> dict:
    """
    Get list of all problems
    Args:
        problemname: titleSlug of the problem
    Returns:
        str: html code of the problem
    
    """
    url = "https://leetcode.com/graphql?"
    headers = {'Content-Type': 'application/json'}
    query ="""
    query questionStats($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            stats
        }
    }
    """

    variables = {"titleSlug": problemname}

    payload = {
        'query': query,
        'operationName': 'questionStats',
        'variables': variables
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload),
        timeout=3.0
    ).json()

    return eval(response["data"]["question"]["stats"])
