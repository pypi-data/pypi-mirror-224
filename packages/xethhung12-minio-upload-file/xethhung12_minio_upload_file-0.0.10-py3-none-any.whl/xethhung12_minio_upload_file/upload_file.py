import os

import urllib3
from minio import Minio

def create_proxy():
    proxy_env = os.getenv('http_proxy')
    if proxy_env != None:
        print("Using proxy: ", proxy_env)
    return urllib3.ProxyManager(
        proxy_env,
        timeout=urllib3.Timeout.DEFAULT_TIMEOUT,
        cert_reqs='CERT_REQUIRED',
        retries=urllib3.Retry(
            total=5,
            backoff_factor=0.2,
            status_forcelist=[500, 502, 503, 504]
        )
    ) if proxy_env is not None else None

def upload(url, access_key, secret_key, bucket, file, dest):
    file = os.path.abspath(file)
    proxy = create_proxy()
    client = Minio(
        url,
        access_key=access_key,
        secret_key=secret_key,
        http_client=proxy
    ) if proxy is not None else Minio(
        url,
        access_key=access_key,
        secret_key=secret_key
    )

    rs = client.fput_object(
        bucket,
        object_name=dest,
        file_path=file
    )
    write_etag(file, rs.etag)
    return rs

def write_etag(file_path, etag):
    with open(f"{file_path}.etag", 'w') as f:
        f.write(etag)
