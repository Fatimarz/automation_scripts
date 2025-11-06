import os 
import shutil
files=os.listdir()
for f in files:
    name, ext=os.path.splitext(f)
    if ext=='.bmp':
        new_name=f'{name}.bmp'
        os.rename(f,new_name)
        shutil.move(new_name, 'images/')           # moving into folders

    
    elif ext=='.docx':
        new_name=f'{name}.docx'
        os.rename(f,new_name)
        shutil.move(new_name, 'docs/')


    

