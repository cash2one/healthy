#-*- coding: UTF-8 -*-
import json
from collections import OrderedDict

class ConvertProtocol():
    commonFieldDict = {"time":"measureTime", "machineCode":"mdevice"}
    jsonFieldDict = {"xy":"spo2", "ml":"heartRate"}
    jsonFieldName = "data"
    
    def convertJsonFields(self, inData):
        data = inData
        for key, value in self.jsonFieldDict.items():
            data = data.replace(value, key)
        return data
    
    def convertCommonFields(self, inData):
        record = inData
        retObject = OrderedDict()
        for key, value in self.commonFieldDict.items():
            retObject[key] = record.pop(value)
        retObject["name"] = "liuhaodong"
        retObject["idCard"] = "1234567"
        retObject[self.jsonFieldName] = json.loads(json.dumps(record))
        return retObject

    def convert(self, jsonData):
        newData = []
        records = json.loads(self.convertJsonFields(jsonData))

        for record in records:
            newData.append(self.convertCommonFields(record))

        return newData
    
    
    