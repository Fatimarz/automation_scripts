import shutil, os, time
source= r"C:\Users\user\OneDrive\Desktop\automation_scripts\auto backup\file.txt"
backup_folder= r"C:\Users\user\OneDrive\Desktop\automation_scripts\auto backup\backup files"
last_modified=os.path.getmtime(source)

print(source)
while True:
    current_modified=os.path.getmtime(source)
    if current_modified!=last_modified:
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        backup_name=f'file_backup_{int(time.time())}.txt'
        shutil.copy(source, os.path.join(backup_folder, backup_name))
        print('file changed and backup created!')
        last_modified=current_modified
    time.sleep(2)