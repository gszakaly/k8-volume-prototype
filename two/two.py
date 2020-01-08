import os
import shutil
import time

INPUT_DIR = '/mnt/input'
OUTPUT_DIR = '/mnt/output'

container_name = os.environ['CONTAINER_NAME']

while True:
    for file_name in os.listdir(INPUT_DIR):
        input_file = os.path.join(INPUT_DIR, file_name)
        output_file = os.path.join(OUTPUT_DIR, file_name)
        
        with open(input_file, 'r') as fin:
            with open(output_file, 'w') as fout:
                fout.write(fin.read())
                fout.write(f'Processed {container_name}\n')
        
        os.remove(input_file)

        print(f'File {file_name} moved')

    time.sleep(1.)



