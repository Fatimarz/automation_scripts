import os
files=[f for f in os.listdir() if f.endswith('.txt')]
print(files)


#checking if file exists
file_path='merged.txt'
if os.path.isfile(file_path):
    with open(file_path, 'r') as f:
        print(f.read())    
else:
    open(file_path, 'w').close()
    print('file created')

#merging files
with open(file_path, 'w') as f:
    for file in files:
        with open(file, 'r') as infile:
            f.write(infile.read() + '\n')



