# export-dataset-from-cvat

- this application is download cvat dataset over 1GB
  - https://github.com/opencv/cvat/issues/2330#issuecomment-895995983

## usage

### requirements

- use Pipenv
- use python 3.11
- use cvat account

### run application

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

# setup application
pipenv install

# download cvat dataset
pipenv run python3 app/main.py
```



