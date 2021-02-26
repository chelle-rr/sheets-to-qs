import csv
import re
import os.path

# import your tsv data by substituting your filename in the below.
# (make sure it's in the same folder as this script.)
# this line reads the tsv as a dictionary, storing the top row as keys for the
# values in each subsequent row

tsv = (input("Enter the name of your .tsv file, excluding extension (must be in same folder as this script): ") + ".tsv")
thing = csv.DictReader(open(tsv), delimiter="\t",quoting=csv.QUOTE_NONE)

qid_re = re.compile('\A(Q[0-9]*)')
output = (input("Enter desired output filename: ") + ".tsv")

# this outputs a new tsv. the .items function provides each key-value pair
with open(output,'w') as csv_out:
	for entity in thing:
		csv_out.write('CREATE\n')
		for key,value in entity.items():
			qid_find = qid_re.findall(value)
			if qid_find and key != "P8":
				csv_out.write('LAST\t{}\t{}\n'.format(key,value))
			else:
				csv_out.write('LAST\t{}\t\"{}\"\n'.format(key,value))
