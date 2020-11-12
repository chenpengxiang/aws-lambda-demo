import json

data = ['鞋子', '鞋子尺寸', '鞋子理论', '鞋子品牌', '鞋子码数',
        'aws', 'aws收费模式', 'aws SQS', 'aws S3', 'aws lambda', 'aws rds',
        'lang-go', 'lang-java', 'lang-python', 'lang-c', 'lang-js', 'lang-rust'
        ]

def getData(event, context):
    result = []
    if 'pathParameters' in event and 'query' in event['pathParameters']:
        result = [x for x in data if x.startswith(event['pathParameters']['query'])]

    if not result:
        print(f'cannot find the data for event: {event}')
    
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            "content-type" : "application/json"
        },
        "body": json.dumps(result, ensure_ascii=False).encode('utf8')
    }

    return response
