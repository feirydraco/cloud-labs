import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    client = boto3.client('elastictranscoder')
    pipeline_id = <PIPELINE>
    
    sourceKey = event['Records'][0]['s3']['object']['key']
    outputKey = sourceKey.split('.')[0]
    
    response = client.create_job(
        PipelineId = pipeline_id,
        OutputKeyPrefix = outputKey + '/',
        Input = {
            'Key': sourceKey
        },
        Outputs = [
            {
                'Key': outputKey + '-1080p.mp4',
                'PresetId': '1351620000001-000001'
            },
            {
                'Key': outputKey + '-720p.mp4',
                'PresetId': '1351620000001-000010'
                
            }
        ]
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Execution complete.')
    }
