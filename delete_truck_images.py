import os
import subprocess

def delete_files_if_exceed_limit(directory, limit):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist. Ignoring operation.")
        return

    # Get the number of files in the directory
    num_files = len(os.listdir(directory))
    
    # Check if the number of files exceeds the limit
    if num_files > limit:
        print(f"Number of files in {directory} exceeds {limit}. Deleting files...")
        
        # Use the find command to delete files
        command = f"sudo find {directory} -mindepth 1 -delete"
        subprocess.run(command, shell=True)
        
        print("Files deleted successfully.")
    else:
        print(f"Number of files in {directory} is within the limit.")

if __name__ == "__main__":
    # Set the directory paths and the limit
    truck_cam_directory = "/tmp/truck_cam_images/"
    sec_cam_directory = "/tmp/sec_cam_images/"
    file_limit = 500
    
    # Delete files if the limit is exceeded
    delete_files_if_exceed_limit(truck_cam_directory, file_limit)
    delete_files_if_exceed_limit(sec_cam_directory, file_limit)

