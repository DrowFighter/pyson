import csv
import json

class Parser:
    def csv_to_json(self, csvFilePath, jsonFilePath):
        self.jsonArray = []
        
        #read csv file
        with open(csvFilePath, encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf) 

            #convert each csv row into python dict
            for row in csvReader: 
                #add this python dict to json array
                self.jsonArray.append(row)
    
        #convert python self.jsonArray to JSON String and write to file
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
            jsonString = json.dumps(self.jsonArray, indent=4)
            jsonf.write(jsonString)

    def __init__(self):

        with open("diamonds.csv", 'r') as input, open('temp.csv', 'w') as output:
            reader = csv.reader(input, delimiter = ',')
            writer = csv.writer(output, delimiter = ',')

            all = []
            row = next(reader)
            row.insert(0, 'ID')
            all.append(row)
            for k, row in enumerate(reader):
                all.append([str(k+1)] + row)
            writer.writerows(all)
        csvFilePath = r'temp.csv'
        jsonFilePath = r'diamonds.json'
        self.csv_to_json(csvFilePath, jsonFilePath)

