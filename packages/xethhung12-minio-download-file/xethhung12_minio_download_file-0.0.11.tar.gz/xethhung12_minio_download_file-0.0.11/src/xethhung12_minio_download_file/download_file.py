import os.path

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


def download(url, access_key, secret_key, bucket, remote, local):
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

    def do_download(remote_file, local_file):
        rs = client.fget_object(
            bucket,
            object_name=remote_file,
            file_path=local_file
        )
        write_etag(local_file, rs.etag)
        print("Downloaded")

    etag_local = check_is_latest(local)
    if etag_local is not None:
        f = client.get_object(bucket, object_name=remote)
        etag = str(f.headers['etag']).strip("\"")
        if etag_local == etag:
            print("The same no need to download")
        else:
            do_download(remote, local)
        return
    else:
        do_download(remote, local)
        return


def write_etag(file_path, etag):
    with open(f"{file_path}.etag", 'w') as f:
        f.write(etag)


def check_is_latest(file_path):
    etag = list(filter(lambda x: x == f"{file_path}.etag", os.listdir(os.path.dirname(os.path.abspath(file_path)))))
    if len(etag) == 0:
        return None
    else:
        with open(f"{file_path}.etag", 'r') as f:
            return str(f.read())
