import os

def get_all_filenames_in_path(path):
    filenames = []
    try:
        files_and_dirs = os.listdir(path)
        for item in files_and_dirs:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                filenames.append(item)
        return filenames

    except OSError as e:
        print(f"Error: {e}")
        return None
    
path = "assets"
filenames = get_all_filenames_in_path(path)

if filenames:
    print("Filenames in the directory:")
    with open("names.txt", "w") as f:
        for filename in filenames:
            f.write(f'<img src="../SpaceCoder96/assets/{filename}">\n')
else:
    print("Failed to retrieve filenames.")