import os
import shutil
import kagglehub


def download_data_from_kaggle(dataset_name: str):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    source_path = kagglehub.dataset_download(dataset_name)
    destination_path = ROOT_DIR + "/data/" + dataset_name
    
    try:
        os.makedirs(destination_path)
    except FileExistsError:
        pass

    for file_name in os.listdir(path=source_path):
        source =  os.path.join(source_path, file_name)
        destination = os.path.join(destination_path, file_name)

        if os.path.exists(destination):
            print(f"Data exists at {destination}")
            continue
        else:
            shutil.move(source, destination)

    
    shutil.rmtree(source_path.split(dataset_name)[0], ignore_errors=True)

    return destination_path
    