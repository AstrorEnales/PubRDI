from pub_data import PublicationDataFile

all_references = []
all_remedies = []
all_drugs = []
all_compounds = []
all_enzymes = []
all_transporter = []

for pmid in [12095536, 11180034, 17215845]:
    data_file = PublicationDataFile('../data/references/pmid_%s/data.json' % pmid)
    all_references.append(data_file.publication)
    for x in data_file.remedies:
        if x in all_remedies:
            all_remedies[all_remedies.index(x)].merge(x)
        else:
            all_remedies.append(x)
    for x in data_file.drugs:
        if x in all_drugs:
            all_drugs[all_drugs.index(x)].merge(x)
        else:
            all_drugs.append(x)
    for x in data_file.compounds:
        if x in all_compounds:
            all_compounds[all_compounds.index(x)].merge(x)
        else:
            all_compounds.append(x)
    for x in data_file.enzymes:
        if x in all_enzymes:
            all_enzymes[all_enzymes.index(x)].merge(x)
        else:
            all_enzymes.append(x)
    for x in data_file.transporter:
        if x in all_transporter:
            all_transporter[all_transporter.index(x)].merge(x)
        else:
            all_transporter.append(x)

print('References:')
for x in all_references:
    print('\t', x)
print('Remedies:')
for x in all_remedies:
    print('\t', x)
print('Drugs:')
for x in all_drugs:
    print('\t', x)
print('Compounds:')
for x in all_compounds:
    print('\t', x)
print('Enzymes:')
for x in all_enzymes:
    print('\t', x)
print('Transporter:')
for x in all_transporter:
    print('\t', x)
