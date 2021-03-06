"""Tests for ai.py and api_utils.py that mock the json responses that would be returned from the lab server
"""
import os
import pandas as pd

os.environ["LAB_HOST"] = "lab"
os.environ['LAB_PORT'] = "5080"
os.environ['APIKEY'] = "aaaaa"

from ai.ai import AI
import ai.ai
from ai.api_utils import LabApi
import ai.recommender.random_recommender
import sys
import json
from unittest.mock import Mock, patch
import lab_api_mocker as mocker


@patch('ai.api_utils.LabApi')
def test_ai_init( mockLabApi): #, mockRequestsPost
    labApiInstance = mockLabApi.return_value

    labApiInstance.launch_experiment.return_value = {'launch_experiment'}
    labApiInstance.get_projects.return_value = {'get_projects'}
    labApiInstance.get_filtered_datasets.return_value = {'get_filtered_datasets'}
    labApiInstance.get_new_experiments.return_value = {'get_new_experiments'}
    labApiInstance.set_ai_status.return_value = {'set_ai_status'}
    labApiInstance.get_all_ml_p.return_value = pd.DataFrame(
            {'algorithm':['testAlgo','testAlgo'],
             'parameters':[{'criterion':'gini','max_depth':2},
                           {'criterion':'entropy','max_depth':3}]
             })

    lab_connection_args = {}
    pennai = AI()
