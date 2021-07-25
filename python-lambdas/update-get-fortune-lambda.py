import json
import boto3

def lambda_handler(event, context):

    client = boto3.client('lambda')
    response = client.update_function_code(
        FunctionName='get-fortune',
        S3Bucket='get-fortune',
        S3Key='get-fortune/Get-fortune/my-deployment-package.zip',
        Publish=True,
    )
        
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
        }
        

        # print('Closing Lambda function')
        # return {
        #     'statusCode': 400,
        #     'body': json.dumps(response)
        # }