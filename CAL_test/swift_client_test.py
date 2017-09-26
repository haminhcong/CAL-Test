from keystoneauth1 import session
from keystoneauth1.identity import v3
from swiftclient.client import Connection

# Create a password auth plugin
auth = v3.Password(auth_url='http://192.168.122.100:5000/v3/',
                   username='admin',
                   password='bkcloud',
                   user_domain_name='Default',
                   project_name='admin',
                   project_domain_name='Default')

# Create session
keystone_session = session.Session(auth=auth)

# Create swiftclient Connection
swift_connection = Connection(session=keystone_session)

test_container_name = 'test_mcos_containers'
test_object_name = 'sample_2.iso'

try:
    swift_connection.put_container(test_container_name)

    with open('./media/configs/sample_2.iso',
              'r') as sample_file_content:
        swift_connection.put_object(
            test_container_name,
            test_object_name,
            contents=sample_file_content,
        )
except Exception as e:
    pass
pass
resp_headers, containers = swift_connection.get_account()
for container in containers:
    print(container)