
from pprint import pprint
import json
import hf_downloader.profiles
from datasets import load_dataset,list_datasets

datasets_list = list_datasets()
print("datasets_list:",datasets_list)
with open("../../download/datasets_all.json", "w") as json_file:
    json.dump(datasets_list, json_file)

