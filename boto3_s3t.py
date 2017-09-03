import boto3
import os

s3_resource = boto3.resource('s3')
s3_client = s3_resource.meta.client


def s3_list_buckets():
    buckets = []
    for bucket in s3_resource.buckets.all():
        buckets.append(bucket.name)

    return buckets


def s3_list_objects(bucketname):
    objects = []

    if 'Contents' in s3_client.list_objects(Bucket=bucketname).keys():
        for key in s3_client.list_objects(Bucket=bucketname)['Contents']:
            objects.append(key['Key'])

    return objects


def s3_del_object(bucketname, object):
    try:
        #Delete objects with versions
        if 'Status' in s3_client.get_bucket_versioning(Bucket=bucketname).keys():
            if 'Versions' in s3_client.list_object_versions(Bucket=bucketname).keys():
                for version in s3_client.list_object_versions(Bucket=bucketname)['Versions']:
                    if version['Key'] == object:
                        s3_client.delete_object(Bucket=bucketname, Key=version['Key'], VersionId=version['VersionId'])
        # This doesn't delete object versions
        else:
            found = 0
            for obj in s3_list_objects(bucketname):
                if obj == object:
                    s3_client.delete_object(Bucket=bucketname, Key=object)
                    return 1

            if found == 0:
                return 0
    except:
        return 0


def s3_del_bucket(bucketname):
    try:
        s3_client.delete_bucket(Bucket=bucketname)
    except:
        print("Error deleting bucket")


def s3_put_object(file, bucketname):
    try:
        s3_client.upload_file(file, bucketname, os.path.basename(file))
        return 1
    except:
        return 0

def s3_create_bucket(bucketname):
    try:
        s3_client.create_bucket(ACL='private', Bucket=bucketname)
        return 1
    except:
        return 0

# #List buckets and objects
# for bucket in s3_list_buckets():
#     s3_list_objects(bucket)
#
# #Delete object
# bucket = "drthretherthwrthrewth"
# object = "test.php"
# if s3_del_object(bucket, object):
#     print("{} was successfully deleted from {} bucket".format(object, bucket))
# else:
#     print("Error, object not found in {} bucket".format(bucket))
#
# #Delete bucket
# s3_del_bucket(bucket)
#
# #Create bucket
# s3_create_bucket("testbucket287346")
#
# #Upload file
# if s3_put_object("/Users/admin/Downloads/Python.docx", "ljkahsdkjfhasdf"):
#     print("Successfully uploaded file")
# else:
#     print("There was an error during upload")


