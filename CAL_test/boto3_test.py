import boto3

session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id='6d0ea4ae46924038840023818e4355a2',
    aws_secret_access_key='8bb3d8dfbfac475d85bab35962a82d40',
    endpoint_url='http://192.168.122.150:8080',
    use_ssl=False,
    region_name='RegionOne'
)
s3_client.create_bucket(Bucket='bucket1')
bucket_list_resp = s3_client.list_buckets()
pass
