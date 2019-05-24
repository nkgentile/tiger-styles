# flask app using s3 to store files
import boto3
import logging
from botocore.exceptions import ClientError
from tools.config import S3_BUCKET, S3_KEY, S3_SECRET

class StorageUtils:
    def __init__(self):
        try:
            self.s3_resource = boto3.resource( "s3",
                    aws_access_key_id = S3_KEY,
                    aws_secret_access_key = S3_SECRET
            )
        except ClientError as e:
            logging.error(e)
            raise e

    def fileUpload(self, srcFile, tarFile):
        """
        srcFile: input file with path
        tarFile: output object inside storage

        returns: Boolean, Message
        """
        try:
            self.s3_resource.Bucket(S3_BUCKET).upload_file(Filename=srcFile, Key=tarFile)
        except ClientError as e:
            logging.error(e)
            return False, "Couldn't upload to S3 - src:{} tar:{}".format(srcFile,tarFile)
        return True, "{} uploaded as {}".format(srcFile, tarFile)

    def downloadFile(self, srcFile, tarFile):
        """
        srcFile: remote S3 file Name
        tarFile: local file with path
        returns: Boolean, location of downloaded file
        """
        try:
            self.s3_resource.Bucket(S3_BUCKET).download_file(srcFile, tarFile)
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                logging.error ("Key: {} object doesn't exist in S3 bucket".format(srcFile))
            else:
                raise e
            return False, "Couldn't upload to S3 - src:{} tar:{}".format(srcFile,tarFile)
        return True, "downloaded remote object into {}".format(tarFile)

    def removeFile(self, srcFile):
        try:
            self.s3_resource.Object(S3_BUCKET, srcFile).delete()
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                logging.error ("Key: {} object doesn't exist in S3 bucket".format(srcFile))
            else:
                raise e
        return True, "Remote file {} is deleted".format(srcFile)

    def listFiles(self):
        return self.s3_resource.Bucket(S3_BUCKET).objects.all()

    def _getBucketObj(self):
        return self.s3_resource.Bucket(S3_BUCKET)
