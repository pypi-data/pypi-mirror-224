import os

import urllib3
from minio import Minio


def check_is_latest(file_path):
    etag = list(filter(lambda x: x == f"{file_path}.etag", os.listdir(os.path.dirname(os.path.abspath(file_path)))))
    if len(etag) == 0:
        return None
    else:
        with open(f"{file_path}.etag", 'r') as f:
            return str(f.read())


def write_etag(file_path, etag):
    with open(f"{file_path}.etag", 'w') as f:
        f.write(etag)


def create_client(url, access_key, secret_key, proxy):
    proxy = create_proxy() if proxy is None else proxy
    return Minio(
        url,
        access_key=access_key,
        secret_key=secret_key,
        http_client=proxy
    ) if proxy is not None else Minio(
        url,
        access_key=access_key,
        secret_key=secret_key
    )


def create_proxy():
    proxy_env = os.getenv('http_proxy')
    if proxy_env is not None:
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
