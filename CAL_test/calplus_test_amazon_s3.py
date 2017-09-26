import os

from calplus.client import Client
from calplus.provider import Provider


def get_env():
    cloud_type = 'amazon'
    cloud_config = {
        "aws_access_key_id": "6d0ea4ae46924038840023818e4355a2",
        "aws_secret_access_key": "8bb3d8dfbfac475d85bab35962a82d40",
        "region_name": "RegionOne",
        "endpoint_url": "http://192.168.122.150:8080"
    }
    return cloud_type, cloud_config


def main():
    cloud_type, cloud_config = get_env()
    provider = Provider(cloud_type, cloud_config)
    # Client for object storage
    client = Client(version='1.0.0', resource='object_storage',
                    provider=provider)
    try:
        create_container_result = client.create_container(
            'test.mcos.containers')
        test_result = client.driver.list_containers()
        # object_list = client.list_container_objects(container='test_ctn')
        pass
        # Add more tests bellow
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
