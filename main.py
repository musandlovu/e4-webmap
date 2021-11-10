import csv
with open("data/volcanoes.tsv", 'r') as fv:
    s = fv.read()
    my_sniffer = csv.Sniffer().sniff(s)
    fv.seek(0)
    my_reader = csv.DictReader(fv, dialect=my_sniffer)
    rows = []
    for row in my_reader:
        if "?" not in row["Type"] and "Unknown" not in row['Type'] and "Historical" not in row['Status'] and "Unnamed" not in row["Volcano Name"]:
            if 'Latitude' in row.keys() and 'Longitude' in row.keys():
                rows.append(row)