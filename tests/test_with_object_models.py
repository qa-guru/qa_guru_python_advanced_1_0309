import json

import requests
from jsonschema import validate

from model.reqres import ResponseGetUser, User, ResponseUser, Reqres


def test_get_user(reqresin):
    expected_response_get_user = ResponseGetUser(data=ResponseUser(
        id=2,
        email="janet.weaver@reqres.in",
        first_name="Janet",
        last_name="Weaver",
        avatar="https://reqres.in/img/faces/2-image.jpg"
    ))

    result_response_get_user = ResponseGetUser(response=reqresin.get("/api/users/2", verify=False))

    assert result_response_get_user.support_url == expected_response_get_user.support_url
    assert result_response_get_user.json == expected_response_get_user.json


def test_get_user_with_object_model(env):
    expected_response_get_user = ResponseGetUser(data=ResponseUser(
        id=2,
        email="janet.weaver@reqres.in",
        first_name="Janet",
        last_name="Weaver",
        avatar="https://reqres.in/img/faces/2-image.jpg"
    ))

    result_response_get_user = Reqres(env).get_user(2)

    assert result_response_get_user.support_url == expected_response_get_user.support_url
    assert result_response_get_user.json == expected_response_get_user.json
