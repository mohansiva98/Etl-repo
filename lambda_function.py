import boto3
import time

emr = boto3.client('emr-serverless')
app_id = '00ftn3gk35e5md09'  # Replace with your actual Application ID
s3_bucket = 'etl-emr-input-bucket-yourname'
job_role = 'arn:aws:iam::375046931023:role/EMRServerlessLambdaFullAccess'

def lambda_handler(event, context):
    response = emr.start_job_run(
        applicationId=app_id,
        executionRoleArn=job_role,
        jobDriver={
            'sparkSubmit': {
                'entryPoint': f's3://{s3_bucket}/etl_job.py',
                'sparkSubmitParameters': '--conf spark.executor.memory=2G --conf spark.executor.cores=2'
            }
        },
        configurationOverrides={
            "monitoringConfiguration": {
                "s3MonitoringConfiguration": {
                    "logUri": f"s3://{s3_bucket}/logs/"
                }
            }
        },
        name='etl-spark-job'
    )
    
    print("Job submitted:", response['jobRunId'])
    return {"jobRunId": response['jobRunId']}
