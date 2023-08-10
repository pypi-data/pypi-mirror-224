# Build
```shell
rm -fr dist/*
python -m build
```

# Deploy
```shell
python twine upload dist/* -u __token__ -p {token}
```