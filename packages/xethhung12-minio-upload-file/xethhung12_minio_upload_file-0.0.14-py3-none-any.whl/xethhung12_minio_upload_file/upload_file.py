import os
from xethhung12_minio_common import create_client, create_proxy, write_etag


def upload(url, access_key, secret_key, bucket, file, dest):
    file = os.path.abspath(file)

    client = create_client(url, access_key, secret_key, create_proxy())

    rs = client.fput_object(
        bucket,
        object_name=dest,
        file_path=file
    )
    write_etag(file, rs.etag)
    return rs
