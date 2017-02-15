import sys
file_to_read = sys.argv[1]

import csv
g = open(file_to_read,encoding="ISO-8859-15")
checklist = csv.reader(g)

checklist_sp=[]
checklist_fam=[]

for row in checklist:
    checklist_sp.append(row[5])
    checklist_fam.append(row[8])

checklist_dict={}
for i in range(len(checklist_sp)):
    checklist_dict[checklist_sp[i]]=checklist_fam[i]

#for i,j in checklist_dict.items():
#    print("Species " + i + " belongs to Family " + j)

count_species = {}
for k,v in checklist_dict.items():
    count_species[v]=len(k)

for k,v in count_species.items():
    print("There are " + str(v) + " total species in Family " + k)

g.close()
