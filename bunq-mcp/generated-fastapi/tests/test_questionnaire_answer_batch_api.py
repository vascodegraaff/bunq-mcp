# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.birdee_customer_questionnaire_answer_batch import BirdeeCustomerQuestionnaireAnswerBatch  # noqa: F401
from openapi_server.models.birdee_customer_questionnaire_answer_batch_create import BirdeeCustomerQuestionnaireAnswerBatchCreate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_questionnaire_answer_batch_for_user_birdee_customer(client: TestClient):
    """Test case for c_reate_questionnaire_answer_batch_for_user_birdee_customer

    
    """
    birdee_customer_questionnaire_answer_batch = {"questionnaire_type":"questionnaire_type","all_question_answer":[{"question":"question","all_answer":["all_answer","all_answer"]},{"question":"question","all_answer":["all_answer","all_answer"]}]}

    headers = {
        "cache_control": 'cache_control_example',
        "user_agent": 'user_agent_example',
        "x_bunq_language": 'x_bunq_language_example',
        "x_bunq_region": 'x_bunq_region_example',
        "x_bunq_client_request_id": 'x_bunq_client_request_id_example',
        "x_bunq_geolocation": 'x_bunq_geolocation_example',
        "x_bunq_client_authentication": 'x_bunq_client_authentication_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/questionnaire-answer-batch".format(userID=56, birdee-customerID=56),
    #    headers=headers,
    #    json=birdee_customer_questionnaire_answer_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

