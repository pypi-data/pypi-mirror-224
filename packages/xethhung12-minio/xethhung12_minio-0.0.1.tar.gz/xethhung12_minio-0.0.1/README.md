# Build and deploy
```shell
rm -fr dist/*
python -m build
python twine upload dist/* -u __token__ -p {token}
```

# Behind Proxy 
if the client is connecting to internet though a company proxy server, use the environment variable(`http_proxy`) to setup the proxy. \
e.g. `http_proxy=http://127.0.0.1:8080`


# Usage of upload
```python
python -m xethhung12_minio_upload_file \
    --url {url} \
    --access-key {access-key} \
    --secret-key {secret-key} \
    --bucket {bucket} \
    --local-file {local file} \
    --remote-file {remote file}
```

# Usage  of download
```python
python -m xethhung12_minio_download_file \
    --url {url} \
    --access-key {access-key} \
    --secret-key {secret-key} \
    --bucket {bucket} \
    --local-file {local file} \
    --remote-file {remote file}
```