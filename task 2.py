import os
import shutil

def organize_files(directory):
    # Mapping of file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        # Add more types as needed
    }

    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to respective folders
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(os.path.join(directory, filename), os.path.join(directory, folder, filename))
                moved = True
                break

        if not moved:
            # If the file type is not recognized, move to 'Others' folder
            other_folder = os.path.join(directory, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(os.path.join(directory, filename), os.path.join(other_folder, filename))

    print("Files organized successfully.")

# Specify the directory to organize
directory_to_organize = 'C:/Users/Akhlaq computer/Videos/Captures'
organize_files(directory_to_organize)