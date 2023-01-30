import csv
import json

class MyParser:

    def write_to_json_file(self):
        print('write_to_json_file')
        with open('diamonds.json', 'w', encoding='utf-8') as jsonf: 
            jsonString = json.dumps(self.jsonHash, indent=4)
            jsonf.write(jsonString)

    #TODO: understand how to update the file and not just rewrite it
    def update_to_json_file(self):
        print('update_to_json_file')


    def csv_to_json(self):
        #read csv file
        with open('temp.csv', encoding='utf-8') as csvf: 
            #load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf) 

            #convert each csv row into python dict
            for row in csvReader: 
                #add this python dict to json array
                self.jsonHash[row.get('ID')]=row
    
        #convert python self.jsonHash to JSON String and write to file
        self.write_to_json_file()

    def __init__(self):
        self.jsonHash = {}
        self.rowsNum = 0

        with open("diamonds.csv", 'r') as input, open('temp.csv', 'w') as output:
            reader = csv.reader(input, delimiter = ',')
            writer = csv.writer(output, delimiter = ',')

            tempArray = []
            row = next(reader)
            row.insert(0, 'ID')
            tempArray.append(row)
            for k, row in enumerate(reader):
                tempArray.append([str(k+1)] + row)

            self.rowsNum = len(tempArray) -1
            writer.writerows(tempArray)
        self.csv_to_json()

    def create(self,data):
        print('MyParser.create',data)
        self.rowsNum = self.rowsNum +1
        self.jsonHash[self.rowsNum] = data
        self.write_to_json_file()
        print('MyParser.create - new row id:',self.rowsNum)
        return str(self.rowsNum)
    
    def update(self,data):
        print('MyParser.update')
        rowId = data.get('ID')
        if(self.jsonHash.get(rowId) != None):
            self.jsonHash[rowId] = data
        self.write_to_json_file()
        return ""


    def getAll(self, data):
        print('MyParser.getAll')
        return self.jsonHash

    def getFirst10(self, data):
        print('MyParser.getFirst10')
        tempJson = {}
        for x in range(1,11):
            print(self.jsonHash.get(str(x)))
            tempJson[x] = self.jsonHash.get(str(x))
        return tempJson
    
    def delete(self, data):
        print('MyParser.delete')
        rowId = data.get('ID')
        print('rowId',rowId)
        print('self.jsonHash.get(rowId)',self.jsonHash.get(rowId))
        if(self.jsonHash.get(rowId) != None):
            del self.jsonHash[rowId]
        self.write_to_json_file()
        return ""

