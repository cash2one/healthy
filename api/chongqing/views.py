#-*- coding: UTF-8 -*-
import uuid
import time
import datetime
import json
import base64
import xmltodict
from collections import OrderedDict
from serializers import TbdiabetesflupSeri, TbhypertensionflupSeri,TbhypertensionspecialSeri,TbdiabetesSpecialSeri, TbareaSeri, TbmedicalorganizationSeri, TbUserSeri, TbhealthrecordSeri, TbhealexaminationSeri, YTJMeasureSeri
from website.models import Tbdiabetesflup, Tbhypertensionflup,Tbhypertensionspecial,TbdiabetesSpecial, Tbarea, Tbmedicalorganization, UserProfile, Tbhealthrecord, Tbhealexamination
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from parsers import XMLParser
from renderers import XMLRenderer
from xml.dom import minidom
from xml.dom.minidom import Document
from pysimplesoap.server import SoapDispatcher

# Handle XML.
def getAttributeFromXML(xml, name):
    doc = minidom.parseString(xml)
    root = doc.documentElement
    if len(root.getElementsByTagName(name)) != 0:
        value = root.getElementsByTagName(name)[0].firstChild.data
        return value
    else:
        return ''

def delNodeFromXML(xml, fatherName, nodeName):
#     doc = minidom.parseString(xml)
#     root = doc.documentElement
#     fatherNode = root.getElementsByTagName(fatherName)[0]
#     for subnode in fatherNode.childNodes:
#         if subnode.nodeType == fatherNode.ELEMENT_NODE and subnode.tagName == nodeName:
#             fatherNode.removeChild(subnode)
#             break
#     return doc.toxml("UTF-8")
    doc = minidom.parseString(xml)
    root = doc.documentElement
    for fatherNode in root.getElementsByTagName(fatherName):
        for subnode in fatherNode.childNodes:
            if subnode.nodeType == fatherNode.ELEMENT_NODE and subnode.tagName == nodeName:
                fatherNode.removeChild(subnode)
                break
    return doc.toxml("UTF-8")

def addNodeToXML(xml, fatherName, nodeName, nodeValue):
    data = delNodeFromXML(xml, fatherName, nodeName)
    doc = minidom.parseString(data)
    root = doc.documentElement
    newNode = doc.createElement(nodeName)
    newTextNode = doc.createTextNode(nodeValue)
    newNode.appendChild(newTextNode)
    root.getElementsByTagName(fatherName)[0].appendChild(newNode)
    return root.toxml("UTF-8")

def addReponseHeader(content, requestMId, requestTime, actionType):
    doc = Document()
    rootNode = doc.createElement("response-message")
    doc.appendChild(rootNode)
    resMidNode = doc.createElement("responseMessageId")
    rootNode.appendChild(resMidNode)
    resMidValue = doc.createTextNode(str(uuid.uuid1()))
    resMidNode.appendChild(resMidValue)
    reqMidNode = doc.createElement("requestMessageId")
    rootNode.appendChild(reqMidNode)
    reqMidValue = doc.createTextNode(str(requestMId))
    reqMidNode.appendChild(reqMidValue)
    resMtimeNode = doc.createElement("responseTime")
    rootNode.appendChild(resMtimeNode)
    ISOTIMEFORMAT='%Y-%m-%d %X'
    resMtimeValue = doc.createTextNode(time.strftime(ISOTIMEFORMAT, time.localtime()))
    resMtimeNode.appendChild(resMtimeValue)
    reqMtimeNode = doc.createElement("requestTime")
    rootNode.appendChild(reqMtimeNode)
    reqMtimeValue = doc.createTextNode(str(requestTime))
    reqMtimeNode.appendChild(reqMtimeValue)
    actionTypeNode = doc.createElement("actionType")
    rootNode.appendChild(actionTypeNode)
    actionTypeValue = doc.createTextNode(str(actionType))
    actionTypeNode.appendChild(actionTypeValue)
    if content != '':
        contentNode = doc.createElement("content")
        rootNode.appendChild(contentNode)
        contentValue = doc.createCDATASection(content)
        contentNode.appendChild(contentValue)
    reqStatus = doc.createElement("status")
    rootNode.appendChild(reqStatus)
    reqStatusValue = doc.createTextNode("0")
    reqStatus.appendChild(reqStatusValue)
    reqStatusDescNode = doc.createElement("statusDescription")
    rootNode.appendChild(reqStatusDescNode)
    reqStatusDescValue = doc.createTextNode("ok")
    reqStatusDescNode.appendChild(reqStatusDescValue)
    return doc.toxml()

def setXMLSize(content, cnt):
    doc = minidom.parseString(content)
    root = doc.documentElement
    root.setAttribute("total", str(cnt))
    root.setAttribute("start", "1")
    root.setAttribute("returnSize", str(cnt))
    return doc.toprettyxml(indent = "", newl = "", encoding = "utf-8")

# Handle SOAP.
def jobDispatch(arg0):
    doc = minidom.parseString(arg0)
    root = doc.documentElement
    actionType = root.getElementsByTagName('actionType')
    actionTypeValue = actionType[0].childNodes[0].nodeValue
    requestContent = root.getElementsByTagName('content')
    xmlData = base64.decodestring(requestContent[0].childNodes[0].nodeValue)
    print "\n****API Receive: Command is %s****" % actionTypeValue
    print xmlData
    print "*****************************\n"
    if (actionTypeValue == 'G0301000101'):   # 一体机注册
        content = machineRegisterViewSet()
    elif (actionTypeValue == 'M0000010101'): # 行政区域查询
        content = areaViewGet(xmlData)
    elif (actionTypeValue == 'M0000010102'): # 医疗机构查询
        content = medicalorganizationViewGet(xmlData)
    elif (actionTypeValue == 'M0000010103'): # 用户列表查询
        content = userViewGet(xmlData)
    elif (actionTypeValue == 'M0100020101'): # 健康档案查询
        content = healthRecordViewGet(xmlData)
    elif (actionTypeValue == 'M0100020201'): # 健康档案新增
        content = healthRecordViewCreate(xmlData)
    elif (actionTypeValue == 'M0100020202'): # 健康档案修改
        content = healthRecordViewUpdate(xmlData)
    elif (actionTypeValue == 'M0100030101'): # 体检管理查询
        content = healexaminationViewGet(xmlData)
    elif (actionTypeValue == 'M0100030201'): # 体检管理上传
        content = healexaminationViewSet(xmlData)
    elif (actionTypeValue == 'M0100080201'): # 体检测量上传
        content = healthMeasureViewSet(xmlData)
    elif (actionTypeValue == 'M0100070101'): # 糖尿病专项查询
        content = diabetesSpecialViewGet(xmlData)
    elif (actionTypeValue == 'M0100070102'): # 糖尿病随访记录查询
        content = diabetesFlupViewGet(xmlData)
    elif (actionTypeValue == 'M0100070201'): # 糖尿病随访记录新增
        content = diabetesFlupViewSet(xmlData)
    elif (actionTypeValue == 'M0100060101'): # 高血压专项查询
        content = hypertensionSpecialViewGet(xmlData)
    elif (actionTypeValue == 'M0100060102'): # 高血压随访记录查询
        content = hypertensionFlupViewGet(xmlData)
    elif (actionTypeValue == 'M0100060202'): # 高血压随访记录新增
        content = hypertensionFlupViewSet(xmlData)
    else:
        content = ''
    requestMId = root.getElementsByTagName('requestMessageId')[0].childNodes[0].nodeValue
    requestTime = root.getElementsByTagName('requestTime')[0].childNodes[0].nodeValue
    print "\n****API Response: Command is %s****" % actionTypeValue
    #print content
    #print "*****************************\n"
    return addReponseHeader(base64.encodestring(content), requestMId, requestTime, actionTypeValue)

dispatcher = SoapDispatcher(
    'PlatformService',
    location = "http://localhost:8000/api/PlatformService.wsdl",
    action = "http://localhost:8000/api/PlatformService.wsdl",
    namespace = "http://localhost:8000/api/PlatformService.wsdl",
    prefix = "ns0",
    ns = "bl2")

# Register function.
dispatcher.register_function('send', jobDispatch,
    returns={'sendResponse': str},
    args={'arg0': str})

@csrf_exempt # not using CSRF protection.
def dispatcher_handler(request):
    if request.method == "POST":  # return function result.
        response = HttpResponse(dispatcher.dispatch(request.body))
    else: # return WSDL file.
        response = HttpResponse(dispatcher.wsdl())
        response['Content-length'] = str(len(response.content))
    return response

# Test without SOAP.
class TestView(APIView):
    renderer_classes = (XMLRenderer,)
    def get(self, request):
        return Response(healthRecordViewGet())

# Register related functions.
def areaViewGet(xmlData):
    areaCode = getAttributeFromXML(xmlData, "areaCode")
    data = Tbarea.objects.filter(areaCode__startswith=areaCode)
    if len(data) == 0:
        print "**API ERROR(areaViewGet): No records with areaCode=%s in DB." % areaCode
        return ''
    dataSeri = TbareaSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["area"]}
    content = renderer.get_xml(dataSeri.data, item_name)
    return setXMLSize(content, len(data))

def medicalorganizationViewGet(xmlData):
    print xmlData
    # orgCode = getAttributeFromXML(xmlData, "orgCode")
    data = Tbmedicalorganization.objects.all() # return all organizations
    if len(data) == 0:
        print "**API ERROR(medicalorganizationViewGet): No records DB."
        return ''
    dataSeri = TbmedicalorganizationSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["org"]}
    content = renderer.get_xml(dataSeri.data, item_name)
    return setXMLSize(content, len(data))

def userViewGet(xmlData):
    orgCode = getAttributeFromXML(xmlData, "orgCode")
    orgObj = Tbmedicalorganization.objects.filter(orgCode=orgCode)
    data = UserProfile.objects.filter(orgCode=orgObj, type=1) # Only get doctor here.
    if len(data) == 0:
        print "**API ERROR(userViewGet): No records with orgCode=%s in DB." % orgCode
        return ''
    dataSeri = TbUserSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["user"]}
    content = renderer.get_xml(dataSeri.data, item_name)
    return setXMLSize(content, len(data))

def machineRegisterViewSet():
    return ''

# Health record related functions.
def healthRecordViewGet(xmlData):
    # use area code to get data
    # householdRegisterCode = getAttributeFromXML(xmlData, "householdRegisterCode")
    # area = Tbarea.objects.filter(areaCode=householdRegisterCode)
    # data = Tbhealthrecord.objects.filter(householdRegisterCode=area)

    # use doctor id to get data
    responsibleDoctorCode = getAttributeFromXML(xmlData, "responsibleDoctorCode")
    print '++++======================R'
    print(responsibleDoctorCode)
    doctor = UserProfile.objects.filter(id=(int)(responsibleDoctorCode))
    data = Tbhealthrecord.objects.filter(responsibleDoctorCode=doctor)
    dataSeri = TbhealthrecordSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["healthRecord"], 1:["pastHistory"]}
    content = renderer.get_xml(dataSeri.data, item_name)
    res = delNodeFromXML(content, "healthRecord", "machineCode")
    res = delNodeFromXML(res, "healthRecord", "machineNo")
    print res
    return setXMLSize(res, len(data))

def healthRecordViewCreate(xmlData):
    xmlData = addNodeToXML(xmlData, "healthRecord", "birthday", "1996-07-08")
    
    xmlData = delNodeFromXML(xmlData, "healthRecord", "personId") # default: 12
    healthFileNum = str(int(time.time()))+str(datetime.datetime.now().microsecond) # default: random
    xmlData = addNodeToXML(xmlData, "healthRecord", "healthFileNumber", healthFileNum)
    machineNo = getAttributeFromXML(xmlData, "machineNo")
    name = getAttributeFromXML(xmlData, "name")
    idCard = getAttributeFromXML(xmlData, "idCard")
       
    try:
        nowLiveCode = getAttributeFromXML(xmlData, "nowLiveCode")
    except :
        print "Can not get nowLiveCode in nowLiveCode"
        xmlData = addNodeToXML(xmlData, "healthRecord", "nowLiveCode", "5")
    else:
        if len(nowLiveCode) == 0:
            xmlData = addNodeToXML(xmlData, "healthRecord", "nowLiveCode", "5")
    
    
    parser = XMLParser()
    item_name = {0:["healthRecord"], 1:["pastHistory"]}
    seriData = parser.get_seri(xmlData, item_name)
    print '**API: Create a new record.'
    dataSeri = TbhealthrecordSeri(data=seriData, many=True, context=seriData)
    if dataSeri.is_valid():
        dataSeri.save()   
             
        doc = Document()

        baseNode = doc.createElement("responseDatas")
        doc.appendChild(baseNode)
        
        rootNode = doc.createElement("healthRecord")
        baseNode.appendChild(rootNode)
        
        nodeName = doc.createElement("personId")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode(healthFileNum)
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("machineNo")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode(machineNo)
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("name")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode(name)
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("recordResultCode")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode("0")
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("recordResultDesc")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode("身份证号码["+ idCard +"] 已经建档！")
        nodeName.appendChild(nodeVal)
                        
        data = doc.toprettyxml(indent = "", newl = "", encoding = "utf-8")

        print data
        return data
    else:
        print "**API ERROR(healthRecordViewCreate): Data is not valid."
        return ''

def healthRecordViewUpdate(xmlData):
    parser = XMLParser()
    item_name = {0:["healthRecord"], 1:["pastHistory"]}
    seriData = parser.get_seri(xmlData, item_name)
    
    healthFileNumber = getAttributeFromXML(xmlData, "healthFileNumber")
    record = Tbhealthrecord.objects.filter(healthFileNumber=str(healthFileNumber))
    
    if len(record) == 0:
        print '**API: No such record.'
        return ''
    print '**API: Update exist record.'
    dataSeri = TbhealthrecordSeri(record, data=seriData, many=True, context=seriData)
    if dataSeri.is_valid():
        dataSeri.save()
    else:
        print "**API ERROR(healthRecordViewSet): Data is not valid."
    return ''

# Examination related functions.
def healexaminationViewGet(xmlData):
    healthFileNumber = getAttributeFromXML(xmlData, "healthFileNumber")
    data = Tbhealexamination.objects.filter(healthFileNumber=healthFileNumber)
    dataSeri = TbhealexaminationSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["healthExamination"], 1:["hospitalized", "familyBed", "medication", "vaccination"]}
    content = renderer.get_xml(dataSeri.data, item_name)
    
    res = delNodeFromXML(content, "healthExamination", "machineCode")
    res = delNodeFromXML(res, "healthExamination", "machineNo")

    return setXMLSize(res, len(data))

def healexaminationViewSet(xmlData):
    # healthFileNumber = getAttributeFromXML(xmlData, "healthFileNumber")

    xmlData = delNodeFromXML(xmlData, "healthExamination", "personId") # default: 12
    healthFileNum = getAttributeFromXML(xmlData, "healthFileNumber")
    machineNo = getAttributeFromXML(xmlData, "machineNo")
    name = getAttributeFromXML(xmlData, "name")
   
    parser = XMLParser()
    item_name = {0:["healthExamination"]}
    seriData = parser.get_seri(xmlData, item_name)
    print '**API: Create a new record.'
    dataSeri = TbhealexaminationSeri(data=seriData, many=True, context=seriData)
    print dataSeri

    if dataSeri.is_valid():
        dataSeri.save()
        doc = Document()
        baseNode = doc.createElement("responseDatas")
        doc.appendChild(baseNode)
        rootNode = doc.createElement("healthExamination")
        baseNode.appendChild(rootNode)
        
        nodeName = doc.createElement("businesskey")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode(machineNo)
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("personId")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode(healthFileNum)
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("machineNo")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode(machineNo)
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("name")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode(name)
        
        nodeName.appendChild(nodeVal)
        nodeName = doc.createElement("recordResultCode")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode("0")
        nodeName.appendChild(nodeVal)
        
        nodeName = doc.createElement("recordResultDesc")
        rootNode.appendChild(nodeName)
        nodeVal = doc.createTextNode("操作成功")
        nodeName.appendChild(nodeVal)
        
        data = doc.toprettyxml(indent = "", newl = "", encoding = "utf-8")
        print data
        return data
    else:
        print "**API ERROR(healexaminationViewSet): Data is not valid."
        return ''

# Health measure functions.
def healthMeasureGetDataField(xmlData):
#     doc = minidom.parseString(xmlData)
#     root = doc.documentElement
#     newNode = doc.createElement("test")
#     newTextNode = doc.createTextNode("haha")
#     newNode.appendChild(newTextNode)
#     root.getElementsByTagName("jkcl")[0].appendChild(newNode)
#     xmlData = root.toxml("UTF-8")
    
    data = delNodeFromXML(xmlData, "jkcl", "responsibleDoctorCode")
    data = delNodeFromXML(data, "jkcl", "idCard")
    data = delNodeFromXML(data, "jkcl", "time")
    data = delNodeFromXML(data, "jkcl", "personId")
    data = delNodeFromXML(data, "jkcl", "name")
    doc = minidom.parseString(data)

    root = doc.documentElement
    nodes = root.getElementsByTagName("jkcl")[0]
    # xmlStr = ""
    # for node in nodes.childNodes:
    #     xmlStr = xmlStr + node.toxml()
    # print xmlStr
    convertedDict = xmltodict.parse(nodes.toxml())
    jsonStr = json.dumps(convertedDict["jkcl"])
    return jsonStr

def healthMeasureViewSet(xmlData):
#     data = YTJMeasure.objects.filter(ID=1)
#     dataSeri = YTJMeasureSeri(data, many=True)
#     print dataSeri.data
    
    parser = XMLParser()
    item_name = {0:["jkcl"]}
    jsonData = healthMeasureGetDataField(xmlData)
    jsonData = json.loads(jsonData)
    seriData = parser.get_seri(xmlData, item_name)
    newSeriData = [OrderedDict(list(seriData[0].items()) + list(OrderedDict([("data",jsonData)]).items()))]
    print '**API: Create a new record.'
    dataSeri = YTJMeasureSeri(data=newSeriData, many=True, context=seriData)
    if dataSeri.is_valid():
        dataSeri.save()
    else:
        print "**API ERROR(healexaminationViewSet): Data is not valid."
    return ''

def diabetesSpecialViewGet(xmlData): #糖尿病专项查询
    print("11111111111111")
    specialNo = getAttributeFromXML(xmlData, "specialNo")
    print(specialNo)
    data = TbdiabetesSpecial.objects.filter(specialNo=specialNo)
    print("xxxxxxxxxxxxxxx5")

    dataSeri = TbdiabetesSpecialSeri(data, many=True)
    print("xxxxxxxxxxxxxxx4")

    renderer = XMLRenderer()
    print("xxxxxxxxxxxxxxx3")

    item_name = {0:["diabetesSpecial"]}
    print("xxxxxxxxxxxxxxx2")

    content = renderer.get_xml(dataSeri.data, item_name)
    print(content)
    print("xxxxxxxxxxxxxxx1")
    return setXMLSize(content, len(data))

def diabetesSpecialViewSet(xmlData): #糖尿病专项新增
    parser = XMLParser()
    item_name = {0:["diabetesSpecial"]}
    seriData = parser.get_seri(xmlData, item_name)
    print '**API: Create a new record.'
    dataSeri = TbdiabetesSpecialSeri(data=seriData, many=True, context=seriData)
    print dataSeri
    if dataSeri.is_valid():
        dataSeri.save()
    else:
        print "**API ERROR(diabetesSpecialViewSet): Data is not valid."
    return ''

def hypertensionSpecialViewGet(xmlData):
    specialNo = getAttributeFromXML(xmlData, "specialNo")
    print(specialNo)
    data = Tbhypertensionspecial.objects.filter(specialNo=specialNo)
    dataSeri = TbhypertensionspecialSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["hypertensionSpecial"]}
    print("xxxxxxxxxxxxxxx2")
    content = renderer.get_xml(dataSeri.data, item_name)
    print(content)
    print("xxxxxxxxxxxxxxx1")
    res = delNodeFromXML(content, "hypertensionSpecial", "householdRegisterCode")
    res = delNodeFromXML(res, "hypertensionSpecial", "responsibleDoctorCode")
    res = delNodeFromXML(res, "hypertensionSpecial", "organization")
    res = delNodeFromXML(res, "hypertensionSpecial", "mechineCode")
    res = delNodeFromXML(res, "hypertensionSpecial", "mechineNo")
    res = delNodeFromXML(res, "hypertensionSpecial", "genderCode")
    print res
    return setXMLSize(res, len(data))

def hypertensionSpecialViewSet(xmlData):
    parser = XMLParser()
    item_name = {0:["hypertensionSpecial"]}
    seriData = parser.get_seri(xmlData, item_name)
    print seriData
    print '**API: Create a new record.'
    dataSeri = TbhypertensionspecialSeri(data=seriData, many=True, context=seriData)
    print dataSeri
    if dataSeri.is_valid():
        dataSeri.save()
    else:
        print "**API ERROR(hypertensionSpecial): Data is not valid."
    return ''

def hypertensionFlupViewGet(xmlData):
    specialNo = getAttributeFromXML(xmlData, "specialNo")
    print(specialNo)
    data = Tbhypertensionflup.objects.filter(specialNo=specialNo)
    dataSeri = TbhypertensionflupSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["hypertensionFlup"]}
    print("xxxxxxxxxxxxxxx2")
    content = renderer.get_xml(dataSeri.data, item_name)
    print(content)
    print("xxxxxxxxxxxxxxx1")
#     content = delNodeFromXML(content, "hypertensionFlup", "specialNo")
    content = delNodeFromXML(content, "hypertensionFlup", "healthFileNumber")

    print content
    return setXMLSize(content, len(data))

def hypertensionFlupViewSet(xmlData): #高血压随访新增
    parser = XMLParser()
    specialNo = getAttributeFromXML(xmlData, "specialNo")
    item_name = {0:["hypertensionFlup"]}
    xmlData = addNodeToXML(xmlData, "hypertensionFlup", "businessKey", str(uuid.uuid1()))    
    xmlData = addNodeToXML(xmlData, "hypertensionFlup", "healthFileNumber", specialNo)    

    xmlData = delNodeFromXML(xmlData, "hypertensionFlup", "personId")

    print(xmlData)
    seriData = parser.get_seri(xmlData, item_name)
    print seriData
    print '**API: Create a new record. 11111'

    dataSeri = TbhypertensionflupSeri(data=seriData, many=True, context=seriData)
    print dataSeri
    if dataSeri.is_valid():
        print "AAAAAAAAAAAAAAAA"
        dataSeri.save()
        print "AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBB"
    else:
        print "**API ERROR(hypertensionFlup): Data is not valid."
    return ''

def diabetesFlupViewGet(xmlData): #糖尿病随访查询（M0100070102）
    specialNo = getAttributeFromXML(xmlData, "specialNo")
    print(specialNo)
    data = Tbdiabetesflup.objects.filter(specialNo=specialNo)
    dataSeri = TbdiabetesflupSeri(data, many=True)
    renderer = XMLRenderer()
    item_name = {0:["diabetesFlup"]}
    print("xxxxxxxxxxxxxxx2")
    content = renderer.get_xml(dataSeri.data, item_name)
    print("xxxxxxxxxxxxxxx1")
    return setXMLSize(content, len(data))


def diabetesFlupViewSet(xmlData): #糖尿病随访新增 M0100070201
    print "In dbFVS **********************"
    parser = XMLParser()
#     specialNo = getAttributeFromXML(xmlData, "specialNo")
#     print specialNo
    item_name = {0:["diabetesFlup"]}
#     xmlData = addNodeToXML(xmlData, "hypertensionFlup", "businessKey", str(uuid.uuid1()))    
#     xmlData = addNodeToXML(xmlData, "hypertensionFlup", "healthFileNumber", specialNo)
#     xmlData = delNodeFromXML(xmlData, "hypertensionFlup", "personId")

    print(xmlData)
    seriData = parser.get_seri(xmlData, item_name)
    print seriData
    print '**API: Create a new record. 11111'

    dataSeri = TbdiabetesflupSeri(data=seriData, many=True, context=seriData)
    print dataSeri
    if dataSeri.is_valid():
        print "AAAAAAAAAAAAAAAACCCCCCCCCCCCCCCC"
        dataSeri.save()
        print "AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBB"
    else:
        print "**API ERROR(hypertensionFlup): Data is not valid."
    return ''
