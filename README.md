# Fa_to_one
Combine Fasta files located in different directories into one file 

input files should be in .fasta format 

example : file.fasta	

Real life scenario:

folder_1: 

file1.fasta

file2.fasta

file3.fasta

........

........

file_n.fasta


Folder_2:

file1.fasta

file2.fasta

file3.fasta

........

........

file_n.fasta

Folder_3: 

file1.fasta

file2.fasta

file3.fasta

........

........

file_n.fasta

### output ### 
The result is following:

Folder1.allinone.fasta

Folder2.allinone.fasta

Folder3.allinone.fasta

output represents files(reads) with .fasta extension located in output folder that you specify in code.    

### command line examples ###

python3 Fa_to_one.py #This will generate bash file#

bash fa_to_one.sh which can be run using ./bash fa_to_one.sh command	

#written by V.Shevtsov xatabadich(at)gmail.com
