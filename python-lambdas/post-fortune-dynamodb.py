import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    Fortune_table = dynamodb.Table('Fortunes')
    fortune = event['fortune']
    
    # Query Dynamodb for total number of records 
    Scan_fortunes = Fortune_table.scan()
    Total_fortunes = Scan_fortunes['Count']
    fortune_id = Total_fortunes + 1
    
    response = Fortune_table.put_item(
        Item={
            'fortune': fortune,
            'fortune_id': fortune_id
        }
    )
    
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
    