import boto3

region_name = 'us-east-1'
file_key = 'codebase.txt'

s3 = boto3.client('s3', region_name=region_name)

try:
    
    response = s3.get_object(Bucket='abhishek-cloud-assignment', Key=file_key)
    
   
    file_contents = response['Body'].read().decode('utf-8')

   
    print(f'File Key: {file_key}')
    print(f'File Size: {len(file_contents)} bytes')
    print(f'Last Modified: {response["LastModified"]}')
    print(f'File Contents:')
    print(file_contents)

except Exception as e:
    print(f'An error occurred: {str(e)}')
