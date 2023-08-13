from xethhung12_minio_common import create_client, create_proxy, write_etag, check_is_latest


def download(url, access_key, secret_key, bucket, remote, local):
    client = create_client(url, access_key, secret_key, create_proxy())

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

