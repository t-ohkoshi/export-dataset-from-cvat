# export-dataset-from-cvat

- this application is download cvat dataset over 1GB
  - https://github.com/opencv/cvat/issues/2330#issuecomment-895995983

## usage

### requirements

- use Pipenv (python 3.11) or Python with cvat-cli installed.
- use cvat account

### run application

#### setup

```
# clone this repository
git@github.com:t-ohkoshi/export-dataset-from-cvat.git

# move repostiory
cd export-dataset-from-cvat

# set cvat account + dataset
tee .env <<EOF
USER_NAME = "your cvat user name"
PASSWORD = "your cvat password"
TASK_IDS = "target task id"
EOF
```

#### use Pipenv

```
# setup application
pipenv install

# download cvat dataset
pipenv run python3 app/main.py
```

#### Python with cvat-cli installed

```
python3 app/main.py
```

#### options parametor

- [source code](./app/main.py#L18-L20)
    - default format: `YOLO 1.1`
    - include image : `True`

- [cvat-cli support format](https://github.com/opencv/cvat/tree/bb579e83cae6fac36cd4b65e29bade93b21be412/cvat/apps/dataset_manager/formats)
- [cvat-cli dump cmd](https://github.com/opencv/cvat/blob/bb579e83cae6fac36cd4b65e29bade93b21be412/site/content/en/docs/api_sdk/cli/_index.md?plain=1#L195)



```

