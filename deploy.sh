#!/bin/bash
echo "Invoking Lambda function to trigger EMR job..."
aws lambda invoke \
  --function-name my-trigger-emr-lambda \
  --invocation-type Event \
  --payload '{}' \
  response.json
