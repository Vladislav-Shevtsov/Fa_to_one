# Goal
The script combines fasta files of different loci located in different directories into one fasta file for each sample.

To achieve the distribution of locus files to folders that correspond to the name of the locus, please see the "move_to_folder" script https://github.com/Vladislav-Shevtsov/Sort-files-by-pattern


input files should be in .fasta format 

example : file.fasta	

To :

* folder_1_sample_1: 

       locus_1.fasta

       locus_2.fasta

       locus_3.fasta

       ........

       ........

       locus_n.fasta


* Folder_2_sample_2:

      locus_1.fasta

      locus_2.fasta

      locus_3.fasta

       ........

       ........

       locus_n.fasta

* Folder_3_sample_3: 

       locus_1.fasta

       locus_2.fasta

       locus_3.fasta

       ........

       ........

       locus__n.fasta

### output ### 
As a result, the script will generate following files:

Sample_1_all_loci_in_one_file.fasta

Sample_2_all_loci_in_one_file.fasta

Sample_3_all_loci_in_one_file.fasta

output represents files(reads) with .fasta extension located in output folder that you specify in code.    

### command line examples ###

```python3 Fa_to_one.py``` #This will generate bash file named "fa_to_one.sh"

```./fa_to_one.sh``` #This will execute the bash file 

#written by Shevtsov V.  xatabadich(at)gmail.com
