import sys
import os

def show_current_path(currnet_path):
    print(currnet_path)


def main():
    # pu.db
    currnet_path = os.getcwd()
    show_current_path(currnet_path)

main()