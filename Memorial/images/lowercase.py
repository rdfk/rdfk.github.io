import os

def lowercase_filenames_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            lowercase_name = filename.lower()
            original_path = os.path.join(folder_path, filename)
            lowercase_path = os.path.join(folder_path, lowercase_name)

            # Only rename if the new name is different
            if filename != lowercase_name:
                os.rename(original_path, lowercase_path)
                print(f"Renamed: {filename} → {lowercase_name}")
        print("\n✅ Done. All filenames converted to lowercase.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
folder = input("Enter the path to the folder (e.g. G:\\Coding Etc\\Memorial\\images):\n")
lowercase_filenames_in_folder(folder)
