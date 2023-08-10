import argparse
from file_upload import upload as upload

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Upload file to minio',
        description='The command upload file to minio',
    )
    parser.add_argument('--url', help='the host url')
    parser.add_argument('--access-key', help='the access-key')
    parser.add_argument('--secret-key', help='the secret-key')
    parser.add_argument('--bucket', help='the bucket name')
    parser.add_argument('--local-file', help='the local file')
    parser.add_argument('--remote-file', help='the remote file')
    args = parser.parse_args()

    url = args.url
    access_key = args.access_key
    secret_key = args.secret_key
    bucket = args.bucket
    local_file = args.local_file
    remote_file = args.remote_file
    try:
        upload(
            url,
            access_key,
            secret_key,
            bucket,
            local_file,
            remote_file
        )
    except Exception as ex:
        print("Error", ex)
