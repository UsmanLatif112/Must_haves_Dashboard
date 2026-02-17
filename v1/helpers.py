from pathlib import Path


def delete_file_if_exists(file_path):
    try:
        path = Path(file_path)
        if path.is_file():
            path.unlink()
            print(f"The file {file_path} has been deleted.")
        else:
            print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")
