# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Dicmedicationlist(models.Model):
    drugCode = models.CharField(db_column='drugCode', max_length=22, blank=True, null=True)  # Field name made lowercase.
    drugName = models.CharField(db_column='drugName', max_length=32)  # Field name made lowercase.
    drugUsage = models.CharField(db_column='drugUsage', max_length=32)  # Field name made lowercase.
    drugUsageAdd = models.CharField(db_column='drugUsageAdd', max_length=32, blank=True, null=True)  # Field name made lowercase.
    drugDosage = models.CharField(db_column='drugDosage', max_length=32)  # Field name made lowercase.
    drugDosageAdd = models.CharField(db_column='drugDosageAdd', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DicMedicationList'


class Tbchildspecial(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    genderCode = models.CharField(db_column='genderCode', max_length=1)  # Field name made lowercase.
    birthday = models.DateField()
    householdRegister = models.CharField(db_column='householdRegister', max_length=60, blank=True, null=True)  # Field name made lowercase.
    childHealthCardNo = models.CharField(db_column='childHealthCardNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    homeAddress = models.CharField(db_column='homeAddress', max_length=60, blank=True, null=True)  # Field name made lowercase.
    birthWeight = models.DecimalField(db_column='birthWeight', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    birthHeight = models.DecimalField(db_column='birthHeight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    parity = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    deliveryTimes = models.DecimalField(db_column='deliveryTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deliveryGestationalWeeks = models.DecimalField(db_column='deliveryGestationalWeeks', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deliveryModeCode = models.CharField(db_column='deliveryModeCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    childbirth = models.CharField(max_length=100, blank=True, null=True)
    birthHospital = models.CharField(db_column='birthHospital', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fatherName = models.CharField(db_column='fatherName', max_length=20)  # Field name made lowercase.
    motherName = models.CharField(db_column='motherName', max_length=20)  # Field name made lowercase.
    fatherContac = models.CharField(db_column='fatherContac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    motherContac = models.CharField(db_column='motherContac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    UNHSCode = models.CharField(db_column='UNHSCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CYP17Code = models.CharField(db_column='CYP17Code', max_length=1, blank=True, null=True)  # Field name made lowercase.
    PKUCode = models.CharField(db_column='PKUCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CHCode = models.CharField(db_column='CHCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    highRiskCode = models.CharField(db_column='highRiskCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    highRiskFactors = models.CharField(db_column='highRiskFactors', max_length=500, blank=True, null=True)  # Field name made lowercase.
    apgar1 = models.SmallIntegerField(blank=True, null=True)
    apgar5 = models.SmallIntegerField(blank=True, null=True)
    apgar10 = models.SmallIntegerField(blank=True, null=True)
    pastHistory = models.CharField(db_column='pastHistory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    allergicHistory = models.CharField(db_column='allergicHistory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    childbirthHospital = models.CharField(db_column='childbirthHospital', max_length=50, blank=True, null=True)  # Field name made lowercase.
    childbirthDoctor = models.CharField(db_column='childbirthDoctor', max_length=20, blank=True, null=True)  # Field name made lowercase.
    childbirthAssistant = models.CharField(db_column='childbirthAssistant', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registDate = models.DateField(db_column='registDate')  # Field name made lowercase.
    registerOrgCode = models.CharField(db_column='registerOrgCode', max_length=16)  # Field name made lowercase.
    registerOrgName = models.CharField(db_column='registerOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorCode = models.CharField(db_column='registerDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorName = models.CharField(db_column='registerDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbChildSpecial'


class Tbdiabetesflup(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    businessKey = models.CharField(db_column='businessKey', max_length=40, blank=True, null=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    healthFileNumber = models.CharField(db_column='healthFileNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    genderCode = models.CharField(db_column='genderCode', max_length=1)  # Field name made lowercase.
    flupData = models.DateField(db_column='flupData')  # Field name made lowercase.
    flupMode = models.CharField(db_column='flupMode', max_length=4)  # Field name made lowercase.
    symptomCodes = models.CharField(db_column='symptomCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    symptomOther = models.CharField(db_column='symptomOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField(db_column='SBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField(db_column='DBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    bloodPressureLevel = models.CharField(db_column='bloodPressureLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weightTarget = models.DecimalField(db_column='weightTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bmiTarget = models.DecimalField(db_column='bmiTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dorsalisPedisPulseCode = models.CharField(db_column='dorsalisPedisPulseCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    signsOther = models.CharField(db_column='signsOther', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dailySmoking = models.DecimalField(db_column='dailySmoking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailySmokingTarget = models.DecimalField(db_column='dailySmokingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinking = models.DecimalField(db_column='dailyDrinking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinkingTarget = models.DecimalField(db_column='dailyDrinkingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovement = models.DecimalField(db_column='perWeekMovement', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovementTarget = models.DecimalField(db_column='perWeekMovementTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimes = models.DecimalField(db_column='perWeekTimes', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimesTarget = models.DecimalField(db_column='perWeekTimesTarget', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    stapleFood = models.DecimalField(db_column='stapleFood', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    stapleFoodTarget = models.DecimalField(db_column='stapleFoodTarget', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    psychologicalCode = models.CharField(db_column='psychologicalCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    complianceCode = models.CharField(db_column='complianceCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fastingBloodGlucose = models.DecimalField(db_column='fastingBloodGlucose', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    HbA1c = models.DecimalField(db_column='HbA1c', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    aidCheckDate = models.DateField(db_column='aidCheckDate', blank=True, null=True)  # Field name made lowercase.
    aidCheck = models.CharField(db_column='aidCheck', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doseCode = models.CharField(db_column='doseCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lowBloodSugarCode = models.CharField(db_column='lowBloodSugarCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    adverseReactionCode = models.CharField(db_column='adverseReactionCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flupTypeCode = models.CharField(db_column='flupTypeCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    insulinMedicationtype = models.CharField(db_column='insulinMedicationtype', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insulinMedicationRate = models.CharField(db_column='insulinMedicationRate', max_length=1, blank=True, null=True)  # Field name made lowercase.
    insulinMedicationDose = models.DecimalField(db_column='insulinMedicationDose', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    medicationList = models.CharField(db_column='medicationList', max_length=10, blank=True, null=True)  # Field name made lowercase.
    referralReason = models.CharField(db_column='referralReason', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField(db_column='referralOrg', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralDepartment = models.CharField(db_column='referralDepartment', max_length=64, blank=True, null=True)  # Field name made lowercase.
    flupDoctorCode = models.CharField(db_column='flupDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupDoctorName = models.CharField(db_column='flupDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupOrgCode = models.CharField(db_column='flupOrgCode', max_length=16)  # Field name made lowercase.
    flupOrgName = models.CharField(db_column='flupOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField(db_column='nextFlupDate')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbDiabetesFlup'


class Tbdiabetesspecial(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    genderCode = models.CharField(db_column='genderCode', max_length=1)  # Field name made lowercase.
    SBP = models.DecimalField(db_column='SBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField(db_column='DBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    bloodPressureLevel = models.CharField(db_column='bloodPressureLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nextFlupData = models.DateField(db_column='nextFlupData')  # Field name made lowercase.
    diabetesLevelCode = models.CharField(db_column='diabetesLevelCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    caseType = models.CharField(db_column='caseType', max_length=1)  # Field name made lowercase.
    ICDCode = models.CharField(db_column='ICDCode', max_length=20)  # Field name made lowercase.
    doseCode = models.CharField(db_column='doseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    noMedicationCode = models.CharField(db_column='noMedicationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    drugCost = models.DecimalField(db_column='drugCost', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    familyHistoryCode = models.CharField(db_column='familyHistoryCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    randomBloodGlucose = models.DecimalField(db_column='randomBloodGlucose', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kidneyDiseaseYears = models.DecimalField(db_column='kidneyDiseaseYears', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    retinalDiseaseYears = models.DecimalField(db_column='retinalDiseaseYears', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    neuropathyYears = models.DecimalField(db_column='neuropathyYears', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vascularDiseaseYears = models.DecimalField(db_column='vascularDiseaseYears', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    skinInfectDiseaseYears = models.DecimalField(db_column='skinInfectDiseaseYears', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    noComplYears = models.DecimalField(db_column='noComplYears', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    complicationYears = models.DateField(db_column='complicationYears', blank=True, null=True)  # Field name made lowercase.
    initialDisease = models.CharField(db_column='initialDisease', max_length=60, blank=True, null=True)  # Field name made lowercase.
    currentDisease = models.CharField(db_column='currentDisease', max_length=60, blank=True, null=True)  # Field name made lowercase.
    caseSourceCode = models.CharField(db_column='caseSourceCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    caseSourceOther = models.CharField(db_column='caseSourceOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    registDate = models.DateField(db_column='registDate')  # Field name made lowercase.
    registerOrgCode = models.CharField(db_column='registerOrgCode', max_length=16)  # Field name made lowercase.
    registerOrgName = models.CharField(db_column='registerOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorCode = models.CharField(db_column='registerDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorName = models.CharField(db_column='registerDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    diagnoseDate = models.DateField(db_column='diagnoseDate')  # Field name made lowercase.
    diagnoseDoctorCode = models.CharField(db_column='diagnoseDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    diagnoseDoctorName = models.CharField(db_column='diagnoseDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbDiabetesSpecial'


class Tbhealthrecord(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    machineCode = models.CharField(db_column='machineCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    machineNo = models.CharField(db_column='machineNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nowLiveCode = models.CharField(db_column='nowLiveCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nowLiveName = models.CharField(db_column='nowLiveName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nowLiveAddr = models.CharField(db_column='nowLiveAddr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    householdRegisterCode = models.CharField(db_column='householdRegisterCode', max_length=18, blank=True, null=True)  # Field name made lowercase.
    householdRegisterName = models.CharField(db_column='householdRegisterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    householdRegisterAddr = models.CharField(db_column='householdRegisterAddr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    registerOrgCode = models.CharField(db_column='registerOrgCode', max_length=16)  # Field name made lowercase.
    registerDoctorCode = models.CharField(db_column='registerDoctorCode', max_length=20)  # Field name made lowercase.
    registerDoctorName = models.CharField(db_column='registerDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    responsibleDoctorCode = models.CharField(db_column='responsibleDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    responsibleDoctorName = models.CharField(db_column='responsibleDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDate = models.DateField(db_column='registerDate')  # Field name made lowercase.
    healthFileNumber = models.CharField(db_column='healthFileNumber', max_length=17)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    genderCode = models.CharField(db_column='genderCode', max_length=1)  # Field name made lowercase.
    birthday = models.DateField()
    idCard = models.CharField(db_column='idCard', max_length=18)  # Field name made lowercase.
    workUnit = models.CharField(db_column='workUnit', max_length=60, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=30, blank=True, null=True)
    contacts = models.CharField(max_length=20, blank=True, null=True)
    contactsPhone = models.CharField(db_column='contactsPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    residentType = models.CharField(db_column='residentType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ethnicityCode = models.CharField(db_column='ethnicityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ethnicityName = models.CharField(db_column='ethnicityName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bloodGroupCode = models.CharField(db_column='bloodGroupCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rhBloodGroupCode = models.CharField(db_column='rhBloodGroupCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    eduBGCode = models.CharField(db_column='eduBGCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    occupationCode = models.CharField(db_column='occupationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    maritalStatusCode = models.CharField(db_column='maritalStatusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    paymentMethodCodes = models.CharField(db_column='paymentMethodCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymentMethodOther = models.CharField(db_column='paymentMethodOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    drugAllergyHistoryCodes = models.CharField(db_column='drugAllergyHistoryCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    drugAllergyHistoryOther = models.CharField(db_column='drugAllergyHistoryOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    exposureHistoryCodes = models.CharField(db_column='exposureHistoryCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pastHistoryList = models.CharField(db_column='pastHistoryList', max_length=120, blank=True, null=True)  # Field name made lowercase.
    familyHistoryFatherCodes = models.CharField(db_column='familyHistoryFatherCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    familyHistoryFatherOther = models.CharField(db_column='familyHistoryFatherOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    familyHistoryMatherCodes = models.CharField(db_column='familyHistoryMatherCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    familyHistoryMatherOther = models.CharField(db_column='familyHistoryMatherOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    brotherAndSisterCodes = models.CharField(db_column='brotherAndSisterCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    brotherAndSisterOther = models.CharField(db_column='brotherAndSisterOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    familyHistoryChildrenCodes = models.CharField(db_column='familyHistoryChildrenCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    familyHistoryChildrenOther = models.CharField(db_column='familyHistoryChildrenOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    geneticHistoryCode = models.CharField(db_column='geneticHistoryCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    geneticHistoryOther = models.CharField(db_column='geneticHistoryOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    disabilityCodes = models.CharField(db_column='disabilityCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disabilityOther = models.CharField(db_column='disabilityOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    kitchenExhaustCode = models.CharField(db_column='kitchenExhaustCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fuelTypeCode = models.CharField(db_column='fuelTypeCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    waterCode = models.CharField(db_column='waterCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    toiletCode = models.CharField(db_column='toiletCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    livestockColumnCode = models.CharField(db_column='livestockColumnCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbHealthRecord'


class Tbhypertensionflup(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    businessKey = models.CharField(db_column='businessKey', max_length=40, blank=True, null=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    healthFileNumber = models.CharField(db_column='healthFileNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    genderCode = models.CharField(db_column='genderCode', max_length=1)  # Field name made lowercase.
    flupData = models.DateField(db_column='flupData')  # Field name made lowercase.
    flupMode = models.CharField(db_column='flupMode', max_length=4)  # Field name made lowercase.
    symptomCodes = models.CharField(db_column='symptomCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    symptomOther = models.CharField(db_column='symptomOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField(db_column='SBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField(db_column='DBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    bloodPressureLevel = models.CharField(db_column='bloodPressureLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    heartRate = models.DecimalField(db_column='heartRate', max_digits=4, decimal_places=0)  # Field name made lowercase.
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weightTarget = models.DecimalField(db_column='weightTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bmiTarget = models.DecimalField(db_column='bmiTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    signsOther = models.CharField(db_column='signsOther', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dailySmoking = models.DecimalField(db_column='dailySmoking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailySmokingTarget = models.DecimalField(db_column='dailySmokingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinkingTarget = models.DecimalField(db_column='dailyDrinkingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinking = models.DecimalField(db_column='dailyDrinking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovement = models.DecimalField(db_column='perWeekMovement', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovementTarget = models.DecimalField(db_column='perWeekMovementTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimes = models.DecimalField(db_column='perWeekTimes', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimesTarget = models.DecimalField(db_column='perWeekTimesTarget', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    saltIntakeCode = models.CharField(db_column='saltIntakeCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    saltIntakeTargetCode = models.CharField(db_column='saltIntakeTargetCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    psychologicalCode = models.CharField(db_column='psychologicalCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    complianceCode = models.CharField(db_column='complianceCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aidCheck = models.CharField(db_column='aidCheck', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doseCode = models.CharField(db_column='doseCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    adverseReactionCode = models.CharField(db_column='adverseReactionCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flupTypeCode = models.CharField(db_column='flupTypeCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    medicationList = models.CharField(db_column='medicationList', max_length=10, blank=True, null=True)  # Field name made lowercase.
    referralReason = models.CharField(db_column='referralReason', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField(db_column='referralOrg', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralDepartment = models.CharField(db_column='referralDepartment', max_length=64, blank=True, null=True)  # Field name made lowercase.
    flupDoctorCode = models.CharField(db_column='flupDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupDoctorName = models.CharField(db_column='flupDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupOrgCode = models.CharField(db_column='flupOrgCode', max_length=16)  # Field name made lowercase.
    flupOrgName = models.CharField(db_column='flupOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField(db_column='nextFlupDate')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbHypertensionFlup'


class Tbhypertensionspecial(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    genderCode = models.CharField(db_column='genderCode', max_length=1)  # Field name made lowercase.
    SBP = models.DecimalField(db_column='SBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField(db_column='DBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    bloodPressureLevel = models.CharField(db_column='bloodPressureLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nextFlupData = models.DateField(db_column='nextFlupData')  # Field name made lowercase.
    registDate = models.DateField(db_column='registDate')  # Field name made lowercase.
    registerOrgCode = models.CharField(db_column='registerOrgCode', max_length=16)  # Field name made lowercase.
    registerOrgName = models.CharField(db_column='registerOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorCode = models.CharField(db_column='registerDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorName = models.CharField(db_column='registerDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.
    diagnoseDate = models.DateField(db_column='diagnoseDate')  # Field name made lowercase.
    diagnoseDoctorCode = models.CharField(db_column='diagnoseDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    diagnoseDoctorName = models.CharField(db_column='diagnoseDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbHypertensionSpecial'


class Tbpostpartum42Visit(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    pregnantManualNo = models.CharField(db_column='pregnantManualNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    healthDesc = models.CharField(db_column='healthDesc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    psychologicStatus = models.CharField(db_column='psychologicStatus', max_length=250, blank=True, null=True)  # Field name made lowercase.
    flupDate = models.DateField(db_column='flupDate', blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField(db_column='SBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField(db_column='DBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    breastCode = models.CharField(db_column='breastCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    breastDesc = models.CharField(db_column='breastDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lochiaCode = models.CharField(db_column='lochiaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lochiaDesc = models.CharField(db_column='lochiaDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uterusCode = models.CharField(db_column='uterusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uterustDesc = models.CharField(db_column='uterustDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    woundCode = models.CharField(db_column='woundCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    woundDesc = models.CharField(db_column='woundDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(max_length=100, blank=True, null=True)
    typeCode = models.CharField(db_column='typeCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    typeDesc = models.CharField(db_column='typeDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    processCode = models.CharField(db_column='processCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guildCodes = models.CharField(db_column='guildCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    guildOther = models.CharField(db_column='guildOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralCode = models.CharField(db_column='referralCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    referralReason = models.CharField(db_column='referralReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField(db_column='referralOrg', max_length=50, blank=True, null=True)  # Field name made lowercase.
    referralDeparment = models.CharField(db_column='referralDeparment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visitDoctorCode = models.CharField(db_column='visitDoctorCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    visitDoctorName = models.CharField(db_column='visitDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    visitOrgCode = models.CharField(db_column='visitOrgCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    visitOrgName = models.CharField(db_column='visitOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField(db_column='nextFlupDate', blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbPostpartum42Visit'


class Tbpostpartumvisit(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    pregnantManualNo = models.CharField(db_column='pregnantManualNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    healthDesc = models.CharField(db_column='healthDesc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    psychologicStatus = models.CharField(db_column='psychologicStatus', max_length=250, blank=True, null=True)  # Field name made lowercase.
    flupDate = models.DateField(db_column='flupDate', blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField(db_column='SBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    breastCode = models.CharField(db_column='breastCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    breastDesc = models.CharField(db_column='breastDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lochiaCode = models.CharField(db_column='lochiaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(max_length=100, blank=True, null=True)
    DBP = models.DecimalField(db_column='DBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    typeCode = models.CharField(db_column='typeCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    typeDesc = models.CharField(db_column='typeDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    guildCodes = models.CharField(db_column='guildCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    guildOther = models.CharField(db_column='guildOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralCode = models.CharField(db_column='referralCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    referralReason = models.CharField(db_column='referralReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField(db_column='referralOrg', max_length=50, blank=True, null=True)  # Field name made lowercase.
    referralDeparment = models.CharField(db_column='referralDeparment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visitDoctorCode = models.CharField(db_column='visitDoctorCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    visitDoctorName = models.CharField(db_column='visitDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    visitOrgCode = models.CharField(db_column='visitOrgCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    visitOrgName = models.CharField(db_column='visitOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField(db_column='nextFlupDate', blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.
    uterusCode = models.CharField(db_column='uterusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    woundCode = models.CharField(db_column='woundCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lochiaDesc = models.CharField(db_column='lochiaDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uterustDesc = models.CharField(db_column='uterustDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    woundDesc = models.CharField(db_column='woundDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbPostpartumVisit'


class Tbpregnantfirstcheck(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    pregnantManualNo = models.CharField(db_column='pregnantManualNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    age = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Column_35 = models.CharField(db_column='Column_35', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vaginalDeliveryTimes = models.DecimalField(db_column='vaginalDeliveryTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    husbandPhone = models.CharField(db_column='husbandPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gestationWeeks = models.CharField(db_column='gestationWeeks', max_length=10, blank=True, null=True)  # Field name made lowercase.
    highRiskCode = models.CharField(db_column='highRiskCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gravidityTimes = models.DecimalField(db_column='gravidityTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    genderCode = models.CharField(db_column='genderCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visitStatus = models.CharField(db_column='visitStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    caesareanSectionTimes = models.DecimalField(db_column='caesareanSectionTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    highRiskFactors = models.CharField(db_column='highRiskFactors', max_length=500, blank=True, null=True)  # Field name made lowercase.
    deliveryTimes = models.DecimalField(db_column='deliveryTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    highRiskScore = models.DecimalField(db_column='highRiskScore', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    husbandAge = models.DecimalField(db_column='husbandAge', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    checkStatus = models.CharField(db_column='checkStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visit42Status = models.CharField(db_column='visit42Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    LMP = models.DateField(db_column='LMP')  # Field name made lowercase.
    husbandName = models.CharField(db_column='husbandName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expectedBirthDate = models.DateField(db_column='expectedBirthDate', blank=True, null=True)  # Field name made lowercase.
    pastHistoryCodes = models.CharField(db_column='pastHistoryCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pastHistoryOthers = models.CharField(db_column='pastHistoryOthers', max_length=100, blank=True, null=True)  # Field name made lowercase.
    familyHistoryCodes = models.CharField(db_column='familyHistoryCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    familyHistoryOther = models.CharField(db_column='familyHistoryOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    personalHistoryCodes = models.CharField(db_column='personalHistoryCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    personalHistoryOther = models.CharField(db_column='personalHistoryOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    surgeryHistoryCode = models.CharField(db_column='surgeryHistoryCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    surgeryHistoryOther = models.CharField(db_column='surgeryHistoryOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abortionTimes = models.DecimalField(db_column='abortionTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    stillbirthTimes = models.DecimalField(db_column='stillbirthTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deadbirthTime = models.DecimalField(db_column='deadbirthTime', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    neonatalDeath = models.DecimalField(db_column='neonatalDeath', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    birthDefects = models.DecimalField(db_column='birthDefects', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    SBP = models.DecimalField(db_column='SBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField(db_column='DBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    cardiacAuscultationCode = models.CharField(db_column='cardiacAuscultationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cardiacAuscultationDesc = models.CharField(db_column='cardiacAuscultationDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lungAuscultationCode = models.CharField(db_column='lungAuscultationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lungAuscultationDesc = models.CharField(db_column='lungAuscultationDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vulvaCode = models.CharField(db_column='vulvaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vulvaDesc = models.CharField(db_column='vulvaDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vaginCode = models.CharField(db_column='vaginCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vaginDesc = models.CharField(db_column='vaginDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cervixCode = models.CharField(db_column='cervixCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cervixDesc = models.CharField(db_column='cervixDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uterusCode = models.CharField(db_column='uterusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uterusDesc = models.CharField(db_column='uterusDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uterineAccessoriesCode = models.CharField(db_column='uterineAccessoriesCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uterineAccessoriesDesc = models.CharField(db_column='uterineAccessoriesDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hemoglobin = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    leucocy = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bloodOther = models.CharField(db_column='bloodOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    urineProteinCode = models.CharField(db_column='urineProteinCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineSugarCode = models.CharField(db_column='urineSugarCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineKetoneCode = models.CharField(db_column='urineKetoneCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineOccultBloodCode = models.CharField(db_column='urineOccultBloodCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineOther = models.CharField(db_column='urineOther', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bloodGroupCode = models.CharField(db_column='bloodGroupCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rhBloodGroupCode = models.CharField(db_column='rhBloodGroupCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bloodGlucose = models.DecimalField(db_column='bloodGlucose', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    GPT = models.DecimalField(db_column='GPT', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    GOT = models.DecimalField(db_column='GOT', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    albumin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    TBIL = models.DecimalField(db_column='TBIL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    DBIL = models.DecimalField(db_column='DBIL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    serumCreatinine = models.DecimalField(db_column='serumCreatinine', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    BUN = models.DecimalField(db_column='BUN', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vaginalFluidCodes = models.CharField(db_column='vaginalFluidCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vaginalFluidOther = models.CharField(db_column='vaginalFluidOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vaginalCleanlinessCode = models.CharField(db_column='vaginalCleanlinessCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    HBsAgCode = models.CharField(db_column='HBsAgCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    antiHBsCode = models.CharField(db_column='antiHBsCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    HBeAgCode = models.CharField(db_column='HBeAgCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    HBeAbCode = models.CharField(db_column='HBeAbCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    HBcAbCode = models.CharField(db_column='HBcAbCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    syphilisCode = models.CharField(db_column='syphilisCode', max_length=1)  # Field name made lowercase.
    HIV = models.CharField(db_column='HIV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    BScan = models.CharField(db_column='BScan', max_length=100, blank=True, null=True)  # Field name made lowercase.
    overallAssessmentCode = models.CharField(db_column='overallAssessmentCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    healthGuildCodes = models.CharField(db_column='healthGuildCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    healthGuildOther = models.CharField(db_column='healthGuildOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralCode = models.CharField(db_column='referralCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    referralReason = models.CharField(db_column='referralReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField(db_column='referralOrg', max_length=50, blank=True, null=True)  # Field name made lowercase.
    referralDeparment = models.CharField(db_column='referralDeparment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    checkDoctorCode = models.CharField(db_column='checkDoctorCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    checkDoctorName = models.CharField(db_column='checkDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    checkOrgCode = models.CharField(db_column='checkOrgCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    checkOrgName = models.CharField(db_column='checkOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField(db_column='nextFlupDate', blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbPregnantFirstCheck'


class Tbpregnantrecheck(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    pregnantManualNo = models.CharField(db_column='pregnantManualNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    age = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gestationWeeks = models.DecimalField(db_column='gestationWeeks', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    genderCode = models.CharField(db_column='genderCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    antenatalCareDate = models.DateField(db_column='antenatalCareDate', blank=True, null=True)  # Field name made lowercase.
    chiefComplaint = models.CharField(db_column='chiefComplaint', max_length=250)  # Field name made lowercase.
    weight = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    fundusHeight = models.DecimalField(db_column='fundusHeight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    abdominalCircumference = models.DecimalField(db_column='abdominalCircumference', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foetalCirculationCode = models.CharField(db_column='foetalCirculationCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fetalHeartRate = models.CharField(db_column='fetalHeartRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField(db_column='SBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField(db_column='DBP', max_digits=4, decimal_places=0)  # Field name made lowercase.
    hemoglobin = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    leucocyte = models.CharField(max_length=1, blank=True, null=True)
    checkOther = models.CharField(db_column='checkOther', max_length=250, blank=True, null=True)  # Field name made lowercase.
    typeCode = models.CharField(db_column='typeCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    typeDesc = models.CharField(db_column='typeDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    GuildCodes = models.CharField(db_column='GuildCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    GuildOther = models.CharField(db_column='GuildOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralCode = models.CharField(db_column='referralCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    referralReason = models.CharField(db_column='referralReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField(db_column='referralOrg', max_length=50, blank=True, null=True)  # Field name made lowercase.
    referralDeparment = models.CharField(db_column='referralDeparment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    checkDoctorCode = models.CharField(db_column='checkDoctorCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    checkDoctorName = models.CharField(db_column='checkDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    checkOrgCode = models.CharField(db_column='checkOrgCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    checkOrgName = models.CharField(db_column='checkOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField(db_column='nextFlupDate', blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbPregnantRecheck'


class Tbpregnantspecial(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=40)  # Field name made lowercase.
    specialNo = models.CharField(db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField(db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField(db_column='mechineNo', max_length=40)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    husbandPhone = models.CharField(db_column='husbandPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gravidityTimes = models.DecimalField(db_column='gravidityTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    caesareanSectionTimes = models.DecimalField(db_column='caesareanSectionTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pregnantManualNo = models.CharField(db_column='pregnantManualNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    age = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    highRiskCode = models.CharField(db_column='highRiskCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    highRiskFactors = models.CharField(db_column='highRiskFactors', max_length=500, blank=True, null=True)  # Field name made lowercase.
    highRiskScore = models.DecimalField(db_column='highRiskScore', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    husbandAge = models.DecimalField(db_column='husbandAge', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    checkStatus = models.CharField(db_column='checkStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vaginalDeliveryTimes = models.DecimalField(db_column='vaginalDeliveryTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    LMP = models.DateField(db_column='LMP')  # Field name made lowercase.
    husbandName = models.CharField(db_column='husbandName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    genderCode = models.CharField(db_column='genderCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visitStatus = models.CharField(db_column='visitStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visit42Status = models.CharField(db_column='visit42Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    registDate = models.DateField(db_column='registDate')  # Field name made lowercase.
    registerOrgCode = models.CharField(db_column='registerOrgCode', max_length=16)  # Field name made lowercase.
    registerOrgName = models.CharField(db_column='registerOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorCode = models.CharField(db_column='registerDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorName = models.CharField(db_column='registerDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbPregnantSpecial'


class Tbfamilybedhistory(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    admissionDate = models.DateField(db_column='admissionDate', blank=True, null=True)  # Field name made lowercase.
    dischargeDate = models.DateField(db_column='dischargeDate', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=100, blank=True, null=True)
    orgName = models.CharField(db_column='orgName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    medicalRecordNumber = models.CharField(db_column='medicalRecordNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbfamilyBedHistory'


class Tbhealexamination(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    householdRegisterCode = models.CharField(db_column='householdRegisterCode', max_length=18)  # Field name made lowercase.
    orgCode = models.CharField(db_column='orgCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    healthFileNumber = models.CharField(db_column='healthFileNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20, blank=True, null=True)
    genderCode = models.CharField(db_column='genderCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    personId = models.CharField(db_column='personId', max_length=18, blank=True, null=True)  # Field name made lowercase.
    machineCode = models.CharField(db_column='machineCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    businessKey = models.CharField(db_column='businessKey', max_length=40, blank=True, null=True)  # Field name made lowercase.
    examinationDate = models.DateField(db_column='examinationDate', blank=True, null=True)  # Field name made lowercase.
    operatorName = models.CharField(db_column='operatorName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    operatorCode = models.CharField(db_column='operatorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operateTime = models.DateField(db_column='operateTime', blank=True, null=True)  # Field name made lowercase.
    responsibleDoctorCode = models.CharField(db_column='responsibleDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    responsibleDoctorName = models.CharField(db_column='responsibleDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    symptomCodes = models.CharField(db_column='symptomCodes', max_length=60, blank=True, null=True)  # Field name made lowercase.
    symptomOther = models.CharField(db_column='symptomOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pulseRate = models.DecimalField(db_column='pulseRate', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    respiratoryRate = models.DecimalField(db_column='respiratoryRate', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    weight = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    waistline = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    leftSBP = models.DecimalField(db_column='leftSBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    leftDBP = models.DecimalField(db_column='leftDBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rightSBP = models.DecimalField(db_column='rightSBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rightDBP = models.DecimalField(db_column='rightDBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    theAgedStatus = models.CharField(db_column='theAgedStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    selfCareAbilityCode = models.CharField(db_column='selfCareAbilityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cognitiveFunction = models.CharField(db_column='cognitiveFunction', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cognitiveFunctionScore = models.DecimalField(db_column='cognitiveFunctionScore', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    emotionalState = models.CharField(db_column='emotionalState', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emotionalStateScore = models.DecimalField(db_column='emotionalStateScore', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    exerciseFrequencyCode = models.CharField(db_column='exerciseFrequencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    everyWorkoutTime = models.CharField(db_column='everyWorkoutTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    insistOnExerciseTime = models.CharField(db_column='insistOnExerciseTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    exerciseMode = models.CharField(db_column='exerciseMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eatingHabitsCodes = models.CharField(db_column='eatingHabitsCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    smokingStatusCode = models.CharField(db_column='smokingStatusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dailySmoking = models.DecimalField(db_column='dailySmoking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smokingAge = models.DecimalField(db_column='smokingAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smokingCessationAge = models.DecimalField(db_column='smokingCessationAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    drinkingFrequencyCode = models.CharField(db_column='drinkingFrequencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dailyDrinking = models.DecimalField(db_column='dailyDrinking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    temperanceCode = models.CharField(db_column='temperanceCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    temperanceAge = models.DecimalField(db_column='temperanceAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    drinkingAge = models.DecimalField(db_column='drinkingAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    whetherDrunk = models.CharField(db_column='whetherDrunk', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alcoholTypeCodes = models.CharField(db_column='alcoholTypeCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alcoholTypeOther = models.CharField(db_column='alcoholTypeOther', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exposureStateCode = models.CharField(db_column='exposureStateCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hazardousWork = models.CharField(db_column='hazardousWork', max_length=60, blank=True, null=True)  # Field name made lowercase.
    workingTime = models.DecimalField(db_column='workingTime', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dust = models.CharField(max_length=50, blank=True, null=True)
    dustProtective = models.CharField(db_column='dustProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dustProtectiveDesc = models.CharField(db_column='dustProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    radiogen = models.CharField(max_length=50, blank=True, null=True)
    radiogenProtective = models.CharField(db_column='radiogenProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    radiogenProtectiveDesc = models.CharField(db_column='radiogenProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    physical = models.CharField(max_length=50, blank=True, null=True)
    physicalProtective = models.CharField(db_column='physicalProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    physicalProtectiveDesc = models.CharField(db_column='physicalProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.CharField(max_length=50, blank=True, null=True)
    chemistryProtective = models.CharField(db_column='chemistryProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chemistryProtectiveDesc = models.CharField(db_column='chemistryProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    otherToxicant = models.CharField(db_column='otherToxicant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otherProtective = models.CharField(db_column='otherProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    otherProtectiveDesc = models.CharField(db_column='otherProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    lipsCode = models.CharField(db_column='lipsCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dentitionCodes = models.CharField(db_column='dentitionCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    missingTeethLeftUp = models.CharField(db_column='missingTeethLeftUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    missingTeethRightUp = models.CharField(db_column='missingTeethRightUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    missingTeethLeftDown = models.CharField(db_column='missingTeethLeftDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    missingTeethRightDown = models.CharField(db_column='missingTeethRightDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesLeftUp = models.CharField(db_column='cariesLeftUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesRightUp = models.CharField(db_column='cariesRightUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesLeftDown = models.CharField(db_column='cariesLeftDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesRightDown = models.CharField(db_column='cariesRightDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureLeftUp = models.CharField(db_column='dentureLeftUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureRightUp = models.CharField(db_column='dentureRightUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureLeftDown = models.CharField(db_column='dentureLeftDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureRightDown = models.CharField(db_column='dentureRightDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    throatCode = models.CharField(db_column='throatCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visionRight = models.CharField(db_column='visionRight', max_length=12, blank=True, null=True)  # Field name made lowercase.
    visionLeft = models.CharField(db_column='visionLeft', max_length=12, blank=True, null=True)  # Field name made lowercase.
    redressVisionRight = models.CharField(db_column='redressVisionRight', max_length=12, blank=True, null=True)  # Field name made lowercase.
    redressVisionLeft = models.CharField(db_column='redressVisionLeft', max_length=12, blank=True, null=True)  # Field name made lowercase.
    hearingCode = models.CharField(db_column='hearingCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motorFunctionCode = models.CharField(db_column='motorFunctionCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fundusCode = models.CharField(db_column='fundusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fundusAbnormal = models.CharField(db_column='fundusAbnormal', max_length=60, blank=True, null=True)  # Field name made lowercase.
    skinCode = models.CharField(db_column='skinCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    skinOther = models.CharField(db_column='skinOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    scleraCode = models.CharField(db_column='scleraCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    scleraOther = models.CharField(db_column='scleraOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    lymphNodeCode = models.CharField(db_column='lymphNodeCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lymphNodeOther = models.CharField(db_column='lymphNodeOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    barrelChestCode = models.CharField(db_column='barrelChestCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    breathSoundCode = models.CharField(db_column='breathSoundCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    breathSoundOther = models.CharField(db_column='breathSoundOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    raleCode = models.CharField(db_column='raleCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    raleOther = models.CharField(db_column='raleOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    heartRate = models.DecimalField(db_column='heartRate', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rhythmCode = models.CharField(db_column='rhythmCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cardiacSouffleCode = models.CharField(db_column='cardiacSouffleCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cardiacSouffleDesc = models.CharField(db_column='cardiacSouffleDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenTendernessCode = models.CharField(db_column='abdomenTendernessCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenTendernessDesc = models.CharField(db_column='abdomenTendernessDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenMassCode = models.CharField(db_column='abdomenMassCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenMassDesc = models.CharField(db_column='abdomenMassDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenLiverCode = models.CharField(db_column='abdomenLiverCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenLiverDesc = models.CharField(db_column='abdomenLiverDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenSplenomegalyCode = models.CharField(db_column='abdomenSplenomegalyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenSplenomegalyDesc = models.CharField(db_column='abdomenSplenomegalyDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenShiftingDullnessCode = models.CharField(db_column='abdomenShiftingDullnessCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenShiftingDullnessDesc = models.CharField(db_column='abdomenShiftingDullnessDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    legEdemaCode = models.CharField(db_column='legEdemaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dorsalisPedisPulseCode = models.CharField(db_column='dorsalisPedisPulseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    analFingerCodes = models.CharField(db_column='analFingerCodes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    breastCodes = models.CharField(db_column='breastCodes', max_length=32, blank=True, null=True)  # Field name made lowercase.
    breastDesc = models.CharField(db_column='breastDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    vulvaCode = models.CharField(db_column='vulvaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vulvaDesc = models.CharField(db_column='vulvaDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    vaginaCode = models.CharField(db_column='vaginaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vaginaDesc = models.CharField(db_column='vaginaDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cervixCode = models.CharField(db_column='cervixCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cervixDesc = models.CharField(db_column='cervixDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    uterusCode = models.CharField(db_column='uterusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uterusDesc = models.CharField(db_column='uterusDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    uterineAccessoriesCode = models.CharField(db_column='uterineAccessoriesCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uterineAccessoriesDesc = models.CharField(db_column='uterineAccessoriesDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    examinationOther = models.CharField(db_column='examinationOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hemoglobin = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    leucocyte = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    platelet = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bloodOther = models.CharField(db_column='bloodOther', max_length=128, blank=True, null=True)  # Field name made lowercase.
    urineProteinCode = models.CharField(db_column='urineProteinCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineSugarCode = models.CharField(db_column='urineSugarCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineKetoneCode = models.CharField(db_column='urineKetoneCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineOccultBloodCode = models.CharField(db_column='urineOccultBloodCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineOther = models.CharField(db_column='urineOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fastingPlasmaGlucose1 = models.DecimalField(db_column='fastingPlasmaGlucose1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fastingPlasmaGlucose2 = models.DecimalField(db_column='fastingPlasmaGlucose2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ECGCode = models.CharField(db_column='ECGCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ECGDesc = models.CharField(db_column='ECGDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    ECGData = models.TextField(db_column='ECGData', blank=True, null=True)  # Field name made lowercase.
    urineTraceAlbuminCode = models.CharField(db_column='urineTraceAlbuminCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    fecalOccultBloodCode = models.CharField(db_column='fecalOccultBloodCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    glycatedHemoglobin = models.CharField(db_column='glycatedHemoglobin', max_length=16, blank=True, null=True)  # Field name made lowercase.
    HBsAgCode = models.CharField(db_column='HBsAgCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    GPT = models.DecimalField(db_column='GPT', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    GOT = models.DecimalField(db_column='GOT', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    albumin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    TBIL = models.DecimalField(db_column='TBIL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    DBIL = models.DecimalField(db_column='DBIL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    serumCreatinine = models.DecimalField(db_column='serumCreatinine', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    BUN = models.DecimalField(db_column='BUN', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    serumPotassiumConcentration = models.DecimalField(db_column='serumPotassiumConcentration', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    serumSodiumConcentration = models.DecimalField(db_column='serumSodiumConcentration', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    TCHO = models.DecimalField(db_column='TCHO', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    triglyceride = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    LDL = models.DecimalField(db_column='LDL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    HDL = models.DecimalField(db_column='HDL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chestXRayCode = models.CharField(db_column='chestXRayCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chestXRayDesc = models.CharField(db_column='chestXRayDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    BScanCode = models.CharField(db_column='BScanCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    BScanDesc = models.CharField(db_column='BScanDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    papSmearCode = models.CharField(db_column='papSmearCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    papSmearDesc = models.CharField(db_column='papSmearDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    checkOther = models.CharField(db_column='checkOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    flatAndQualityCode = models.CharField(db_column='flatAndQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qiDeficiencyCode = models.CharField(db_column='qiDeficiencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yangXuzhiCode = models.CharField(db_column='yangXuzhiCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yinDeficiencyCode = models.CharField(db_column='yinDeficiencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    phlegmDampnessQualityCode = models.CharField(db_column='phlegmDampnessQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hotAndHumidQualityCode = models.CharField(db_column='hotAndHumidQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bloodStasisCode = models.CharField(db_column='bloodStasisCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qiStagnationCode = models.CharField(db_column='qiStagnationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    specialQualityCode = models.CharField(db_column='specialQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cerebrovascularCodes = models.CharField(db_column='cerebrovascularCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cerebrovascularDesc = models.CharField(db_column='cerebrovascularDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    kidneyDiseaseCodes = models.CharField(db_column='kidneyDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kidneyDiseaseDesc = models.CharField(db_column='kidneyDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    heartDiseaseCodes = models.CharField(db_column='heartDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    heartDiseaseDesc = models.CharField(db_column='heartDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    vascularDiseaseCodes = models.CharField(db_column='vascularDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vascularDiseaseDesc = models.CharField(db_column='vascularDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    eyeDiseaseCodes = models.CharField(db_column='eyeDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eyeDiseaseDesc = models.CharField(db_column='eyeDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    nerveSystemDiseaseCode = models.CharField(db_column='nerveSystemDiseaseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nerveSystemDiseaseDesc = models.CharField(db_column='nerveSystemDiseaseDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    otherSystemDiseaseCode = models.CharField(db_column='otherSystemDiseaseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    otherSystemDiseaseDesc = models.CharField(db_column='otherSystemDiseaseDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    hospitalizedHistory = models.TextField(db_column='hospitalizedHistory', blank=True, null=True)  # Field name made lowercase.
    familyBedHistory = models.TextField(db_column='familyBedHistory', blank=True, null=True)  # Field name made lowercase.
    medicationList = models.TextField(db_column='medicationList', blank=True, null=True)  # Field name made lowercase.
    vaccinationHistory = models.TextField(db_column='vaccinationHistory', blank=True, null=True)  # Field name made lowercase.
    healthEvaluationCode = models.CharField(db_column='healthEvaluationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    diseaseName1 = models.CharField(db_column='diseaseName1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    diseaseName2 = models.CharField(db_column='diseaseName2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    diseaseName3 = models.CharField(db_column='diseaseName3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    diseaseName4 = models.CharField(db_column='diseaseName4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    healthGuidanceCodes = models.CharField(db_column='healthGuidanceCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    healthGuidanceDesc = models.CharField(db_column='healthGuidanceDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    riskFactorsCodes = models.CharField(db_column='riskFactorsCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weightReduction = models.CharField(db_column='weightReduction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vaccinationName = models.CharField(db_column='vaccinationName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    riskFactorsOther = models.CharField(db_column='riskFactorsOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbhealExamination'


class Tbhospitalizedhistory(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    admissionDate = models.DateField(db_column='admissionDate', blank=True, null=True)  # Field name made lowercase.
    dischargeDate = models.DateField(db_column='dischargeDate', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=100, blank=True, null=True)
    orgName = models.CharField(db_column='orgName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    medicalRecordNumber = models.CharField(db_column='medicalRecordNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbhospitalizedHistory'


class Tbmedicationlist(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    drugName = models.CharField(db_column='drugName', max_length=50)  # Field name made lowercase.
    usage = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    dosage = models.CharField(max_length=20, blank=True, null=True)
    medicationTime = models.CharField(db_column='medicationTime', max_length=120, blank=True, null=True)  # Field name made lowercase.
    doseCode = models.CharField(db_column='doseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser', max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime')  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbmedicationList'


class Tbpasthistorylist(models.Model):
   
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    pastHistoryType = models.CharField(db_column='pastHistoryType', max_length=1)  # Field name made lowercase.
    pastHistoryCode = models.CharField(db_column='pastHistoryCode', max_length=1)  # Field name made lowercase.
    pastHistoryAdd = models.CharField(db_column='pastHistoryAdd', max_length=122, blank=True, null=True)  # Field name made lowercase.
    pastHistoryDate = models.DateField(db_column='pastHistoryDate', blank=True, null=True)  # Field name made lowercase.  
    tbhealthRecord = models.ForeignKey(Tbhealthrecord,related_name='history_set')
    CreateUser = models.CharField(db_column='CreateUser',  blank=True, null=True,max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', blank=True, null=True, max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', blank=True, null=True, max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
#         managed = True
        db_table = 'TbpastHistoryList'


class Tbvaccinationhistory(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    inoculationName = models.CharField(db_column='inoculationName', max_length=120)  # Field name made lowercase.
    inoculationDate = models.DateField(db_column='inoculationDate', blank=True, null=True)  # Field name made lowercase.
    orgName = models.CharField(db_column='orgName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField(db_column='CreateUser',  blank=True, null=True,max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser',  blank=True, null=True,max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser',  blank=True, null=True,max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbvaccinationHistory'


class Tbarea(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    areaName = models.CharField(db_column='areaName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    areaCode = models.CharField(db_column='areaCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    areaType = models.IntegerField(db_column='areaType', blank=True, null=True)  # Field name made lowercase.
    parentAreaCode = models.CharField(db_column='parentAreaCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbArea'


class Tbbloodtype(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bloodGroupCode = models.CharField(db_column='bloodGroupCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    bloodGroupName = models.CharField(db_column='bloodGroupName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnabled = models.IntegerField(db_column='IsEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbBloodType'


class Tbbloodtype2(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    BloodName = models.CharField(db_column='BloodName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnabled = models.IntegerField(db_column='IsEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbBloodType2'


class Tbdenture(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Denture_Name = models.CharField(db_column='Denture_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbDenture'


class Tbdiabetescasessource(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    DCS_Name = models.CharField(db_column='DCS_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbDiabetesCasesSource'


class Tbdiabetesmanagementclassificat(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    DMC_Name = models.CharField(db_column='DMC_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbDiabetesManagementClassificat'


class Tbdiabetessymptom(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    DS_Name = models.CharField(db_column='DS_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbDiabetesSymptom'


class Tbdiabetestype(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    DT_Name = models.CharField(db_column='DT_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbDiabetesType'


class Tbdisabilitysituation(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    DS_Name = models.CharField(db_column='DS_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbDisabilitySituation'


class Tbdrugallergyhistory(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drugAllergyHistoryCodes = models.CharField(db_column='drugAllergyHistoryCodes', max_length=120, blank=True, null=True)  # Field name made lowercase.
    drugAllergyHistoryName = models.CharField(db_column='drugAllergyHistoryName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbDrugAllergyHistory'


class Tbedubg(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eduBGCode = models.CharField(db_column='eduBGCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    eduBGName = models.CharField(db_column='eduBGName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbEduBG'


class Tbethnicity(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ethnicityCode = models.CharField(db_column='ethnicityCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    ethnicityName = models.CharField(db_column='ethnicityName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbEthnicity'


class Tbfamilydiseaseshistory(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    FDH_Name = models.CharField(db_column='FDH_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbFamilyDiseasesHistory'


class Tbfilestatus(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    FS_Name = models.CharField(db_column='FS_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbFileStatus'


class Tbfueltypecode(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fuelTypeCode = models.CharField(db_column='fuelTypeCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fuelTypeName = models.CharField(db_column='fuelTypeName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbFuelTypeCode'


class Tbgender(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    genderCode = models.CharField(db_column='genderCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    genderName = models.CharField(db_column='genderName', max_length=1, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnabled = models.IntegerField(db_column='IsEnabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbGender'


class Tbgenetichistorycode(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    geneticHistoryCode = models.CharField(db_column='geneticHistoryCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    geneticHistoryName = models.CharField(db_column='geneticHistoryName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbGeneticHistoryCode'


class Tbhearing(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Hearing_Name = models.CharField(db_column='Hearing_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbHearing'


class Tbkitchenexhaustcode(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kitchenExhaustCode = models.CharField(db_column='kitchenExhaustCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    kitchenExhaustName = models.CharField(db_column='kitchenExhaustName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbKitchenExhaustCode'


class Tblip(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Lip_Name = models.CharField(db_column='Lip_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbLip'


class Tblivestockcolumncode(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    livestockColumnCode = models.CharField(db_column='livestockColumnCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    livestockColumnName = models.CharField(db_column='livestockColumnName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbLivestockColumnCode'


class Tbmaritalstatus(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    maritalStatusCode = models.CharField(db_column='maritalStatusCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    maritalStatusName = models.CharField(db_column='maritalStatusName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbMaritalStatus'


class Tbmedicalorganization(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orgCode = models.CharField(db_column='orgCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    orgName = models.CharField(db_column='orgName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    orgType = models.CharField(db_column='orgType', max_length=120, blank=True, null=True)  # Field name made lowercase.
    parentOrgCode = models.CharField(db_column='parentOrgCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    areaCode = models.CharField(db_column='areaCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    levelOrder = models.IntegerField(db_column='levelOrder', blank=True, null=True)  # Field name made lowercase.
    IsEnabled = models.CharField(db_column='IsEnabled', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbMedicalOrganization'


class Tbpaymentmethodcodes(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paymentMethodCode = models.CharField(db_column='paymentMethodCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    paymentMethodName = models.CharField(db_column='paymentMethodName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbPaymentMethodCodes'


class Tbperson(models.Model):
    PersonId = models.AutoField(db_column='PersonId', primary_key=True)  # Field name made lowercase.
    SpecialNO = models.CharField(db_column='SpecialNO', max_length=120, blank=True, null=True)  # Field name made lowercase.
    RegisterDate = models.DateField(db_column='RegisterDate', blank=True, null=True)  # Field name made lowercase.
    RegisterOrgCode = models.IntegerField(db_column='RegisterOrgCode', blank=True, null=True)  # Field name made lowercase.
    blank = models.IntegerField(db_column='....', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    genderCode = models.CharField(db_column='genderCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    idCard = models.CharField(db_column='idCard', max_length=120, blank=True, null=True)  # Field name made lowercase.
    healthFileNumber = models.CharField(db_column='healthFileNumber', max_length=120, blank=True, null=True)  # Field name made lowercase.
    ethnicityCode = models.CharField(db_column='ethnicityCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    orgCode = models.CharField(db_column='orgCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=120, blank=True, null=True)
    contacts = models.CharField(max_length=120, blank=True, null=True)
    contactsPhone = models.CharField(db_column='contactsPhone', max_length=120, blank=True, null=True)  # Field name made lowercase.
    workUnit = models.CharField(db_column='workUnit', max_length=120, blank=True, null=True)  # Field name made lowercase.
    waterCode = models.CharField(db_column='waterCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    livestockColumnCode = models.CharField(db_column='livestockColumnCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    toiletCode = models.CharField(db_column='toiletCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    kitchenExhaustCode = models.CharField(db_column='kitchenExhaustCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fuelTypeCode = models.CharField(db_column='fuelTypeCode', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbPerson'


class Tbpharyngeal(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Pharyngeal_Name = models.CharField(db_column='Pharyngeal_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbPharyngeal'


class Tbprofession(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Profession_Name = models.CharField(db_column='Profession_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbProfession'


class Tbresidencetype(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    RT_Name = models.CharField(db_column='RT_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbResidenceType'


class Tbrhbloodgrouptype(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rhBloodGroupCode = models.CharField(db_column='rhBloodGroupCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    rhBloodGroupName = models.CharField(db_column='rhBloodGroupName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbRhBloodGroupType'


class Tbrole(models.Model):
    RoleId = models.AutoField(db_column='RoleId', primary_key=True)  # Field name made lowercase.
    RoleName = models.CharField(db_column='RoleName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    dtTm = models.DateField(db_column='dtTm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbRole'


class Tbsymptom(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Symptom_Name = models.CharField(db_column='Symptom_Name', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbSymptom'


class Tbtoiletcode(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    toiletCode = models.CharField(db_column='toiletCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    toiletName = models.CharField(db_column='toiletName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbToiletCode'


class Tbuser(models.Model):
    UserId = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    UserName = models.CharField(db_column='UserName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    UserPWD = models.CharField(db_column='UserPWD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    RoleId = models.IntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.
    LastLoginTime = models.DateField(db_column='LastLoginTime', blank=True, null=True)  # Field name made lowercase.
    LoginCount = models.IntegerField(db_column='LoginCount', blank=True, null=True)  # Field name made lowercase.
    LastLoginIP = models.CharField(db_column='LastLoginIP', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbUser'


class Tbwatercode(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    waterCode = models.CharField(db_column='waterCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    waterName = models.CharField(db_column='waterName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbWaterCode'
