import boto3
import os
import datetime

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

def date_diff(inputtime):
    now = datetime.datetime.utcnow()
    created = datetime.datetime.strptime( str(inputtime).split("+")[0], '%Y-%m-%d %H:%M:%S')

    print(now, created)
    print(now - created)

    minutes_diff = (now - created).total_seconds() // 60


    if minutes_diff >= 1440:
        days = minutes_diff // 1440
        hours = ((minutes_diff % 1440) // 60)
        minutes = ((minutes_diff % 1440) % 60)

    elif minutes_diff >= 60:
        days = 0
        hours = (minutes_diff // 60)
        minutes = ( minutes_diff % 60)
    else:
        days = 0
        hours = 0
        minutes = int(minutes_diff)

    return "Up - " + str(days) + "d:" + str(hours) + "h:" + str(minutes) + "m"


def ec2_create_sg(type, sgname):

    # try:
    if type == 'ssh':
        response = ec2_client.create_security_group(GroupName=sgname, Description='SG for ssh')
        ec2_client.authorize_security_group_ingress(
            GroupId=response['GroupId'],
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ]
        )
        print("Security GroupID {} was crated".format(response['GroupId']))
        return response['GroupId']
    elif type == 'web':
        response = ec2_client.create_security_group(GroupName=sgname, Description='SG for web')
        ec2_client.authorize_security_group_ingress(
            GroupId=response['GroupId'],
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 443,
                 'ToPort': 443,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ]
        )
        print("Security GroupID {} was crated".format(response['GroupId']))
        return response['GroupId']
    else:
        print("Security Group creation process had failed, unknown type!")
        return 0
    # except:
    #         print("Security Group creation process had failed, very likely due to duplicate SG Naming!")
    #         return 0


def ec2_create_key(keyname):
    my_path = os.path.expanduser("~/" + keyname + "_ssh.pem")

    try:
        if os.path.exists(my_path) and os.path.getsize(my_path) > 0:
            print("Warning!!! Key wasn't created because " + my_path + " already exists")
            return 0
        else:
            keypair = ec2_client.create_key_pair(KeyName=keyname)

            print("Key is being exported to "  + my_path)
            with open(my_path, "w+") as line:
                print(keypair['KeyMaterial'], file=line)
                print(keypair['KeyMaterial'])
            line .close()
            return 1
    except:
            return 0


def ec2_create_instance(instancename, sg_name, key, az):

    try:
        instance = ec2_resource.create_instances(
            ImageId='ami-4fffc834',
            InstanceType='t2.micro',
            KeyName=key,
            MaxCount=1,
            MinCount=1,
            Placement={
                'AvailabilityZone': az
            },
            SecurityGroups=sg_name,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': instancename,
                            'Value': instancename
                        }
                    ]
                }
            ]
        )
        return instance[0].id
    except:
        return 0

def ec2_list_instances():

    try:
        response = ec2_client.describe_instances()
        if 'Reservations' in response.keys():
            for reservation in response["Reservations"]:
                if 'Instances' in reservation.keys():
                    for instance in reservation["Instances"]:
                        if 'InstanceId' in instance:
                            if instance["State"]["Name"] == 'running':
                                print(instance["InstanceId"], instance["InstanceType"], date_diff(instance["LaunchTime"]), instance["Placement"]["AvailabilityZone"], instance["PublicIpAddress"], instance["State"]["Name"], instance["VpcId"])
                            else:
                                print(instance["InstanceId"], instance["InstanceType"], instance["LaunchTime"], instance["Placement"]["AvailabilityZone"], instance["State"]["Name"])
        return 1
    except:
        return 0


# # Create EC2 SG
# ec2_create_sg("web", "myweb")
#
# #Create EC2 Key
# ec2_create_key("myweb")
#
# #Create EC2 Instance
# sg_name = ["myweb"]
# ec2_create_instance("lb_myweb1", sg_name, "myweb", "us-east-1a")
# ec2_create_instance("lb_myweb2", sg_name, "myweb", "us-east-1b")
#
# # List instances
# ec2_list_instances()


