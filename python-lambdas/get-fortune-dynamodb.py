import json
import boto3
from boto3.dynamodb.conditions import Key
import random

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    Fortune_table = dynamodb.Table('Fortunes')
    
    Scan_fortunes = Fortune_table.scan()
    Total_fortunes = Scan_fortunes['Count']
    Random_fortune = random.randint(1, Total_fortunes)
    
    response = Fortune_table.get_item(Key={
       'fortune_id': Random_fortune
    })
    
        
    
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": response['Item']
    }
