import csv
import re

tsv = (input("Enter the name of your .tsv file, excluding extension (must be in same folder as this script): ") + ".tsv")
thing = csv.DictReader(open(tsv), delimiter="\t", quoting=csv.QUOTE_NONE)

output = (input("Enter desired output filename: ") + ".tsv")

qid_re = re.compile('^(Q[0-9]*)$')
day_date_re = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
month_date_re = re.compile('^[0-9]{4}-[0-9]{2}$')
year_date_re = re.compile('^[1-2][0-9]{3}$')

with open(output,'w') as csv_out:
	for entity in thing:
		qid = entity["QID"]
		for key,value in entity.items():
			qid_find = qid_re.findall(value)
			day_date_find = day_date_re.findall(value)
			month_date_find = month_date_re.findall(value)
			year_date_find = year_date_re.findall(value)
			if value and key != "QID":
				if day_date_find:
					csv_out.write(qid)
					csv_out.write('\t{}\t+{}T00:00:00Z/11\n'.format(key,value))
				elif month_date_find:
					csv_out.write(qid)
					csv_out.write('\t{}\t+{}-00T00:00:00Z/10\n'.format(key,value))
				elif year_date_find:
					csv_out.write(qid)
					csv_out.write('\t{}\t+{}-00-00T00:00:00Z/09\n'.format(key,value))
				elif qid_find and key != "P8":
					csv_out.write(qid)
					csv_out.write('\t{}\t{}\n'.format(key,value))
				elif key == "P101":
					csv_out.write(qid)
					csv_out.write('\t{}\t{}\n'.format(key,value))
				elif key == "P82" and value:
					csv_out.write(qid)
					csv_out.write('\t{}\ten:\"{}\"\n'.format(key,value))
				elif value:
					csv_out.write(qid)
					csv_out.write('\t{}\t\"{}\"\n'.format(key,value))
