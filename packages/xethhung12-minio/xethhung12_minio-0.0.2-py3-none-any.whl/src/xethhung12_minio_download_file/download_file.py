from xethhung12_minio_common import create_client, write_etag, check_is_latest, create_proxy


def do_download(client, bucket, remote_file, local_file):
    rs = client.fget_object(
        bucket,
        object_name=remote_file,
        file_path=local_file
    )
    write_etag(local_file, rs.etag)
    print("Downloaded")


def download(url, access_key, secret_key, bucket, remote, local):
    client = create_client(url, access_key, secret_key, create_proxy())
    etag_local = check_is_latest(local)
    if etag_local is not None:
        f = client.get_object(bucket, object_name=remote)
        etag = str(f.headers['etag']).strip("\"")
        if etag_local == etag:
            print("The same no need to download")
        else:
            do_download(client, bucket, remote, local)
        return
    else:
        do_download(client, bucket, remote, local)
        return


