from minio import Minio


def upload(url, access_key, secret_key, bucket, file, dest):
    client = Minio(
        url,
        access_key=access_key,
        secret_key=secret_key
    )

    rs = client.fput_object(
        bucket,
        object_name=dest,
        file_path=file
    )

    return rs
