#-*- coding: UTF-8 -*-
from types import NoneType
from rest_framework import serializers
from website.models import Tbdiabetesflup, Tbhypertensionflup,Tbhypertensionspecial, TbdiabetesSpecial, Tbvaccinationhistory, Tbmedicationlist, Tbfamilybedhistory, Tbhospitalizedhistory, Tbpasthistorylist, Tbarea, Tbmedicalorganization, UserProfile, Tbhealthrecord, Tbhealexamination, YTJMeasure

class TbhypertensionflupListSerializer(serializers.ListSerializer):
    def saveCustomerKeys(self, record, xmlData):
        return
    
    def create(self, validated_data):
        record = Tbhypertensionflup.objects.create(**(validated_data[0]))
        self.saveCustomerKeys(record, self.context[0])
        return record

    def update(self, records, validated_data):
        records.update(**(validated_data[0]))
        self.saveCustomerKeys(records[0], self.context[0])
        return records
    
class TbhypertensionflupSeri(serializers.ModelSerializer): # 高血压随访档案
    personId = serializers.SerializerMethodField('getPersonIdFromSpecialNo')
    flupDoctorCode = serializers.SerializerMethodField('getDoctorId')
        
    class Meta:
        model = Tbhypertensionflup
        list_serializer_class = TbhypertensionflupListSerializer
        fields = ('businessKey','healthFileNumber', 'personId','name', 'flupDate', 'flupMode','symptomCodes','symptomOther','SBP','DBP',
                  'bloodPressureLevel','weight','weightTarget','bmi','bmiTarget','heartRate','signsOther','dailySmoking','dailySmokingTarget',
                  'dailyDrinkingTarget','dailyDrinking','perWeekMovements','perWeekMovementsTarget','perWeekTimes','perWeekTimesTarget',
                  'saltIntakeCode','saltIntakeTargetCode','psychologicalCode','complianceCode','aidCheck','doseCode','adverseReactionCode',
                  'flupTypeCode','medicationList','referralReason','referralOrg','referralDepartment','flupDoctorCode','flupDoctorName',
                  'flupOrgCode','flupOrgName','nextFlupDate', 'specialNo')

    def getPersonIdFromSpecialNo(self, obj):
        return obj.specialNo
    
    def getDoctorId(self, obj):
        return obj.responsibleDoctorCode.id
    
class TbhypertensionspecialSeri(serializers.ModelSerializer): # 高血压专项档案
    personId = serializers.SerializerMethodField('getPersonIdFromSpecialNo')
    registerDoctorCode = serializers.SerializerMethodField('getDoctorId')
    registerDate = serializers.SerializerMethodField('getRegisterDate')
    
    class Meta:
        model = Tbhypertensionspecial
        fields = ('personId','householdRegisterCode', 'responsibleDoctorCode','organization','specialNo','mechineCode','mechineNo','name',
                  'genderCode','SBP','DBP','bloodPressureLevel','nextFlupDate','registerDate','registerOrgCode','registerDoctorCode','registerDoctorName',
                  'diagnoseDate','diagnoseOrgCode','diagnoseDoctorCode','diagnoseDoctorName')       
        
    def getRegisterDate(self, obj):
        return obj.registDate
    
    def getPersonIdFromSpecialNo(self, obj):
        return obj.specialNo
    
    def getDoctorId(self, obj):
        return obj.responsibleDoctorCode.id

class TbdiabetesflupSeri(serializers.ModelSerializer): # 糖尿病随访档案
    personId = serializers.SerializerMethodField('getPersonIdFromSpecialNo')
    flupDoctorCode = serializers.SerializerMethodField('getDoctorId')
    
    class Meta:
        model = Tbdiabetesflup
        fields = ('businessKey', 'healthFileNumber','name','flupDate', 'flupMode', 'symptomCodes', 'symptomOther',
                'SBP', 'DBP', 'bloodPressureLevel', 'weight', 'weightTarget', 'bmi', 'bmiTarget', 'dorsalisPedisPulseCode',
                'signsOther', 'dailySmoking', 'dailySmokingTarget', 'dailyDrinking', 'dailyDrinkingTarget', 'perWeekMovements',
                'perWeekMovementsTarget', 'perWeekTimes', 'perWeekTimesTarget', 'stapleFood', 'stapleFoodTarget', 'psychologicalCode',
                'complianceCode', 'fastingBloodGlucose', 'HbA1c', 'aidCheckDate', 'aidCheck', 'doseCode',
                'medicationList', 'flupTypeCode', 'adverseReactionCode', 'lowBloodSugarCode', 'insulinMedicationType',
                'insulinMedicationDose', 'referralReason', 'referralOrg', 'referralDepartment', 'flupDoctorName',
                'flupOrgCode', 'flupOrgName', 'nextFlupDate', 'personId', 'flupDoctorCode')
        
    def getPersonIdFromSpecialNo(self, obj):
        return obj.specialNo
      
    def getDoctorId(self, obj):
        return obj.responsibleDoctorCode.id

class TbdiabetesSpecialSeri(serializers.ModelSerializer): # 糖尿病专项档案
    personId = serializers.SerializerMethodField('getPersonIdFromSpecialNo')
    registerDoctorCode = serializers.SerializerMethodField('getDoctorId')
    
    class Meta:
        model = TbdiabetesSpecial
        fields = ('personId', 'specialNo','name','registerDate','registerOrgCode','registerDoctorCode','registerDoctorName','diagnoseDate',
                  'diagnoseOrgCode','diagnoseDoctorName','SBP','DBP','bloodPressureLevel','nextFlupDate','diabetesLevelCode','caseType','ICDCode',
                  'doseCode','noMedicationCode','drugCost','familyHistoryCode','height','randomBloodGlucose','kidneyDiseaseYears','retinalDiseaseYears',
                  'neuropathyYears','skinInfectionYears','vascularDiseaseYears','noComplYears','complicationDate','initialDisease','currentDisease', 
                  'caseSourceCode','caseSourceOther')
        
    def getPersonIdFromSpecialNo(self, obj):
        return obj.specialNo
    
    def getDoctorId(self, obj):
        return obj.responsibleDoctorCode.id

# Related to register.
class TbUserSeri(serializers.ModelSerializer):
    userCode = serializers.SerializerMethodField('getPersonIdFromProfile')
    userName = serializers.SerializerMethodField('getPersonNameFromProfile')
    
    class Meta:
        model = UserProfile
        fields = ('userCode', 'userName', 'pym', 'wbm')
        
    def getPersonIdFromProfile(self, obj):
        return obj.id
    
    def getPersonNameFromProfile(self, obj):
        return obj.__str__()
    
class TbareaSeri(serializers.ModelSerializer):
    class Meta:
        model = Tbarea
        fields = ('areaCode', 'areaName', 'areaType', 'parentAreaCode')

class TbmedicalorganizationSeri(serializers.ModelSerializer):
    class Meta:
        model = Tbmedicalorganization
        fields = ('orgCode', 'orgName', 'orgType', 'parentOrgCode', 'areaCode', 'levelOrder')

# Related to healthy record.        
class TbpasthistorylistSeri(serializers.ModelSerializer):
    class Meta:
        model = Tbpasthistorylist
        fields = ('pastHistoryType', 'pastHistoryCode', 'pastHistoryAdd', 'pastHistoryDate')

class HealthyRecordListSerializer(serializers.ListSerializer):
    def saveCustomerKeys(self, record, xmlData):        
        # Save profile object to 'personProfile' field.
        try:
            personId = int(xmlData['responsibleDoctorCode'])
        except:
            print("No doctorId")
        else:
            profile = UserProfile.objects.filter(id=personId)
            if len(profile) != 0:
                record.responsibleDoctorCode = profile[0]
                record.save()

        # Save doctor name to 'responsibleDoctorName' field.
        print(xmlData)
        try:
            doctorId = int(xmlData['responsibleDoctorCode'])
        except:
            print("No doctorId")
        else:
            profile = UserProfile.objects.filter(id=doctorId)
            record.responsibleDoctorName = profile[0].__str__()
            record.save()
 
        # Save area object to 'areaCode' field.
        try:
            areaCode = xmlData['householdRegisterCode']
            print(areaCode)
        except:
            print("No such area code")
        else:
            area = Tbarea.objects.filter(areaCode=areaCode)
            if len(area) != 0:
                record.householdRegisterCode = area[0]
                record.save()
        
        # Save past history to 'pastHistoryList' table.
        history = Tbpasthistorylist.objects.filter(tbhealthRecord=record)
        history.delete()
        try: 
            for pastHistory in xmlData.get('pastHistoryList'):
                historyDate = ''
                if type(pastHistory['pastHistoryDate']) == NoneType:
                    historyDate = pastHistory['pastHistoryDate']
                newHistory = Tbpasthistorylist(pastHistoryType = pastHistory['pastHistoryType'],
                                            pastHistoryCode = pastHistory['pastHistoryCode'],
                                            pastHistoryAdd = pastHistory['pastHistoryAdd'],
                                            pastHistoryDate = historyDate,
                                            tbhealthRecord = record)
                newHistory.save()
        except:
            print("no past history")
        return

    def create(self, validated_data):
        record = Tbhealthrecord.objects.create(**(validated_data[0]))
        self.saveCustomerKeys(record, self.context[0])
        return record

    def update(self, records, validated_data):
        print(validated_data)
        records.update(**(validated_data[0]))
        self.saveCustomerKeys(records[0], self.context[0])
        return records

class TbhealthrecordSeri(serializers.ModelSerializer):
    pastHistoryList = TbpasthistorylistSeri(many=True, read_only=True)
    personId = serializers.SerializerMethodField('getPersonIdFromHealthFileNum')
    responsibleDoctorCode = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    householdRegisterCode = serializers.SlugRelatedField(many=False, read_only=True, slug_field='areaCode')

    class Meta:
        list_serializer_class = HealthyRecordListSerializer
        model = Tbhealthrecord
        fields = ('personId', 'nowLiveCode', 'nowLiveName',
                  'nowLiveAddr', 'householdRegisterCode', 'householdRegisterName',
                  'householdRegisterAddr', 'registerOrgCode', 'registerDoctorCode',
                  'registerDoctorName', 'responsibleDoctorCode', 'registerDate',
                  'healthFileNumber', 'name', 'genderCode', 'birthday', 'idCard', 'workUnit',
                  'phone', 'contacts', 'contactsPhone', 'residentType', 'ethnicityCode',
                  'ethnicityName', 'bloodGroupCode', 'rhBloodGroupCode', 'eduBGCode',
                  'occupationCode', 'maritalStatusCode', 'paymentMethodCodes', 'paymentMethodOther',
                  'drugAllergyHistoryCodes', 'drugAllergyHistoryOther', 'exposureHistoryCodes',
                  'pastHistoryList', 'familyHistoryFatherCodes', 'familyHistoryFatherOther',
                  'familyHistoryMatherCodes', 'familyHistoryMatherOther', 'brotherAndSisterCodes',
                  'brotherAndSisterOther', 'familyHistoryChildrenCodes',
                  'familyHistoryChildrenOther', 'geneticHistoryCode', 'geneticHistoryOther',
                  'disabilityCodes', 'disabilityOther', 'kitchenExhaustCode', 'fuelTypeCode',
                  'waterCode', 'toiletCode', 'livestockColumnCode', 'machineCode', 'machineNo')

    def getPersonIdFromHealthFileNum(self, obj):
        #return obj.personProfile.id
        return obj.healthFileNumber


# Related to heal examination.
class TbhospitalizedhistorySeri(serializers.ModelSerializer):
    class Meta:
        model = Tbhospitalizedhistory
        fields = ('admissionDate', 'dischargeDate', 'reason', 'orgName', 'medicalRecordNumber')

class TbfamilybedhistorySeri(serializers.ModelSerializer):
    class Meta:
        model = Tbfamilybedhistory
        fields = ('admissionDate', 'dischargeDate', 'reason', 'orgName', 'medicalRecordNumber')

class TbmedicationlistSeri(serializers.ModelSerializer):
    class Meta:
        model = Tbmedicationlist
        fields = ('drugName', 'usage', 'reason', 'dosage', 'medicationTime', 'doseCode')

class TbvaccinationhistorySeri(serializers.ModelSerializer):
    class Meta:
        model = Tbvaccinationhistory
        fields = ('inoculationName', 'inoculationDate', 'orgName')

class HealexaminationListSerializer(serializers.ListSerializer):
    def saveCustomerKeys(self, record, xmlData):
        # Save profile object to 'personProfile' field.
#         personId = int(xmlData['personId'])
#         profile = UserProfile.objects.filter(id=personId)
#         if len(profile) != 0:
#             record.personProfile = profile[0]
            
        # Save org object to 'organization' field.
        try:
            orgCode = int(xmlData['orgCode'])
        except:
            print('no org code')
        else:
            org = Tbmedicalorganization.objects.filter(orgCode=orgCode)
            if len(org) != 0:
                record.organization = org[0]

        # Save doctor name to 'responsibleDoctorName' field.
        try:
            doctorId = int(xmlData['responsibleDoctorCode'])
            profile = UserProfile.objects.filter(id=doctorId)
            record.responsibleDoctorName = profile[0].__str__()
        except:
            print('no doctor id')
        
        # Save area object to 'areaCode' field.
        try:
            areaCode = xmlData['householdRegisterCode']
            area = Tbarea.objects.filter(areaCode=areaCode)
            if len(area) != 0:
                record.householdRegisterCode = area[0]
        except:
            print('no area code')
            
        record.save()
        print("save other table ok!")
        return
    
    def create(self, validated_data):
        record = Tbhealexamination.objects.create(**(validated_data[0]))
        self.saveCustomerKeys(record, self.context[0])
        return record

    def update(self, records, validated_data):
        records.update(**(validated_data[0]))
        self.saveCustomerKeys(records[0], self.context[0])
        return records


class TbhealexaminationSeri(serializers.ModelSerializer):
#     hospitalizedHistory = TbhospitalizedhistorySeri(many=True, read_only=True)
#     familyBedHistory = TbfamilybedhistorySeri(many=True, read_only=True)
#     medicationList = TbmedicationlistSeri(many=True, read_only=True)
#     vaccinationHistory = TbvaccinationhistorySeri(many=True, read_only=True)
    
    personId = serializers.SerializerMethodField('getPersonIdFromHealthFileNum')
    orgCode = serializers.SerializerMethodField('getOrgCode')
    responsibleDoctorCode = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    householdRegisterCode = serializers.SlugRelatedField(many=False, read_only=True, slug_field='areaCode')

    class Meta:
        model = Tbhealexamination
        list_serializer_class = HealexaminationListSerializer
        fields = ('businessKey', 'personId', 'healthFileNumber', 'name', 'examinationDate', 'orgCode',
                  'operatorCode', 'operatorName', 'operateTime', 'responsibleDoctorCode',
                  'responsibleDoctorName', 'symptomCodes', 'symptomOther', 'temperature',
                  'pulseRate', 'respiratoryRate', 'height', 'weight', 'bmi', 'waistline',
                  'leftSBP', 'leftDBP', 'rightSBP', 'rightDBP', 'theAgedStatus',
                  'selfCareAbilityCode', 'cognitiveFunction', 'cognitiveFunctionScore',
                  'emotionalState', 'emotionalStateScore', 'exerciseFrequencyCode',
                  'everyWorkoutTime', 'insistOnExerciseTime', 'exerciseMode', 'eatingHabitsCodes',
                  'smokingStatusCode', 'dailySmoking', 'smokingAge', 'smokingCessationAge',
                  'drinkingFrequencyCode', 'dailyDrinking', 'temperanceCode', 'temperanceAge',
                  'drinkingAge', 'whetherDrunk', 'alcoholTypeCodes', 'alcoholTypeOther',
                  'exposureStateCode', 'hazardousWork', 'workingTime', 'dust', 'dustProtective',
                  'dustProtectiveDesc', 'radiogen', 'radiogenProtective', 'radiogenProtectiveDesc',
                  'physical', 'physicalProtective', 'physicalProtectiveDesc', 'chemistry',
                  'chemistryProtective', 'chemistryProtectiveDesc', 'otherToxicant',
                  'otherProtective', 'otherProtectiveDesc', 'lipsCode', 'dentitionCodes',
                  'missingTeethLeftUp', 'missingTeethRightUp', 'missingTeethLeftDown',
                  'missingTeethRightDown', 'cariesLeftUp', 'cariesRightUp', 'cariesLeftDown',
                  'cariesRightDown', 'dentureLeftUp', 'dentureRightUp', 'dentureLeftDown',
                  'dentureRightDown', 'throatCode', 'visionRight', 'visionLeft',
                  'redressVisionRight', 'redressVisionLeft', 'hearingCode', 'motorFunctionCode',
                  'fundusCode', 'fundusAbnormal', 'skinCode', 'skinOther', 'scleraCode',
                  'scleraOther', 'lymphNodeCode', 'lymphNodeOther', 'barrelChestCode',
                  'breathSoundCode', 'breathSoundOther', 'raleCode', 'raleOther', 'heartRate',
                  'rhythmCode', 'cardiacSouffleCode', 'cardiacSouffleDesc', 'abdomenTendernessCode',
                  'abdomenTendernessDesc', 'abdomenMassCode', 'abdomenMassDesc', 'abdomenLiverCode',
                  'abdomenLiverDesc', 'abdomenSplenomegalyCode', 'abdomenSplenomegalyDesc',
                  'abdomenShiftingDullnessCode', 'abdomenShiftingDullnessDesc', 'dorsalisPedisPulseCode',
                  'analFingerCodes', 'breastCodes', 'breastDesc', 'vulvaCode', 'vulvaDesc',
                  'vaginaCode', 'vaginaDesc', 'cervixCode', 'cervixDesc', 'uterusCode', 'uterusDesc',
                  'uterineAccessoriesCode', 'uterineAccessoriesDesc', 'examinationOther', 'hemoglobin',
                  'leucocyte', 'platelet', 'bloodOther', 'urineProteinCode', 'urineSugarCode',
                  'urineKetoneCode', 'urineOccultBloodCode','urineOther', 'fastingPlasmaGlucose1',
                  'fastingPlasmaGlucose2', 'ECGCode', 'ECGDesc', 'ECGData', 'urineTraceAlbuminCode',
                  'fecalOccultBloodCode', 'glycatedHemoglobin', 'HBsAgCode', 'GPT', 'GOT', 'albumin',
                  'TBIL', 'DBIL', 'serumCreatinine','BUN', 'serumPotassiumConcentration',
                  'serumSodiumConcentration', 'TCHO', 'triglyceride', 'LDL', 'HDL', 'chestXRayCode',
                  'chestXRayDesc', 'BScanCode', 'BScanDesc', 'papSmearCode', 'papSmearDesc', 'checkOther', 
                  'flatAndQualityCode', 'qiDeficiencyCode', 'yangXuzhiCode', 'yinDeficiencyCode',
                  'phlegmDampnessQualityCode', 'hotAndHumidQualityCode', 'bloodStasisCode',
                  'qiStagnationCode', 'specialQualityCode', 'cerebrovascularCodes','cerebrovascularDesc',
                  'kidneyDiseaseCodes', 'kidneyDiseaseDesc','heartDiseaseCodes','heartDiseaseDesc',
                  'vascularDiseaseCodes','vascularDiseaseDesc','eyeDiseaseCodes', 'eyeDiseaseDesc',
                  'nerveSystemDiseaseCode', 'nerveSystemDiseaseDesc', 'otherSystemDiseaseCode',
                  'otherSystemDiseaseDesc' , 'healthEvaluationCode', 'diseaseName1', 'diseaseName2',
                  'diseaseName3', 'diseaseName4', 'healthGuidanceCodes','healthGuidanceDesc',
                  'riskFactorsCodes', 'weightReduction', 'vaccinationName', 'riskFactorsOther',
                  'householdRegisterCode', 'legEdemaCode', 'machineCode', 'machineNo')
        #'hospitalizedHistory', 'familyBedHistory', 'medicationList', 'vaccinationHistory'
        #
    def getPersonIdFromHealthFileNum(self, obj):
        #return obj.personProfile.id
        return obj.healthFileNumber
    def getOrgCode(self, obj):
        return obj.organization.orgCode

    
# Related to health measure.
class YTJMeasureListSerializer(serializers.ListSerializer):
    def saveCustomerKeys(self, record, xmlData):
        # Save profile object to 'personProfile' field.
        personId = int(xmlData['personId'])
        profile = UserProfile.objects.filter(id=personId)
        if len(profile) != 0:
            record.personProfile = profile[0]
        # Save doctor name to 'responsibleDoctorName' field.
        doctorId = int(xmlData['responsibleDoctorCode'])
        profile = UserProfile.objects.filter(id=doctorId)
        if len(profile) != 0:
            record.responsibleDoctorCode = profile[0]
        record.save()
        return
    
    def create(self, validated_data):
        record = YTJMeasure.objects.create(**(validated_data[0]))
        self.saveCustomerKeys(record, self.context[0])
        return record

    def update(self, records, validated_data):
        records.update(**(validated_data[0]))
        self.saveCustomerKeys(records[0], self.context[0])
        return records

class YTJMeasureSeri(serializers.ModelSerializer):
    personId = serializers.SerializerMethodField('getPersonIdFromProfile')
    responsibleDoctorCode = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        list_serializer_class = YTJMeasureListSerializer
        model = YTJMeasure
        fields = ('responsibleDoctorCode', 'personId', 'idCard', 'name', 'time', 'data')
        
    def getPersonIdFromProfile(self, obj):
        return obj.personProfile.id
