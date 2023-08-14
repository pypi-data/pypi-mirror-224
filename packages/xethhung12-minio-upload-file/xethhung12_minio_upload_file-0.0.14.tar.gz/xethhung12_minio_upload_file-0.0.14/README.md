
# Build
```shell
rm -fr dist/*
python -m build
```

# Deploy
```shell
python twine upload dist/* -u __token__ -p {token}
```

# Usage 
```python
python -m xethhung12_minio_upload_file \
    --url {url} \
    --access-key {access-key} \
    --secret-key {secret-key} \
    --bucket {bucket} \
    --local-file {local file} \
    --remote-file {remote file}
```