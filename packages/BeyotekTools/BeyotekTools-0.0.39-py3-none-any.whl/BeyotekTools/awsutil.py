import boto3
from botocore.exceptions import ClientError


def create_ec2_instance(ImageId, MinCount=1, MaxCount=1, InstanceType="t2.nano", KeyName="ec2-key"):
    try:
        print("Creating EC2 Instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId=ImageId,
            MinCount=MinCount,
            MaxCount=MaxCount,
            KeyName=KeyName,
            InstanceType=InstanceType
        )
    except Exception as e:
        print(e)

def create_ec2_instance_from_launch_template(LaunchTemplateId, MinCount=1, MaxCount=1):
    try:
        print("Creating EC2 Instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            MinCount=MinCount,
            MaxCount=MaxCount,
            LaunchTemplate={
                'LaunchTemplateId': LaunchTemplateId
#                'LaunchTemplateName': 'string',
#                'Version': 'string'
            }
        )
    except Exception as e:
        print(e)


def get_ec2_instances():
    try:
        resource_ec2 = boto3.client("ec2")
        return resource_ec2.describe_instances()["Reservations"]
    except Exception as e:
        print(e)


def reboot_ec2_instance(instance_id):
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.reboot_instances(InstanceIDs=[instance_id])
        print(f"Reboted Instance {instance_id}")
    except Exception as e:
        print(e)


def stop_ec2_instance(instance_id):
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.stop_instances(InstanceIDs=[instance_id])
        print(f"Stopped Instance {instance_id}")
    except Exception as e:
        print(e)


def start_ec2_instance(instance_id):
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.start_instances(InstanceIDs=[instance_id])
        print(f"Started Instance {instance_id}")
    except Exception as e:
        print(e)


def start_ec2_terminate(instance_id):
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.terminate_instances(InstanceIDs=[instance_id])
        print(f"Terminating Instance {instance_id}")
    except Exception as e:
        print(e)

def add_security_group_ingress(groupid,protocal,fromport,toport,ip):
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.authorize_security_group_ingress(
            GroupId=groupid,
            IpProtocol=protocal,
            FromPort=int(fromport),
            ToPort=int(toport),
            CidrIp=ip
        )
        print(f"Added Inboud Rule To Security Group {groupid}")
    except Exception as e:
        print(f"Could Not Add In Boud Rule Error:{e}")