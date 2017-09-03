import boto3
import boto3_ec2

elb_client = boto3.client('elb')

def elb_create_lb(lbname, sg_id, az):

    try:
        lb = elb_client.create_load_balancer(
            LoadBalancerName=lbname,
            Listeners=[
                {
                    'Protocol': 'HTTP',
                    'LoadBalancerPort': 80,
                    'InstanceProtocol': 'HTTP',
                    'InstancePort': 80
                }
            ],
            AvailabilityZones=az,
            SecurityGroups=[
                sg_id
            ],
            Tags=[
                {
                    'Key': lbname
                }
            ]
        )

        elb_client.modify_load_balancer_attributes(
            LoadBalancerName=lbname,
            LoadBalancerAttributes={
                'CrossZoneLoadBalancing': {
                    'Enabled': True
                },
                'AccessLog': {
                    'Enabled': False
                },
                'ConnectionDraining': {
                    'Enabled': True,
                    'Timeout': 60
                },
                'ConnectionSettings': {
                    'IdleTimeout': 60
                }
            }
        )

        elb_client.configure_health_check(
            LoadBalancerName=lbname,
            HealthCheck={
                'Target': 'TCP:80',
                'Interval': 10,
                'Timeout': 5,
                'UnhealthyThreshold': 5,
                'HealthyThreshold': 5
            }
        )

        print("LB is created, DNS: {}".format(lb['DNSName']))
        return 1
    except:
        return 0


# #Create a ELB
# sg_id = boto3_ec2.ec2_create_sg("web", "lb1_web")
# az = ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e", "us-east-1f"]
# elb_create_lb("lb1", sg_id, az)
#
# #Create EC2 Instance
# sg_name1 = ["myweb"]
# instanceid1 = boto3_ec2.ec2_create_instance("lb_web_vm1", sg_name1, "myweb", "us-east-1e")
# print(instanceid1)
#
#
# sg_name2 = ["myweb"]
# instanceid2 = boto3_ec2.ec2_create_instance("lb_web_vm2", sg_name2, "myweb", "us-east-1f")
# print(instanceid2)
#
#
# # #Attach EC2 instances
# elb_client.register_instances_with_load_balancer(LoadBalancerName='lb1', Instances=[{'InstanceId': instanceid1}, {'InstanceId': instanceid2}])
