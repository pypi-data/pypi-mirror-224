from minio import Minio


def download(url, access_key, secret_key, bucket, remote, local):
    client = Minio(
        url,
        access_key=access_key,
        secret_key=secret_key
    )

    rs = client.fget_object(
        bucket,
        object_name=remote,
        file_path=local
    )

    return rs
