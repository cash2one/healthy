#-*- coding: utf-8 -*-
'''
Created on 2016年1月20日

@author: LHD
'''
from django.db.models import Q
from models import *
from DIC import *
from website.models import Tbdiabetesflup
from django.db.models.query import QuerySet
from django.db.models import Count
#===============================================================================
# #读取一个既往病例史   参数为记录的ID
#===============================================================================
def history_read(id):
    try:
        record=Tbhealthrecord.objects.get(ID__exact=id)
        past_history=record.pastHistoryList.all()
        print len(past_history)
        List=[]
        for each in past_history:
            dic={}
            dic['pastHistoryType']=each.pastHistoryType#既往病类型
            if each.pastHistoryType=='1':
                dic['pastHistoryCode']=pastHistoryCode_ill[each.pastHistoryCode] #既往病代码 返回值为既往病的名称
            else:
    #             print each.pastHistoryCode
                dic['pastHistoryCode']= pastHistoryCode_other[each.pastHistoryCode] 
            dic['pastHistoryAdd']=each.pastHistoryAdd#既往病附件
            dic['pastHistoryDate']=each.pastHistoryDate#既往病日期
            List.append(dic)
        return List
    except:
        print '错误 history_read'
        return False
#===============================================================================
# #添加一个既往病例史，参数为记录ID和一个list 添加成功返回true 否则返回false
#===============================================================================
def history_write(id,List):
    try:
        record=Tbhealthrecord.objects.get(healthFileNumber__exact=id)
        for each in List:
            history=Tbpasthistorylist(tbhealthRecord=record,pastHistoryType=each['pastHistoryType'],pastHistoryCode=each['pastHistoryCode'],pastHistoryAdd=each['pastHistoryAdd'],pastHistoryDate=each['pastHistoryDate'])
            history.save()
        return  True
    except:
        return False


#===============================================================================
# #电子健康档案查询 参数为查询字典 页数，以及每页的记录数， 成功过则返回一个元祖 第一个参数是链表长度 第二个是请求页面  否则返回(0,0)
#===============================================================================
def healthRecordCheck(DIC,page,num,user):
    try:
        userProfile=UserProfile.objects.get(user=user)
        recordList=[]
#         print userProfile.type   #类型 0为管理员 1为医生   2为患者
#         print userProfile.id
        if userProfile.type=='0': #如果是管理员，就选出机构内的所有记录，以及子机构的记录。
#             print userProfile.areaCode
            organizationList=Tbmedicalorganization.objects.filter(Q(ID=userProfile.orgCode.ID)) #首先找到自己的机构
            organizationList=list(organizationList)
            for each in organizationList:#循环找到所有的子机构
                L=[]
                if each.orgType=="62":
                    break;
                else:
                    L=Tbmedicalorganization.objects.filter(Q(parentOrgCode=each.orgCode))
                    
                organizationList.extend(L)
              
            #organizationList=Tbmedicalorganization.objects.filter(Q(ID=userProfile.orgCode.ID)|Q(parentOrgCode=userProfile.orgCode.orgCode))
#             print areaList
            recordList=Tbhealthrecord.objects.filter(Q(organization__in=organizationList),
                                                     idCard__contains=DIC['personId'],#居民身份证号
#                                                      householdRegisterCode__contains=DIC['householdRegisterCode'],#户籍地代码
                                                     genderCode__contains=DIC['genderCode'],#性别代码
                                                     birthday__range=(DIC['star'],DIC['end']),# 建档时间范围
                                                     healthFileNumber__contains=DIC['healthFileNumber'],#健康档案编号
                                                     registerOrgCode__contains=DIC['registerOrgCode'],#建档单位编号
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
            
        elif userProfile.type=='1':#如果是医生，就选择责任医生是他的那些记录
            recordList=Tbhealthrecord.objects.filter(Q(responsibleDoctorCode=userProfile.id),#如果是医生，就选择他管辖的那些记录
                                                     idCard__contains=DIC['personId'],#居民身份证号
#                                                      householdRegisterCode__contains=DIC['householdRegisterCode'],#户籍地代码
                                                     genderCode__contains=DIC['genderCode'],#性别代码
                                                     birthday__range=(DIC['star'],DIC['end']),# 建档时间范围
                                                     healthFileNumber__contains=DIC['healthFileNumber'],#健康档案编号
                                                     registerOrgCode__contains=DIC['registerOrgCode'],#建档单位编号
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
        elif userProfile.type=='2':#如果是用户，就选择personId是自己的那些记录
            recordList=Tbhealthrecord.objects.filter(Q(personProfile=userProfile.id),
                                                     idCard__contains=DIC['personId'],#居民身份证号
#                                                      householdRegisterCode__contains=DIC['householdRegisterCode'],#户籍地代码
                                                     genderCode__contains=DIC['genderCode'],#性别代码
                                                     birthday__range=(DIC['star'],DIC['end']),# 建档时间范围
                                                     healthFileNumber__contains=DIC['healthFileNumber'],#健康档案编号
                                                     registerOrgCode__contains=DIC['registerOrgCode'],#建档单位编号
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
        
        for record in recordList:
            record.genderCode=genderCode[record.genderCode]
        return (len(recordList),recordList[(page-1)*num:page*num])
    except:
        return (0,0)
#===============================================================================
# 查看个人健康档案 参数为个人健康档案号ID. 成功则返回记录的字典  否则返回0
#===============================================================================
def helthRecordCheck_Detail(id): 
    try:
        dict=Tbhealthrecord.objects.filter(ID__exact=id)[0] #获取记录
        record = dict
        if genderCode.has_key(dict.genderCode):
            record.genderCode=genderCode[dict.genderCode]#性别
        else:
            record.genderCode=""
        if residentType.has_key(dict.residentType):
            record.residentType=residentType[dict.residentType]#常住类型
        else :
            record.residentType=""
        if bloodGroupCode.has_key(dict.bloodGroupCode):
            record.bloodGroupCode=bloodGroupCode[dict.bloodGroupCode]#血型代码
        else:
            record.bloodGroupCode=""
        if rhBloodGroupCode.has_key(dict.rhBloodGroupCode):
            record.rhBloodGroupCode=rhBloodGroupCode[dict.rhBloodGroupCode]#RH阴性代码
        else:
            record.rhBloodGroupCode=""
        if eduBGCode.has_key(dict.eduBGCode):
            record.eduBGCode=eduBGCode[dict.eduBGCode]#文化程序代码
        else:
            record.eduBGCode=""
        if occupationCode.has_key(dict.occupationCode):
            record.occupationCode=occupationCode[dict.occupationCode]#职业代码
        else:
            record.occupationCode=""
        if maritalStatusCode.has_key(dict.maritalStatusCode):
            record.maritalStatusCode=maritalStatusCode[dict.maritalStatusCode]#婚姻状况代码
        else :
            record.maritalStatusCode=""
        if paymentMethodCodes.has_key(dict.paymentMethodCodes):
            record.paymentMethodCodes=paymentMethodCodes[dict.paymentMethodCodes]#费用支付方式代码
        else :
            record.paymentMethodCodes=""
        if drugAllergyHistoryCodes.has_key(dict.drugAllergyHistoryCodes):
            record.drugAllergyHistoryCodes=drugAllergyHistoryCodes[dict.drugAllergyHistoryCodes]#药物过敏史
        else :
            record.drugAllergyHistoryCodes=""
        if exposureHistoryCodes.has_key(dict.exposureHistoryCodes):
            
            record.exposureHistoryCodes=exposureHistoryCodes[dict.exposureHistoryCodes]#暴露史代码
        else :
            record.exposureHistoryCodes=""
        if familyHistoryFatherCodes.has_key(dict.familyHistoryFatherCodes):
            record.familyHistoryFatherCodes=familyHistoryFatherCodes[dict.familyHistoryFatherCodes]#家庭病史父亲
        else :
            record.familyHistoryFatherCodes=""
        if familyHistoryMatherCodes.has_key(dict.familyHistoryMatherCodes):
            record.familyHistoryMatherCodes=familyHistoryMatherCodes[dict.familyHistoryMatherCodes]#家庭病史母亲
        else :
            record.familyHistoryMatherCodes=""
        if brotherAndSisterCodes.has_key(dict.brotherAndSisterCodes):
            record.brotherAndSisterCodes=brotherAndSisterCodes[dict.brotherAndSisterCodes]#家庭病史兄弟姐妹
        else :
            record.brotherAndSisterCodes=""
        if familyHistoryChildrenCodes.has_key(dict.familyHistoryChildrenCodes):
            record.familyHistoryChildrenCodes=familyHistoryChildrenCodes[dict.familyHistoryChildrenCodes]#家庭病史儿女
        else :
            record.familyHistoryChildrenCodes=""
        if geneticHistoryCode.has_key(dict.geneticHistoryCode):
            record.geneticHistoryCode=geneticHistoryCode[dict.geneticHistoryCode]#遗传病史
        else :
            record.geneticHistoryCode=""
        if disabilityCodes.has_key(dict.disabilityCodes):
            
            record.disabilityCodes=disabilityCodes[dict.disabilityCodes]#残疾情况
        else :
            record.disabilityCodes=""
        if kitchenExhaustCode.has_key(dict.kitchenExhaustCode):
            record.kitchenExhaustCode=kitchenExhaustCode[dict.kitchenExhaustCode]#厨房排风
        else :
            record.kitchenExhaustCode=""
        if fuelTypeCode.has_key(dict.fuelTypeCode):
            record.fuelTypeCode=fuelTypeCode[dict.fuelTypeCode]#燃料类型
        else :
            record.fuelTypeCode=""
        if waterCode.has_key(dict.waterCode):
            record.waterCode=waterCode[dict.waterCode]#饮水类型
        else :
            record.waterCode=""
        if toiletCode.has_key(dict.toiletCode):
            record.toiletCode=toiletCode[dict.toiletCode]#厕所类型
        else :
            record.toiletCode=""
        if livestockColumnCode.has_key(dict.livestockColumnCode):
            record.livestockColumnCode=livestockColumnCode[dict.livestockColumnCode]#牲畜
        else :
            record.livestockColumnCode=""
        return record
    except:
        return 0

#===============================================================================
# #健康体检表查询 # 参数为查询字典 页数，以及每页的记录数， 成功过则返回一个元祖 第一个参数是链表长度 第二个是请求页面  否则返回(0,0)
#===============================================================================
def healExaminationCheck(DIC,page,num,user):
    try:
        userProfile=UserProfile.objects.get(user=user)
        recordList=[]
        if userProfile.type=='0':                
            organizationList=Tbmedicalorganization.objects.filter(Q(ID=userProfile.orgCode.ID)) #首先找到自己的机构
            organizationList=list(organizationList)
            for each in organizationList:#循环找到所有的子机构
                L=[]
                if each.orgType=="62":
                    break;
                else:
                    L=Tbmedicalorganization.objects.filter(Q(parentOrgCode=each.orgCode))
                organizationList.extend(L)
           
            recordList=Tbhealexamination.objects.filter(Q(organization__in=organizationList),
                                                        #idCard__contains=DIC['personId'],#居民身份证号
                                                         #genderCode__contains=DIC['genderCode'],#性别代码
                                                         #examinationDate__range=(DIC['star'],DIC['end']),# 建档时间范围
                                                         healthFileNumber__contains=DIC['healthFileNumber'],#健康档案编号
                                                         #orgCode__contains=DIC['registerOrgCode'],#建档单位编号
                                                         name__contains=DIC['name'],#姓名
                                                         ).order_by('healthFileNumber')
           
        elif userProfile.type=='1':
            recordList=Tbhealexamination.objects.filter(Q(responsibleDoctorCode=userProfile.id),#医生    查找责任医生是自己的ID那些记录
                                                         #idCard__contains=DIC['personId'],#居民身份证号
                                                         #genderCode__contains=DIC['genderCode'],#性别代码
                                                         #examinationDate__range=(DIC['star'],DIC['end']),# 建档时间范围
                                                         healthFileNumber__contains=DIC['healthFileNumber'],#健康档案编号
                                                         #orgCode__contains=DIC['registerOrgCode'],#建档单位编号
                                                         name__contains=DIC['name'],#姓名
                                                         ).order_by('healthFileNumber')
        elif userProfile.type=='2':
            recordList=Tbhealexamination.objects.filter(Q(personProfile=userProfile.id),#是患者，查找登录名是自己ID的那些用户
                                                         #idCard__contains=DIC['personId'],#居民身份证号
                                                         #genderCode__contains=DIC['genderCode'],#性别代码
                                                         #examinationDate__range=(DIC['star'],DIC['end']),# 建档时间范围
                                                         healthFileNumber__contains=DIC['healthFileNumber'],#健康档案编号
                                                         #orgCode__contains=DIC['registerOrgCode'],#建档单位编号
                                                         name__contains=DIC['name'],#姓名
                                                         ).order_by('healthFileNumber')
       
#         for record in recordList:
#             record.genderCode=genderCode[record.genderCode]
        return (len(recordList),recordList[(page-1)*num:page*num])
    except:
        return (0,0)
#===============================================================================
# 查看个人健康体检  参数为个人健康体检ID. 成功则返回记录的字典  否则返回0
#===============================================================================
def healExaminationCheck_Detail(id): 
    try:
        dict=Tbhealexamination.objects.filter(ID__exact=id)[0] #获取记录
        record = dict
#===============================================================================
# #         record.genderCode=genderCode[dict.genderCode]#性别
# #         record.symptomCodes=symptomCodes[dict.symptomCodes]#症状
# #         record.theAgedStatus=theAgedStatus[dict.theAgedStatus]#老年人健康状况自我评估
# #         record.selfCareAbilityCode=selfCareAbilityCode[dict.selfCareAbilityCode]#老年人生活自理能力自我评估
# #         record.cognitiveFunction=cognitiveFunction[dict.cognitiveFunction]#老年人认知功能
# #         record.emotionalState=emotionalState[dict.emotionalState]#老年人情感状态
# #         record.exerciseFrequencyCode=exerciseFrequencyCode[dict.exerciseFrequencyCode]#体育锻炼情况
# #         record.eatingHabitsCodes=eatingHabitsCodes[dict.eatingHabitsCodes]#饮食习惯
# #         record.smokingStatusCode=smokingStatusCode[dict.smokingStatusCode]#吸烟状态
# #         record.drinkingFrequencyCode=drinkingFrequencyCode[dict.drinkingFrequencyCode]#饮酒频率
# #         record.temperanceCode=temperanceCode[dict.temperanceCode]#是否戒酒
# #         record.whetherDrunk=whetherDrunk[dict.whetherDrunk]#近一年是否饮酒
# #         record.alcoholTypeCodes=alcoholTypeCodes[dict.alcoholTypeCodes]#饮酒种类
# #         record.exposureStateCode=exposureStateCode[dict.exposureStateCode]#是否有职业暴露情况
# #         record.dustProtective=dustProtective[dict.dustProtective]#粉尘防护措施
# #         record.radiogenProtective=radiogenProtective[dict.radiogenProtective]#放射性物质防护措施
# #         record.physicalProtective=physicalProtective[dict.physicalProtective]#物理因素防护措施
# #         record.chemistryProtective=chemistryProtective[dict.chemistryProtective]#化学因素防护措施
# #         record.otherProtective=otherProtective[dict.otherProtective]#其他防护措施
# #         record.lipsCode=lipsCode[dict.lipsCode]#口唇代码
# #         record.dentitionCodes=dentitionCodes[dict.dentitionCodes]#齿 列
# #         record.throatCode=throatCode[dict.throatCode]#咽部
# #         record.hearingCode=hearingCode[dict.hearingCode]#听力
# #         record.motorFunctionCode=motorFunctionCode[dict.motorFunctionCode]#运动功能
# #         record.fundusCode=fundusCode[dict.fundusCode]#眼底
# #         record.skinCode=skinCode[dict.skinCode]#皮肤
# #         record.scleraCode=scleraCode[dict.scleraCode]#巩膜
# #         record.lymphNodeCode=lymphNodeCode[dict.lymphNodeCode]#淋巴结
# #         record.barrelChestCode=barrelChestCode[dict.barrelChestCode]#肺-桶状胸
# #         record.breathSoundCode=breathSoundCode[dict.breathSoundCode]#肺呼吸音
# #         record.raleCode=raleCode[dict.raleCode]#肺罗音
# #         record.rhythmCode=rhythmCode[dict.rhythmCode]#心脏心律
# #         record.cardiacSouffleCode=cardiacSouffleCode[dict.cardiacSouffleCode]#心脏杂音
# #         record.abdomenTendernessCode=abdomenTendernessCode[dict.abdomenTendernessCode]#腹部-压痛
# #         record.abdomenMassCode=abdomenMassCode[dict.abdomenMassCode]#腹部 -包块
# #         record.abdomenLiverCode=abdomenLiverCode[dict.abdomenLiverCode]#腹部-肝大
# #         record.abdomenSplenomegalyCode=abdomenSplenomegalyCode[dict.abdomenSplenomegalyCode]#腹部-脾大
# #         record.abdomenShiftingDullnessCode=abdomenShiftingDullnessCode[dict.abdomenShiftingDullnessCode]#腹部 -移动性浊音
# #         record.legEdemaCode=legEdemaCode[dict.legEdemaCode]#下肢水肿
# #         record.dorsalisPedisPulseCode=dorsalisPedisPulseCode[dict.dorsalisPedisPulseCode]#足背动脉
# #         record.analFingerCodes=analFingerCodes[dict.analFingerCodes]#肛门指诊
# #         record.breastCodes=breastCodes[dict.breastCodes]#乳腺代码
# #         record.vulvaCode=vulvaCode[dict.vulvaCode]#妇科 外阴
# #         record.vaginaCode=vaginaCode[dict.vaginaCode]#妇科 阴道
# #         record.cervixCode=cervixCode[dict.cervixCode]#妇科 宫颈
# #         record.uterusCode=uterusCode[dict.uterusCode]#妇科 宫体
# #         record.uterineAccessoriesCode=uterineAccessoriesCode[dict.uterineAccessoriesCode]#妇科 附件
# #         record.urineProteinCode=urineProteinCode[dict.urineProteinCode]#尿常规 尿蛋白
# #         record.urineSugarCode=urineSugarCode[dict.urineSugarCode]#尿常规 尿糖
# #         record.urineKetoneCode=urineKetoneCode[dict.urineKetoneCode]#尿常规 尿酮体
# #         record.urineOccultBloodCode=urineOccultBloodCode[dict.urineOccultBloodCode]#尿常规 鸟潜血
# #         record.ECGCode=ECGCode[dict.ECGCode]#心电图
# #         record.fecalOccultBloodCode=fecalOccultBloodCode[dict.fecalOccultBloodCode]#大便潜血
# #         record.HBsAgCode=HBsAgCode[dict.HBsAgCode]#乙 型 肝 炎表面抗原
# #         record.chestXRayCode=chestXRayCode[dict.chestXRayCode]#胸部 X线片
# #         record.BScanCode=BScanCode[dict.BScanCode]#B超
# #         record.papSmearCode=papSmearCode[dict.papSmearCode]#宫 颈 涂 片
# #         record.flatAndQualityCode=flatAndQualityCode[dict.flatAndQualityCode]#中 医 平 和质
# #         record.qiDeficiencyCode=qiDeficiencyCode[dict.qiDeficiencyCode]#中 医 气 虚质
# #         record.yangXuzhiCode=yangXuzhiCode[dict.yangXuzhiCode]#中 医 阳 虚
# #         record.yinDeficiencyCode=yinDeficiencyCode[dict.yinDeficiencyCode]#中 医 阴 虚
# #         record.phlegmDampnessQualityCode=phlegmDampnessQualityCode[dict.phlegmDampnessQualityCode]#中 医 痰 湿
# #         record.hotAndHumidQualityCode=hotAndHumidQualityCode[dict.hotAndHumidQualityCode]#中 医 湿 热
# #         record.bloodStasisCode=bloodStasisCode[dict.bloodStasisCode]#中 医 血 瘀
# #         record.qiStagnationCode=qiStagnationCode[dict.qiStagnationCode]#中 医 气 郁
# #         record.specialQualityCode=specialQualityCode[dict.specialQualityCode]#中 医 特 秉
# #         record.cerebrovascularCodes=cerebrovascularCodes[dict.cerebrovascularCodes]#脑 血 管 疾病
# #         record.kidneyDiseaseCodes=kidneyDiseaseCodes[dict.kidneyDiseaseCodes]#肾 脏 疾 病
# #         record.heartDiseaseCodes=heartDiseaseCodes[dict.heartDiseaseCodes]#心 脏 疾 病
# #         record.vascularDiseaseCodes=vascularDiseaseCodes[dict.vascularDiseaseCodes]#血 管 疾 病
# #         record.eyeDiseaseCodes=eyeDiseaseCodes[dict.eyeDiseaseCodes]#眼 部 疾 病
# #         record.healthEvaluationCode=healthEvaluationCode[dict.healthEvaluationCode]#健康评价
# #         record.healthGuidanceCodes=healthGuidanceCodes[dict.healthGuidanceCodes]#健康指导
# #         record.riskFactorsCodes=riskFactorsCodes[dict.riskFactorsCodes]#危险因素控制
#===============================================================================
        if genderCode.has_key(dict.genderCode):
            record.genderCode=genderCode[dict.genderCode]#性别
        else:
            record.genderCode="无此字典，请检查数据库"
        if symptomCodes.has_key(dict.symptomCodes):
            record.symptomCodes=symptomCodes[dict.symptomCodes]#症状
        else:
            record.symptomCodes="无此字典，请检查数据库"
        if theAgedStatus.has_key(dict.theAgedStatus):
            record.theAgedStatus=theAgedStatus[dict.theAgedStatus]#老年人健康状况自我评估
        else:
            record.theAgedStatus="无此字典，请检查数据库"          
        if selfCareAbilityCode.has_key(dict.selfCareAbilityCode):
            record.selfCareAbilityCode=selfCareAbilityCode[dict.selfCareAbilityCode]#老年人生活自理能力自我评估
        else:
            record.selfCareAbilityCode="无此字典，请检查数据库"  
        if cognitiveFunction.has_key(dict.cognitiveFunction):
            record.cognitiveFunction=cognitiveFunction[dict.cognitiveFunction]#老年人认知功能
        else:
            record.cognitiveFunction="无此字典，请检查数据库"  
        if emotionalState.has_key(dict.emotionalState):
            record.emotionalState=emotionalState[dict.emotionalState]#老年人情感状态
        else:
            record.emotionalState="无此字典，请检查数据库"  
        if exerciseFrequencyCode.has_key(dict.exerciseFrequencyCode):
            record.exerciseFrequencyCode=exerciseFrequencyCode[dict.exerciseFrequencyCode]#体育锻炼情况
        else:
            record.exerciseFrequencyCode="无此字典，请检查数据库"  
        if eatingHabitsCodes.has_key(dict.eatingHabitsCodes):
            record.eatingHabitsCodes=eatingHabitsCodes[dict.eatingHabitsCodes]#饮食习惯
        else:
            record.eatingHabitsCodes="无此字典，请检查数据库"  
        if smokingStatusCode.has_key(dict.smokingStatusCode):
            record.smokingStatusCode=smokingStatusCode[dict.smokingStatusCode]#吸烟状态
        else:
            record.smokingStatusCode="无此字典，请检查数据库"  
        if drinkingFrequencyCode.has_key(dict.drinkingFrequencyCode):
            record.drinkingFrequencyCode=drinkingFrequencyCode[dict.drinkingFrequencyCode]#饮酒频率
        else:
            record.drinkingFrequencyCode="无此字典，请检查数据库"   
        if temperanceCode.has_key(dict.temperanceCode):
            record.temperanceCode=temperanceCode[dict.temperanceCode]#是否戒酒
        else:
            record.temperanceCode="无此字典，请检查数据库"  
        if whetherDrunk.has_key(dict.whetherDrunk):
            record.whetherDrunk=whetherDrunk[dict.whetherDrunk]#近一年是否饮酒
        else:
            record.whetherDrunk="无此字典，请检查数据库"  
        if alcoholTypeCodes.has_key(dict.alcoholTypeCodes):
            record.alcoholTypeCodes=alcoholTypeCodes[dict.alcoholTypeCodes]#饮酒种类
        else:
            record.alcoholTypeCodes="无此字典，请检查数据库"  
        if exposureStateCode.has_key(dict.exposureStateCode):
            record.exposureStateCode=exposureStateCode[dict.exposureStateCode]#是否有职业暴露情况
        else:
            record.exposureStateCode="无此字典，请检查数据库"            
        if dustProtective.has_key(dict.dustProtective):
            record.dustProtective=dustProtective[dict.dustProtective]#粉尘防护措施
        else:
            record.dustProtective="无此字典，请检查数据库"  
        if radiogenProtective.has_key(dict.radiogenProtective):
            record.radiogenProtective=radiogenProtective[dict.radiogenProtective]#放射性物质防护措施
        else:
            record.radiogenProtective="无此字典，请检查数据库"  
        if physicalProtective.has_key(dict.physicalProtective):
            record.physicalProtective=physicalProtective[dict.physicalProtective]#物理因素防护措施
        else:
            record.physicalProtective="无此字典，请检查数据库"  
        if chemistryProtective.has_key(dict.chemistryProtective):
            record.chemistryProtective=chemistryProtective[dict.chemistryProtective]#化学因素防护措施
        else:
            record.chemistryProtective="无此字典，请检查数据库"  
        if otherProtective.has_key(dict.otherProtective):
            record.otherProtective=otherProtective[dict.otherProtective]#其他防护措施
        else:
            record.otherProtective="无此字典，请检查数据库"  
        if lipsCode.has_key(dict.lipsCode):
            record.lipsCode=lipsCode[dict.lipsCode]#口唇代码
        else:
            record.lipsCode="无此字典，请检查数据库"    
        if dentitionCodes.has_key(dict.dentitionCodes):
            record.dentitionCodes=dentitionCodes[dict.dentitionCodes]#齿 列
        else:
            record.dentitionCodes="无此字典，请检查数据库"          
        if throatCode.has_key(dict.throatCode):
            record.throatCode=throatCode[dict.throatCode]#咽部
        else:
            record.throatCode="无此字典，请检查数据库"     
        if hearingCode.has_key(dict.hearingCode):
            record.hearingCode=hearingCode[dict.hearingCode]#听力
        else:
            record.hearingCode="无此字典，请检查数据库" 
        if motorFunctionCode.has_key(dict.motorFunctionCode):
            record.motorFunctionCode=motorFunctionCode[dict.motorFunctionCode]#运动功能
        else:
            record.motorFunctionCode="无此字典，请检查数据库" 
        if fundusCode.has_key(dict.fundusCode):
            record.fundusCode=fundusCode[dict.fundusCode]#眼底
        else:
            record.fundusCode="无此字典，请检查数据库" 
        if skinCode.has_key(dict.skinCode):
            record.skinCode=skinCode[dict.skinCode]#皮肤
        else:
            record.skinCode="无此字典，请检查数据库" 
        if scleraCode.has_key(dict.scleraCode):
            record.scleraCode=scleraCode[dict.scleraCode]#巩膜
        else:
            record.scleraCode="无此字典，请检查数据库" 
        if lymphNodeCode.has_key(dict.lymphNodeCode):
            record.lymphNodeCode=lymphNodeCode[dict.lymphNodeCode]#淋巴结
        else:
            record.lymphNodeCode="无此字典，请检查数据库" 
        if barrelChestCode.has_key(dict.barrelChestCode):
            record.barrelChestCode=barrelChestCode[dict.barrelChestCode]#肺-桶状胸
        else:
            record.barrelChestCode="无此字典，请检查数据库" 
        if breathSoundCode.has_key(dict.breathSoundCode):
            record.breathSoundCode=breathSoundCode[dict.breathSoundCode]#肺呼吸音
        else:
            record.breathSoundCode="无此字典，请检查数据库" 
        if raleCode.has_key(dict.raleCode):
            record.raleCode=raleCode[dict.raleCode]#肺罗音
        else:
            record.raleCode="无此字典，请检查数据库" 
        if rhythmCode.has_key(dict.rhythmCode):
            record.rhythmCode=rhythmCode[dict.rhythmCode]#心脏心律
        else:
            record.rhythmCode="无此字典，请检查数据库" 
        if cardiacSouffleCode.has_key(dict.cardiacSouffleCode):
            record.cardiacSouffleCode=cardiacSouffleCode[dict.cardiacSouffleCode]#心脏杂音
        else:
            record.cardiacSouffleCode="无此字典，请检查数据库" 
        if abdomenTendernessCode.has_key(dict.abdomenTendernessCode):
            record.abdomenTendernessCode=abdomenTendernessCode[dict.abdomenTendernessCode]#腹部-压痛
        else:
            record.abdomenTendernessCode="无此字典，请检查数据库" 
        if abdomenMassCode.has_key(dict.abdomenMassCode):
            record.abdomenMassCode=abdomenMassCode[dict.abdomenMassCode]#腹部 -包块
        else:
            record.abdomenMassCode="无此字典，请检查数据库" 
        if abdomenLiverCode.has_key(dict.abdomenLiverCode):
            record.abdomenLiverCode=abdomenLiverCode[dict.abdomenLiverCode]#腹部-肝大
        else:
            record.abdomenLiverCode="无此字典，请检查数据库" 
        if abdomenSplenomegalyCode.has_key(dict.abdomenSplenomegalyCode):
            record.abdomenSplenomegalyCode=abdomenSplenomegalyCode[dict.abdomenSplenomegalyCode]#腹部-脾大
        else:
            record.abdomenSplenomegalyCode="无此字典，请检查数据库" 
        if abdomenShiftingDullnessCode.has_key(dict.abdomenShiftingDullnessCode):
            record.abdomenShiftingDullnessCode=abdomenShiftingDullnessCode[dict.abdomenShiftingDullnessCode]#腹部 -移动性浊音
        else:
            record.abdomenShiftingDullnessCode="无此字典，请检查数据库" 
        if legEdemaCode.has_key(dict.legEdemaCode):
            record.legEdemaCode=legEdemaCode[dict.legEdemaCode]#下肢水肿
        else:
            record.legEdemaCode="无此字典，请检查数据库" 
        if dorsalisPedisPulseCode.has_key(dict.dorsalisPedisPulseCode):
            record.dorsalisPedisPulseCode=dorsalisPedisPulseCode[dict.dorsalisPedisPulseCode]#足背动脉
        else:
            record.dorsalisPedisPulseCode="无此字典，请检查数据库" 
        if analFingerCodes.has_key(dict.analFingerCodes):
            record.analFingerCodes=analFingerCodes[dict.analFingerCodes]#肛门指诊
        else:
            record.analFingerCodes="无此字典，请检查数据库" 
        if breastCodes.has_key(dict.breastCodes):
            record.breastCodes=breastCodes[dict.breastCodes]#乳腺代码
        else:
            record.breastCodes="无此字典，请检查数据库" 
        if vulvaCode.has_key(dict.vulvaCode):
            record.vulvaCode=vulvaCode[dict.vulvaCode]#妇科 外阴
        else:
            record.vulvaCode="无此字典，请检查数据库" 
        if vaginaCode.has_key(dict.vaginaCode):
            record.vaginaCode=vaginaCode[dict.vaginaCode]#妇科 阴道
        else:
            record.vaginaCode="无此字典，请检查数据库" 
        if cervixCode.has_key(dict.cervixCode):
            record.cervixCode=cervixCode[dict.cervixCode]#妇科 宫颈
        else:
            record.cervixCode="无此字典，请检查数据库" 
        if uterusCode.has_key(dict.uterusCode):
            record.uterusCode=uterusCode[dict.uterusCode]#妇科 宫体
        else:
            record.uterusCode="无此字典，请检查数据库" 
        if uterineAccessoriesCode.has_key(dict.uterineAccessoriesCode):
            record.uterineAccessoriesCode=uterineAccessoriesCode[dict.uterineAccessoriesCode]#妇科 附件
        else:
            record.uterineAccessoriesCode="无此字典，请检查数据库" 
        if urineProteinCode.has_key(dict.urineProteinCode):
            record.urineProteinCode=urineProteinCode[dict.urineProteinCode]#尿常规 尿蛋白
        else:
            record.urineProteinCode="无此字典，请检查数据库" 
        if urineSugarCode.has_key(dict.urineSugarCode):
            record.urineSugarCode=urineSugarCode[dict.urineSugarCode]#尿常规 尿糖
        else:
            record.urineSugarCode="无此字典，请检查数据库" 
        if urineKetoneCode.has_key(dict.urineKetoneCode):
            record.urineKetoneCode=urineKetoneCode[dict.urineKetoneCode]#尿常规 尿酮体
        else:
            record.urineKetoneCode="无此字典，请检查数据库" 
        if urineOccultBloodCode.has_key(dict.urineOccultBloodCode):
            record.urineOccultBloodCode=urineOccultBloodCode[dict.urineOccultBloodCode]#尿常规 鸟潜血
        else:
            record.urineOccultBloodCode="无此字典，请检查数据库" 
        if ECGCode.has_key(dict.ECGCode):
            record.ECGCode=ECGCode[dict.ECGCode]#心电图
        else:
            record.ECGCode="无此字典，请检查数据库" 
        if fecalOccultBloodCode.has_key(dict.fecalOccultBloodCode):
            record.fecalOccultBloodCode=fecalOccultBloodCode[dict.fecalOccultBloodCode]#大便潜血
        else:
            record.fecalOccultBloodCode="无此字典，请检查数据库" 
        if HBsAgCode.has_key(dict.HBsAgCode):
            record.HBsAgCode=HBsAgCode[dict.HBsAgCode]#乙 型 肝 炎表面抗原
        else:
            record.HBsAgCode="无此字典，请检查数据库" 
        if chestXRayCode.has_key(dict.chestXRayCode):
            record.chestXRayCode=chestXRayCode[dict.chestXRayCode]#胸部 X线片
        else:
            record.chestXRayCode="无此字典，请检查数据库" 
        if BScanCode.has_key(dict.BScanCode):
            record.BScanCode=BScanCode[dict.BScanCode]#B超
        else:
            record.BScanCode="无此字典，请检查数据库" 
        if papSmearCode.has_key(dict.papSmearCode):
            record.papSmearCode=papSmearCode[dict.papSmearCode]#宫 颈 涂 片
        else:
            record.papSmearCode="无此字典，请检查数据库" 
        if flatAndQualityCode.has_key(dict.flatAndQualityCode):
            record.flatAndQualityCode=flatAndQualityCode[dict.flatAndQualityCode]#中 医 平 和质
        else:
            record.flatAndQualityCode="无此字典，请检查数据库" 
        if qiDeficiencyCode.has_key(dict.qiDeficiencyCode):
            record.qiDeficiencyCode=qiDeficiencyCode[dict.qiDeficiencyCode]#中 医 气 虚质
        else:
            record.qiDeficiencyCode="无此字典，请检查数据库" 
        if yangXuzhiCode.has_key(dict.yangXuzhiCode):
            record.yangXuzhiCode=yangXuzhiCode[dict.yangXuzhiCode]#中 医 阳 虚
        else:
            record.yangXuzhiCode="无此字典，请检查数据库" 
        if yinDeficiencyCode.has_key(dict.yinDeficiencyCode):
            record.yinDeficiencyCode=yinDeficiencyCode[dict.yinDeficiencyCode]#中 医 阴 虚
        else:
            record.yinDeficiencyCode="无此字典，请检查数据库" 
        if phlegmDampnessQualityCode.has_key(dict.phlegmDampnessQualityCode):
            record.phlegmDampnessQualityCode=phlegmDampnessQualityCode[dict.phlegmDampnessQualityCode]#中 医 痰 湿
        else:
            record.phlegmDampnessQualityCode="无此字典，请检查数据库" 
        if hotAndHumidQualityCode.has_key(dict.hotAndHumidQualityCode):
            record.hotAndHumidQualityCode=hotAndHumidQualityCode[dict.hotAndHumidQualityCode]#中 医 湿 热
        else:
            record.hotAndHumidQualityCode="无此字典，请检查数据库" 
        if bloodStasisCode.has_key(dict.bloodStasisCode):
            record.bloodStasisCode=bloodStasisCode[dict.bloodStasisCode]#中 医 血 瘀
        else:
            record.bloodStasisCode="无此字典，请检查数据库" 
        if qiStagnationCode.has_key(dict.qiStagnationCode):
            record.qiStagnationCode=qiStagnationCode[dict.qiStagnationCode]#中 医 气 郁
        else:
            record.qiStagnationCode="无此字典，请检查数据库" 
        if specialQualityCode.has_key(dict.specialQualityCode):
            record.specialQualityCode=specialQualityCode[dict.specialQualityCode]#中 医 特 秉
        else:
            record.specialQualityCode="无此字典，请检查数据库" 
        if cerebrovascularCodes.has_key(dict.cerebrovascularCodes):
            record.cerebrovascularCodes=cerebrovascularCodes[dict.cerebrovascularCodes]#脑 血 管 疾病
        else:
            record.cerebrovascularCodes="无此字典，请检查数据库" 
        if kidneyDiseaseCodes.has_key(dict.kidneyDiseaseCodes):
            record.kidneyDiseaseCodes=kidneyDiseaseCodes[dict.kidneyDiseaseCodes]#肾 脏 疾 病
        else:
            record.kidneyDiseaseCodes="无此字典，请检查数据库" 
        if heartDiseaseCodes.has_key(dict.heartDiseaseCodes):
            record.heartDiseaseCodes=heartDiseaseCodes[dict.heartDiseaseCodes]#心 脏 疾 病
        else:
            record.heartDiseaseCodes="无此字典，请检查数据库" 
        if vascularDiseaseCodes.has_key(dict.vascularDiseaseCodes):
            record.vascularDiseaseCodes=vascularDiseaseCodes[dict.vascularDiseaseCodes]#血 管 疾 病
        else:
            record.vascularDiseaseCodes="无此字典，请检查数据库" 
        if eyeDiseaseCodes.has_key(dict.eyeDiseaseCodes):
            record.eyeDiseaseCodes=eyeDiseaseCodes[dict.eyeDiseaseCodes]#眼 部 疾 病
        else:
            record.eyeDiseaseCodes="无此字典，请检查数据库" 
        if healthEvaluationCode.has_key(dict.healthEvaluationCode):
            record.healthEvaluationCode=healthEvaluationCode[dict.healthEvaluationCode]#健康评价
        else:
            record.healthEvaluationCode="无此字典，请检查数据库" 
        if healthGuidanceCodes.has_key(dict.healthGuidanceCodes):
            record.healthGuidanceCodes=healthGuidanceCodes[dict.healthGuidanceCodes]#健康指导
        else:
            record.healthGuidanceCodes="无此字典，请检查数据库" 
        if riskFactorsCodes.has_key(dict.riskFactorsCodes):
            record.riskFactorsCodes=riskFactorsCodes[dict.riskFactorsCodes]#危险因素控制
        else:
            record.riskFactorsCodes="无此字典，请检查数据库" 
        if nerveSystemDiseaseCode.has_key(dict.nerveSystemDiseaseCode):
            record.nerveSystemDiseaseCode=nerveSystemDiseaseCode[dict.nerveSystemDiseaseCode]#神经系统疾病
        else:
            record.nerveSystemDiseaseCode="无此字典，请检查数据库" 
        if otherSystemDiseaseCode.has_key(dict.otherSystemDiseaseCode):
            record.otherSystemDiseaseCode=otherSystemDiseaseCode[dict.otherSystemDiseaseCode]#其他系统疾病
        else:
            record.otherSystemDiseaseCode="无此字典，请检查数据库"        
        return record
    except:
        return 0




#===============================================================================
# 高血压随访记录查询     参数为查询字典 页数，以及每页的记录数， 成功过则返回一个元祖 第一个参数是链表长度 第二个是请求页面  否则返回(0,0)
#===============================================================================
def hypertensionflupCheck(DIC,page,num,user):
    try:
        userProfile=UserProfile.objects.get(user=user)
        recordList=[]
#         print userProfile.type   #类型 0为管理员 1为医生   2为患者
#         print userProfile.id
        if userProfile.type=='0': #如果是管理员，
            organizationList=Tbmedicalorganization.objects.filter(Q(ID=userProfile.orgCode.ID)) #首先找到自己的机构
            organizationList=list(organizationList)
            for each in organizationList:#循环找到所有的子机构
                L=[]
                if each.orgType=="62":
                    break;
                else:
                    L=Tbmedicalorganization.objects.filter(Q(parentOrgCode=each.orgCode))
                    
                organizationList.extend(L)
            recordList=Tbhypertensionflup.objects.filter(Q(organization__in=organizationList),
                                                    name__contains=DIC['name']#姓名
                                                     ).order_by('healthFileNumber')
            
        elif userProfile.type=='1':#如果是医生，就选择责任医生是他的那些记录
            recordList=Tbhypertensionflup.objects.filter(Q(responsibleDoctorCode=userProfile.id),#如果是医生，就选择他管辖的那些记录
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
        elif userProfile.type=='2':#如果是用户，就选择personId是自己的那些记录
            recordList=Tbhypertensionflup.objects.filter(Q(personProfile=userProfile.id),
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
#         for record in recordList:
#             record.genderCode=genderCode[record.genderCode]
        return (len(recordList),recordList[(page-1)*num:page*num])
    except:
        return (0,0)
     
def diabetesflupCheck(DIC,page,num,user):
    try:
        userProfile=UserProfile.objects.get(user=user)
        recordList=[]
#         print userProfile.type   #类型 0为管理员 1为医生   2为患者
#         print userProfile.id
        if userProfile.type=='0': #如果是管理员，就选出区域内的所有记录
            organizationList=Tbmedicalorganization.objects.filter(Q(ID=userProfile.orgCode.ID)) #首先找到自己的机构
            organizationList=list(organizationList)
            for each in organizationList:#循环找到所有的子机构
                L=[]
                if each.orgType=="62":
                    break;
                else:
                    L=Tbmedicalorganization.objects.filter(Q(parentOrgCode=each.orgCode))
                    
                organizationList.extend(L)
            recordList=Tbdiabetesflup.objects.filter(Q(organization__in=organizationList),
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
        elif userProfile.type=='1':#如果是医生，就选择责任医生是他的那些记录
            recordList=Tbdiabetesflup.objects.filter(Q(responsibleDoctorCode=userProfile.id),#如果是医生，就选择他管辖的那些记录
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
        elif userProfile.type=='2':#如果是用户，就选择personId是自己的那些记录
            recordList=Tbdiabetesflup.objects.filter(Q(personProfile=userProfile.id),
                                                     name__contains=DIC['name'],#姓名
                                                     ).order_by('healthFileNumber')
#         for record in recordList:
#             record.genderCode=genderCode[record.genderCode]
        return (len(recordList),recordList[(page-1)*num:page*num])
    except:
        return (0,0)
def YTJMeasureCheck(DIC,page,num,user):
    try:
        userProfile=UserProfile.objects.get(user=user)
        recordList=[]
#         print userProfile.type   #类型 0为管理员 1为医生   2为患者
        
        if userProfile.type=='0': #如果是管理员，就选出区域内的所有记录   
           
            organizationList=Tbmedicalorganization.objects.filter(Q(ID=userProfile.orgCode.ID)) #首先找到自己的机构
            organizationList=list(organizationList)
            
            for each in organizationList:#循环找到所有的子机构
                L=[]
                if each.orgType=="62":
                    break;
                else:
                    L=Tbmedicalorganization.objects.filter(Q(parentOrgCode=each.orgCode))
                    
                organizationList.extend(L)
#             recordList=YTJMeasure.objects.filter(Q(organization__in=organizationList),
#                                                 machineCode__contains=DIC['machineCode'],
#                                                 time__range=(DIC['start'],DIC['end']),#birthday__range=(DIC['star'],DIC['end']),
#                                                 name__contains=DIC['name'],#姓名
#                                                 ).order_by('ID')
            print '___________ajskldfjajs',DIC
            recordList=YTJMeasure.objects.filter(Q(organization__in=organizationList),
                                                #machineCode__contains=DIC['machineCode'],
                                                #time__range=(DIC['start'],DIC['end']),#birthday__range=(DIC['star'],DIC['end']),
#                                                 idCard__contains=DIC['idCard'],
#                                                 name__contains=DIC['name'],#姓名
                                                ).values('idCard','name','householdRegisterCode','responsibleDoctorCode').annotate(count=Count('idCard'))
            print 'LIu',len(recordList)                                      
        elif userProfile.type=='1':#如果是医生，就选择责任医生是他的那些记录
            recordList=YTJMeasure.objects.filter(Q(responsibleDoctorCode=userProfile.id),#如果是医生，就选择他管辖的那些记录
                                                     #machineCode__contains=DIC['machineCode'],
                                                     #time__range=(DIC['start'],DIC['end']),
                                                     #idCard__contains=DIC['idCard'],
                                                     name__contains=DIC['name'],#姓名
                                                     ).values('idCard','name','householdRegisterCode','responsibleDoctorCode').annotate(count=Count('idCard'))
        elif userProfile.type=='2':#如果是用户，就选择personId是自己的那些记录
            recordList=YTJMeasure.objects.filter(Q(personProfile=userProfile.id),
                                                    # machineCode__contains=DIC['machineCode'],
                                                     #time__range=(DIC['start'],DIC['end']),
                                                     idCard__contains=DIC['idCard'],
                                                     name__contains=DIC['name'],#姓名
                                                   ).values('idCard','name','householdRegisterCode','responsibleDoctorCode').annotate(count=Count('idCard'))
       
        print 'asdfasdfasdf',len(recordList) ,type(recordList),recordList
        for record in recordList: 
            if record.has_key('genderCode'):
                record['genderCode']=genderCode[record['genderCode']]
        
        return (len(recordList),recordList[(page-1)*num:page*num])
    except:
        print "Error7/4"
        return (0,0)

def JKCL_Check(DIC):
    try:
        records=YTJMeasure.objects.filter(idCard__exact=DIC['idCard'],
                                         data__contains=DIC['filter'],
                                         data__has_keys=DIC['item'],
                                         time__range=(DIC['start'],DIC['end']),
                                          ).order_by('time')
        return records
    except:
        print '健康测量查询错误'
        return 0        
    
    
    
    