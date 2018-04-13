from __future__ import print_function

import json
import boto3

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    message = event['Message']
    parsed_message = json.loads(message)
    image_id = parsed_message['ECSAmis'][0]['Regions']['us-east-1']['ImageId']
    print("From SNS: " + image_id)
    #return message
    
    sf_client = boto3.client('stepfunctions')
    
    response = sf_client.start_execution(
        stateMachineArn='arn:aws:states:us-east-1:xxxx:stateMachine:UpdateECSCluster',
        name='UpdateECSCluster',
        input=json.dumps(image_id)
    )
