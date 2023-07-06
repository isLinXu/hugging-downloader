import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import json
# import hf_downloader.profiles
from datasets import load_dataset, list_datasets


def get_hf_datasets_info(save_path="../../download/datasets_all.json", debug=True):
    datasets_list = list_datasets()
    print("datasets_list:", datasets_list)
    if os.path.exists(save_path) == False:
        os.makedirs(save_path)
    with open(save_path, "w") as json_file:
        json.dump(datasets_list, json_file)


if __name__ == '__main__':
    save_path = "/home/linxu/PycharmProjects/hugging-downloader/download/datasets_all.json"
    get_hf_datasets_info(save_path)
