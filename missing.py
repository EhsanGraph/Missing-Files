import os

def get_files_in_folder(folder_path):
    """Get list of files in a folder"""
    return set(os.listdir(folder_path))

def find_missing_files(folder1, folder2):
    """Find missing files in folder2 compared to folder1"""
    files_in_folder1 = get_files_in_folder(folder1)
    files_in_folder2 = get_files_in_folder(folder2)

    missing_files = files_in_folder1 - files_in_folder2

    return missing_files

if __name__ == "__main__":
    folder1_path = input("Enter the path of the first folder: ").strip().rstrip("\\")
    folder2_path = input("Enter the path of the second folder: ").strip().rstrip("\\")
    
    print("Files in folder 1:", get_files_in_folder(folder1_path))
    print("Files in folder 2:", get_files_in_folder(folder2_path))

    missing_files = find_missing_files(folder1_path, folder2_path)

    if missing_files:
        print("Missing files in folder 2 compared to folder 1:")
        for file in missing_files:
            print(file)
    else:
        print("No missing files found.")
