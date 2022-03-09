from behave import given, when, then
import requests
import json
from jsonschema import validate

from features.steps.utils import get_json_data

api_url = "https://api.spotify.com/v1/"
token = ""
headers = {'Authorization': "Bearer {}".format(token)}
params = {}


@given(u'the endpoint {endpoint}')
def step_impl(context, endpoint):
    context.url = api_url + endpoint + '/'


@given(u'id {resource_id}')
def step_impl(context, resource_id):
    context.url = context.url + resource_id


@given(u'param {parameter} {value}')
def step_impl(context, parameter, value):
    params[parameter] = value
    context.data = params


@when(u'method get')
def step_impl(context):
    context.response = requests.get(context.url, headers=headers)


@when(u'method put with params')
def step_impl(context):
    context.response = requests.put(context.url, params=context.data, headers=headers)


@then(u'the response status is {response_status}')
def step_impl(context, response_status):
    assert int(context.response.status_code) == int(response_status)


@then(u'the response matches {response_schema} schema')
def step_impl(context, response_schema):
    expected_response = get_json_data("../schemas/", response_schema)
    response_content = json.loads(context.response.content)
    validate(response_content, expected_response)


@then(u'the response equals {response_json} json')
def step_impl(context, response_json):
    expected_response = get_json_data("../json_responses/", response_json)
    response_content = json.loads(context.response.content)
    print(response_content)
    assert expected_response == response_content
