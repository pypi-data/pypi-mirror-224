from minio import Minio
import urllib3

def download(url, access_key, secret_key, bucket, remote, local, proxy=None):
    client = Minio(
        url,
        access_key=access_key,
        secret_key=secret_key,
    ) if proxy != None else Minio(
        url,
        access_key=access_key,
        secret_key=secret_key,
        http_client=urllib3.ProxyManager(proxy)
    )

    rs = client.fget_object(
        bucket,
        object_name=remote,
        file_path=local
    )

    return rs


