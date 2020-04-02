def snpRecordsFromCSV(csvSNPName):
    with open(csvSNPName, 'r') as recordsObj:
        dict_reader = DictReader(recordsObj)
        records = list(dict_reader)
        return records
