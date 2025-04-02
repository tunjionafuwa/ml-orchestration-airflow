import os
import shutil
import argparse

import kagglehub


parser = argparse.ArgumentParser(
    prog="Kaggle dataset downloader",
    description="Download dastasets from kaggle",
    add_help=False,
)
parser.add_argument("dataset_name", help="name of kaggle dataset")
args = parser.parse_args()


def download_data_from_kaggle(dataset_name: str):
    download_path = kagglehub.dataset_download(dataset_name)

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    destination_path = ROOT_DIR + "/data/" + dataset_name

    try:
        os.makedirs(destination_path)
    except FileExistsError:
        pass

    for file_name in os.listdir(path=download_path):
        source = os.path.join(download_path, file_name)
        destination = os.path.join(destination_path, file_name)

        if not os.path.exists(destination):
            shutil.move(source, destination)

    shutil.rmtree(download_path.split(dataset_name)[0], ignore_errors=True)

    return destination_path


if __name__ == "__main__":
    _ = download_data_from_kaggle(dataset_name=args.dataset_name)
    print("download successful")
