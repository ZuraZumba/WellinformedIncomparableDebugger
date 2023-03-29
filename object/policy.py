def set_object_access_policy(aws_s3_client, bucket_name, file_name):
  response = aws_s3_client.put_object_acl(ACL="public-read",
                                          Bucket=bucket_name,
                                          Key=file_name)
  status_code = response["ResponseMetadata"]["HTTPStatusCode"]
  if status_code == 200:
    return True
  return False


lifecycle_configuration = {
  'Rules': [{
    'ID': 'delete-objects-after-120-days',
    'Status': 'Enabled',
    'Prefix': '',
    'Expiration': {
      'Days': 120
    },
    'NoncurrentVersionExpiration': {
      'NoncurrentDays': 120
    }
  }]
}


def lifecycle(aws_s3_client, bucket_name):
  response = aws_s3_client.put_bucket_lifecycle_configuration(
    Bucket=bucket_name, LifecycleConfiguration=lifecycle_configuration)
  return response
