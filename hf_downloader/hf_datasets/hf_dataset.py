import hf_downloader.profiles
from datasets import load_dataset_builder, load_dataset, get_dataset_split_names, get_dataset_config_names


def get_hf_datasets_info(datasets_name="rotten_tomatoes", debug=True):
    ds_builder = load_dataset_builder("rotten_tomatoes")

    ds_description = ds_builder.info.description

    ds_features = ds_builder.info.features
    if debug:
        print("ds_description:", ds_description)
        print("ds_features:", ds_features)
    return ds_description, ds_features

def load_hf_datasets(datasets_name="rotten_tomatoes", split="train", debug=True):
    ds = load_dataset("rotten_tomatoes", split="train")
    if debug:
        print("ds:", ds)
    return ds


if __name__ == '__main__':
    ds_name = 'rotten_tomatoes'
    get_hf_datasets_info(ds_name)
    dataset = load_dataset("rotten_tomatoes", split="train")
    print("dataset:", dataset)
