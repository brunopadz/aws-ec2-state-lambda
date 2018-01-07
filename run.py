import boto3

ec2 = boto3.resource('ec2')

stopped_instances = ec2.instances.filter(
    Filters=[
        {
            'Name': 'tag-key',
            'Values': ['sched'],
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }
    ]
)

running_instances = ec2.instances.filter(
    Filters=[
        {
            'Name': 'tag-key',
            'Values': ['sched'],
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

for instance in stopped_instances:
    stopped_instances.start()


for instance in running_instances:
    running_instances.stop()
