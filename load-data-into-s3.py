import boto3

def load_data_into_s3(access_key,
                      secret_key,
                      file_name,
                      bucket_name,
                      region):
    s3 = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key,
                      region_name=region 
                      )

    # Uploads the given file using a managed uploader,
    # which will split up large file anutomatically
    # and upload parts in parallel
    s3.upload_file(file_name, bucket_name, file_name)
    


