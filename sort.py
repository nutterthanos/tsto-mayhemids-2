import os
import shutil

def organize_files_by_app_id_prefix(directory, prefix_length=4):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            # Extract the applicationUserId from the filename
            try:
                app_user_id = filename.split("_")[1]
            except IndexError:
                continue  # Skip files that don't match the expected pattern
            
            # Take the prefix of applicationUserId
            prefix = app_user_id[:prefix_length]
            target_dir = os.path.join(directory, prefix)
            
            # Create the target directory if it doesn't exist
            os.makedirs(target_dir, exist_ok=True)
            
            # Move the file to the new directory
            shutil.move(os.path.join(directory, filename), os.path.join(target_dir, filename))
            print(f"Moved {filename} to {target_dir}")

# Usage example
organize_files_by_app_id_prefix(".")