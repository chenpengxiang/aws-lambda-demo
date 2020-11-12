import unittest
import json
from handler import getData

EMPTY_RESULT = b'[]'

class TestGetDataMethod(unittest.TestCase):
    
    def test_with_valid_api_gateway_event(self):
        event = {'version': '1.0', 'resource': '/data/{query}', 'path': '/data/%E9%9E%8B%E5%AD%90', 
        'httpMethod': 'GET', 'X-Forwarded-For': ['84.17.34.143'], 
        'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https'], 
        'accept': ['application/json, text/javascript, */*; q=0.01'], 
        'httpMethod': 'GET', 
        'pathParameters': {'query': '鞋子'}, 'stageVariables': None, 'body': None, 'isBase64Encoded': False}

        response = getData(event, {})
        expect_data = ["鞋子", "鞋子尺寸", "鞋子理论", "鞋子品牌", "鞋子码数"]

        self.assertEqual(200, response['statusCode'])
        self.assertEqual(json.dumps(expect_data, ensure_ascii=False).encode('utf8'), response['body'])


    def test_with_unknown_path_event(self):
        event = {'version': '1.0', 'resource': '/data/{query}', 'path': '/data/unknown', 
        'httpMethod': 'GET', 'X-Forwarded-For': ['84.17.34.143'], 
        'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https'], 
        'accept': ['application/json, text/javascript, */*; q=0.01'], 
        'httpMethod': 'GET', 
        'pathParameters': {'query': 'unknown'}, 'stageVariables': None, 'body': None, 'isBase64Encoded': False}
        response = getData(event, {})
        self.assertEqual(200, response['statusCode'])
        self.assertEqual(EMPTY_RESULT, response['body'])

        