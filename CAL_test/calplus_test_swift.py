import os

from calplus.client import Client
from calplus.provider import Provider


def get_env():
    cloud_type = 'openstack'
    cloud_config = {
        'os_auth_url': 'http://192.168.122.100:35357/v3',
        'os_project_name': 'admin',
        'os_username': 'admin',
        'os_password': 'bkcloud',
        'os_project_domain_name': 'Default',
        'os_user_domain_name': 'Default',
        'os_identity_api_version': '3',
        'os_auth_version': '3',
        'os_swiftclient_version': '2.0',
    }
    return cloud_type, cloud_config


def main():
    cloud_type, cloud_config = get_env()
    provider = Provider(cloud_type, cloud_config)
    # Client for object storage
    client = Client(version='1.0.0', resource='object_storage',
                    provider=provider)
    test_container_name = 'test_mcos_containers'
    test_object_name = 'sample_2.iso'
    try:
        client.create_container(test_container_name)
        with open('./media/configs/sample_2.iso',
                  'r') as sample_file_content:
                client.upload_object(obj=test_object_name,
                                     container=test_container_name,
                                     contents=sample_file_content)

        test_result = client.driver.list_containers()
        test_file_length = os.path.getsize('./media/configs/sample_file.txt')
        object_info = client.stat_object(test_container_name,
                                         test_object_name)
        # downloaded_object_data = client.download_object(test_container_name,
        #                                               test_object_name)
        # client.delete_object(test_container_name,test_object_name)
        # client.delete_container(test_container_name)
        pass
        # Add more tests bellow
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
