import csv
import re

tsv = (input("Enter the name of your .tsv file, excluding extension (must be in same folder as this script): ") + ".tsv")
thing = csv.DictReader(open(tsv), delimiter="\t", quoting=csv.QUOTE_NONE)

qid_re = re.compile('\A(Q[0-9]*)')
output = (input("Enter desired output filename: ") + ".tsv")

day_date_re = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
month_date_re = re.compile('^[0-9]{4}-[0-9]{2}$')
year_date_re = re.compile('^[0-9]{4}$')

with open(output,'w') as csv_out:
	for entity in thing:
		csv_out.write('CREATE\n')
		for key,value in entity.items():
			qid_find = qid_re.findall(value)
			day_date_find = day_date_re.findall(value)
			month_date_find = month_date_re.findall(value)
			year_date_find = year_date_re.findall(value)
			if day_date_find:
				csv_out.write('LAST\t{}\t+{}T00:00:00Z/11\n'.format(key,value))
			elif month_date_find:
				csv_out.write('LAST\t{}\t+{}T00:00:00Z/10\n'.format(key,value))
			elif year_date_find:
				csv_out.write('LAST\t{}\t+{}T00:00:00Z/09\n'.format(key,value))
			elif qid_find and key != "P8":
				csv_out.write('LAST\t{}\t{}\n'.format(key,value))
			else:
				csv_out.write('LAST\t{}\t\"{}\"\n'.format(key,value))
