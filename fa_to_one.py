import os
import sys 

dir = sys.argv[1]
out_dir = sys.argv[2]
allfiles = os.listdir(dir)
fa_list = [os.path.join(dir, i) for i in os.listdir(dir) if i.endswith('.fasta')]
def generate_name(name, suffix = 'allinone'): 
    a, b = os.path.splitext(name)
    new_name = a + '_'+ suffix + b
    return new_name

bash_file = 'fa_to_one.sh' #The name of bash file can be changed 
with open(bash_file, 'w') as f:
    f.write('#!/bin/bash \n')
    for folder in allfiles:
        name = os.path.basename(folder)
        out_sample = os.path.join(out_dir, name)
        out_sample = generate_name(out_sample)
        print(folder, name, out_sample)
        if not os.path.isfile(out_sample):
            f.write(f'cat {folder}/*.fasta >> {out_sample} \n')
            print(out_sample)
