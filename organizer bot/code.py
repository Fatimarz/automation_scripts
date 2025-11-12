import os, shutil

# setting the source and destination folder
source_folder = r"C:\Users\user\Downloads"
dest_folders = r"C:\Users\user\Downloads\organized"

# creating folder if not exist
if not os.path.exists(dest_folders):
    os.makedirs(dest_folders)

# defining file types inside sub folder
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.docx', '.txt', '.pdf', '.xlsx']
}

# helper function to move safely (renames duplicates)
def move_file_safely(src, dest_folder):
    file_name = os.path.basename(src)
    dest_path = os.path.join(dest_folder, file_name)
    base, ext = os.path.splitext(file_name)
    counter = 1

    # if same file exists, rename new one
    while os.path.exists(dest_path):
        new_name = f"{base}_{counter}{ext}"
        dest_path = os.path.join(dest_folder, new_name)
        counter += 1

    shutil.move(src, dest_path)

# searching and moving file in relevant folders
for file in os.listdir(source_folder):  # list all files
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):  # make sure it's just a file
        _, ext = os.path.splitext(file)
        moved = False

        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                folder_path = os.path.join(dest_folders, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                move_file_safely(file_path, folder_path)
                moved = True
                break

        # if not matched to any category, move to 'others'
        if not moved:
            other_path = os.path.join(dest_folders, 'others')
            os.makedirs(other_path, exist_ok=True)
            move_file_safely(file_path, other_path)
