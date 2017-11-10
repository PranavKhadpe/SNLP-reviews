# SNLP term project


## convert
Contains source files to separate real and fake reviews and convert them to csv files

### read_file.py 
Script to separate real and fake reviews in a simple, naive way.

Use it as 
```
python read_file.py folder_name file_name
```

where file_name is the name of the text file that contains the real and fake reviews
and folder_name is the name of the containing folder

The script will write two files, one containg real reviews, and another containing fake reviews in the folder specified.

### json_to_csv.py - 
Forked from vinay20045:master.
Usage: 	
```
python read_file.py <node_name> <input_text_file_name> <output_csv_file_name>
```

### ManyClassifiers.py -
Runs simple classifiers

### Observing_Dist.py
Tells you which were predicted correctly, off by 1,2 and 3

