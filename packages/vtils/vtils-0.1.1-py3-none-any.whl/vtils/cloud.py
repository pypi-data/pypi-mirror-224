import boto3
from botocore.exceptions import ClientError
import os
import logging

class AwsCloudtils(object):
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        self.client = boto3.client('s3',
                            aws_access_key_id=self.access_key,
                            aws_secret_access_key=self.secret_key,
                        )

    def upload_file(self, fpath, bucket, object_name=None):
        if object_name is None:
            object_name = os.path.basename(fpath)
        try:
            response = self.client.upload_file(fpath, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def download_file(self, bucket, object_name, fpath):
        try:
            self.client.download_file(bucket, object_name, fpath)
        except ClientError as e:
            logging.error(e)
            return False
        return True
