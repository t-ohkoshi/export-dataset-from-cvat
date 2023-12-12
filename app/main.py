import os
import sys
import subprocess
import shutil
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
TASK_IDS = os.getenv('TASK_IDS')

def check_login(cvat_cli_path, server_url, username, password):
    login_command = f"{cvat_cli_path} --auth {username}:\'{password}\' --server-host {server_url} ls"
    # check login
    subprocess.run(login_command, shell=True, check=True)

def dump_dataset(cvat_cli_path, server_url, username, password, task_id, include_img, format_name, output_file):
    # get dataset
    dump_command = f"{cvat_cli_path} --auth {username}:\'{password}\' --server-host {server_url} dump --format \"{format_name}\" --with-images {include_img} {task_id} {output_file}"
    subprocess.run(dump_command, shell=True, check=True)

def main():
    dl_path = os.path.join(os.getcwd(), "download")
    cvat_cli_path = shutil.which("cvat-cli")
    if cvat_cli_path is None:
        print("Error: cvat-cli is not installed", file=sys.stderr)
    print(cvat_cli_path)
    server_url = "https://app.cvat.ai/"
    format_name = "YOLO 1.1"

    # check login
    print("CVAT TASK IDs")
    check_login(cvat_cli_path, server_url, USER_NAME, PASSWORD)
    # remove blank
    target_task_ids = filtered_list = [item for item in TASK_IDS.split(',') if item != ""]

    for task_id in target_task_ids:
        print("DownLoad: " + task_id + " Dataset")
        try:
            file_path = task_id + "-dataset-yolo.zip"
            output_file = os.path.join(dl_path, file_path)
            #  get dataset
            dump_dataset(cvat_cli_path, server_url, USER_NAME, PASSWORD, task_id, False, format_name, output_file)
        except subprocess.CalledProcessError as e:
            print(f"RunTime Error: {e}", file=sys.stderr)

main()