#-*- coding: utf-8 -*-
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
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Tbmedicalorganization(models.Model):#医疗机构
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orgCode = models.CharField('机构代码',db_column='orgCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    orgName = models.CharField('机构名称',db_column='orgName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    orgType = models.CharField('机构类型',db_column='orgType', max_length=120, blank=True, null=True)  # Field name made lowercase.
    parentOrgCode = models.CharField('父机构代码',db_column='parentOrgCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    areaCode = models.CharField('所属区域代码',db_column='areaCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    levelOrder = models.IntegerField('排序级别',db_column='levelOrder', blank=True, null=True)  # Field name made lowercase.
    IsEnabled = models.CharField('是否可用',db_column='IsEnabled', max_length=120, blank=True, null=True)  # Field name made lowercase.
    Comment = models.CharField('备注',db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbMedicalOrganization'
        verbose_name = '医疗机构'
        verbose_name_plural = '医疗机构'
    def __unicode__(self):
      return self.orgName
class Tbarea(models.Model):#行政区域机构
    ID = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    areaName = models.CharField('区域名称',db_column='areaName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    areaCode = models.CharField('区域代码',db_column='areaCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    areaType = models.IntegerField('区域类型',db_column='areaType', blank=True, null=True)  # Field name made lowercase.
    parentAreaCode = models.CharField('上级区域代码',db_column='parentAreaCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
    leverOrder=models.IntegerField('等级排序',db_column='leverOrder', blank=True, null=True)
    Comment = models.CharField(db_column='Comment', max_length=120, blank=True, null=True)  # Field name made lowercase.
    IsEnable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbArea'
        verbose_name = '区域'
        verbose_name_plural = '区域'
    def __unicode__(self):
      return self.areaName
class UserProfile(models.Model):
    user = models.OneToOneField(User)    
    areaCode = models.CharField(db_column='areaCode', max_length=32,blank=True)
    type = models.CharField(max_length=1,default='',blank=True)
    orgCode=models.ForeignKey(Tbmedicalorganization,related_name='UserProfile_orgCode',db_column='orgCode',default=1,verbose_name = '机构代码')
    pym=models.CharField(db_column='pym',max_length=32,blank=True,null=True)
    wbm=models.CharField(db_column='wbm',max_length=32,blank=True,null=True)
    def __unicode__(self):
        return self.user.last_name+self.user.first_name

def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

# post_save.connect(create_user_profile, sender=User)


class TbdiabetesSpecial(models.Model):#糖尿病专项档案
    ID=models.AutoField(db_column='ID',primary_key=True)
    #外键 UserProfile  默认为12
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='TbdiabetesSpecial_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')
    personProfile = models.ForeignKey(UserProfile,related_name='TbdiabetesSpecial_personId',db_column='personProfile',default=12,verbose_name = '居民个人ID')
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='TbdiabetesSpecial_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
    
    organization=models.ForeignKey(Tbmedicalorganization,related_name='TbdiabetesSpecial_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    
    specialNo=models.CharField('糖尿病专项编号',db_column='specialNo', max_length=17,blank=True,null=True)
    name=models.CharField('姓名',db_column='name', max_length=20,blank=True,null=True)
    registerDate=models.DateField('建档日期',db_column='registerDate',blank=True,null=True)
    registerOrgCode=models.CharField('建档单位代码',db_column='registerOrgCode', max_length=16,blank=True,null=True)
    registerDoctorCode=models.CharField('建档人代码',db_column='registerDoctorCode', max_length=20,blank=True,null=True)
    registerDoctorName=models.CharField('建档人姓名',db_column='registerDoctorName', max_length=20,blank=True,null=True)
    diagnoseDate=models.DateField('确诊日期',db_column='diagnoseDate', blank=True,null=True)
    diagnoseOrgCode=models.CharField('确诊单位代码',db_column='diagnoseOrgCode', max_length=16,blank=True,null=True)
    #外键 UserProfile  默认为2
#     diagnoseDoctorCode=models.ForeignKey(UserProfile,related_name='TbdiabetesSpecial_Doctor_ID',db_column='diagnoseDoctorCode',default=2,verbose_name = '确诊医生')
    diagnoseDoctorName=models.CharField('确诊医生姓名',db_column='diagnoseDoctorName', max_length=20,blank=True,null=True)
    SBP=models.DecimalField('收缩压',db_column='SBP', max_digits=3,decimal_places=0,blank=True,null=True)
    DBP=models.DecimalField('舒张压',db_column='DBP', max_digits=3,decimal_places=0,blank=True,null=True)
    bloodPressureLevel=models.CharField('血压分级',db_column='bloodPressureLevel', max_length=1,blank=True,null=True)
    nextFlupDate=models.DateField('下次随访日期',db_column='nextFlupDate', blank=True,null=True)
    diabetesLevelCode=models.CharField('糖尿病管理分级代码',db_column='diabetesLevelCode', max_length=1,blank=True,null=True)
    caseType=models.CharField('病例种类',db_column='caseType', max_length=1,blank=True,null=True)
    ICDCode=models.CharField('ICD-10 编码',db_column='ICDCode', max_length=20,blank=True,null=True)
    doseCode=models.CharField('是否服药',db_column='doseCode', max_length=1,blank=True,null=True)
    noMedicationCode=models.CharField('未服药原因',db_column='noMedicationCode', max_length=1,blank=True,null=True)
    drugCost=models.DecimalField('月服药费用',db_column='drugCost', max_digits=10,decimal_places=2,blank=True,null=True)
    familyHistoryCode=models.CharField('糖尿病家族史',db_column='familyHistoryCode', max_length=1,blank=True,null=True)
    height=models.DecimalField('身高',db_column='height', max_digits=6,decimal_places=2,blank=True,null=True)
    randomBloodGlucose=models.DecimalField('随机血糖值',db_column='randomBloodGlucose', max_digits=6,decimal_places=2,blank=True,null=True)
    kidneyDiseaseYears=models.DecimalField('肾脏病变年数',db_column='kidneyDiseaseYears', max_digits=3,decimal_places=0,blank=True,null=True)
    retinalDiseaseYears=models.DecimalField('视网膜病变年数',db_column='retinalDiseaseYears', max_digits=3,decimal_places=0,blank=True,null=True)
    neuropathyYears=models.DecimalField('神经病变年数',db_column='neuropathyYears', max_digits=3,decimal_places=0,blank=True,null=True)
    skinInfectionYears=models.DecimalField('皮肤感染年数',db_column='skinInfectionYears', max_digits=3,decimal_places=0,blank=True,null=True)
    vascularDiseaseYears=models.DecimalField('血管病变年数',db_column='vascularDiseaseYears', max_digits=3,decimal_places=0,blank=True,null=True)
    noComplYears=models.DecimalField('无并发症年数',db_column='noComplYears', max_digits=3,decimal_places=0,blank=True,null=True)
    complicationDate=models.DateField('糖尿病并发症时间',db_column='complicationDate', blank=True,null=True)
    initialDisease=models.CharField('初次病种',db_column='initialDisease', max_length=60,blank=True,null=True)
    currentDisease=models.CharField('当前病种',db_column='currentDisease', max_length=60,blank=True,null=True) 
    caseSourceCode=models.CharField('病例来源',db_column='caseSourceCode', max_length=1,blank=True,null=True)
    caseSourceOther=models.CharField('病例来源其他',db_column='caseSourceOther', max_length=120,blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'TbdiabetesSpecial'
        verbose_name = '糖尿病专项档案'
        verbose_name_plural = '糖尿病专项档案'
    def __unicode__(self):
      return self.areaName
class Tbdiabetesflup(models.Model):#糖尿病随访记录
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    businessKey = models.CharField('业务序号',db_column='businessKey', max_length=40, blank=True, null=True)  # Field name made lowercase.
    #默认为ID=11 地区代码为500   重庆市
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='Tbdiabetesflup_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')
    #登陆名称    默认为 default  ID=12
    personProfile=models.ForeignKey(UserProfile,related_name='Tbdiabetesflup_personProfile',db_column='personProfile',default=12,verbose_name = '登录名')
    #默认为ID=2   admin
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='Tbdiabetesflup_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
    
    organization=models.ForeignKey(Tbmedicalorganization,related_name='Tbdiabetesflup_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    specialNo = models.CharField('糖尿病专项编号',db_column='specialNo', max_length=17, blank=True, null=True)  # Field name made lowercase.
    healthFileNumber = models.CharField('健 康 档 案 编号',db_column='healthFileNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField('一体机代码',db_column='mechineCode', max_length=40,blank=True, null=True)  # Field name made lowercase.
    mechineNo = models.CharField('一体机业务编号',db_column='mechineNo', max_length=40,blank=True, null=True)  # Field name made lowercase.
    name = models.CharField('姓名',max_length=20,blank=True, null=True)
    genderCode = models.CharField('性别',db_column='genderCode', max_length=1,blank=True, null=True)  # Field name made lowercase.
    flupDate = models.DateField('随访日期',db_column='flupDate',blank=True, null=True)  # Field name made lowercase.
    flupMode = models.CharField('随访方式',db_column='flupMode', max_length=4,blank=True, null=True)  # Field name made lowercase.
    symptomCodes = models.CharField('症状代码',db_column='symptomCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    symptomOther = models.CharField('症状（其他）',db_column='symptomOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField('收缩压',db_column='SBP', max_digits=3, decimal_places=0,blank=True, null=True)  # Field name made lowercase.
    DBP = models.DecimalField('舒张压',db_column='DBP', max_digits=3, decimal_places=0,blank=True, null=True)  # Field name made lowercase.
    bloodPressureLevel = models.CharField('血压分级',db_column='bloodPressureLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField('体重',max_digits=5, decimal_places=2, blank=True, null=True)
    weightTarget = models.DecimalField('体重-目标值',db_column='weightTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bmi = models.DecimalField('体质指数',max_digits=5, decimal_places=2, blank=True, null=True)
    bmiTarget = models.DecimalField('体质指数-目标值',db_column='bmiTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dorsalisPedisPulseCode = models.CharField('足 背 动 脉 搏动编码',db_column='dorsalisPedisPulseCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    signsOther = models.CharField('体征-其他',db_column='signsOther', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dailySmoking = models.DecimalField('日吸烟量',db_column='dailySmoking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailySmokingTarget = models.DecimalField('日吸烟量-目标值',db_column='dailySmokingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinking = models.DecimalField('日饮酒量',db_column='dailyDrinking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinkingTarget = models.DecimalField('日饮酒量-目标值',db_column='dailyDrinkingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovements = models.DecimalField('每 周 运 动 次数',db_column='perWeekMovements', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovementsTarget = models.DecimalField('每 周 运 动 次数-目标值',db_column='perWeekMovementsTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimes = models.DecimalField('每 次 运 动 时间',db_column='perWeekTimes', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimesTarget = models.DecimalField('每 次 运 动 时间-目标值',db_column='perWeekTimesTarget', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    stapleFood = models.DecimalField('主食',db_column='stapleFood', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    stapleFoodTarget = models.DecimalField('主食-目标值',db_column='stapleFoodTarget', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    psychologicalCode = models.CharField('心 理 调 整 代码',db_column='psychologicalCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    complianceCode = models.CharField('遵 医 行 为 代码',db_column='complianceCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fastingBloodGlucose = models.DecimalField('空腹血糖',db_column='fastingBloodGlucose', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    HbA1c = models.DecimalField('糖 化 血 红 蛋白',db_column='HbA1c', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    aidCheckDate = models.DateField('辅 助 检 查 日期',db_column='aidCheckDate', blank=True, null=True)  # Field name made lowercase.
    aidCheck = models.CharField('辅助检查（ 其他）',db_column='aidCheck', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doseCode = models.CharField('服 药 依 从 性代码',db_column='doseCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lowBloodSugarCode = models.CharField('低血糖反应',db_column='lowBloodSugarCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    adverseReactionCode = models.CharField('药 物 不 良 反应代码',db_column='adverseReactionCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flupTypeCode = models.CharField('此 次 随 访 分类代码',db_column='flupTypeCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    insulinMedicationType = models.CharField('胰 岛 素 用 药种类',db_column='insulinMedicationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    insulinMedicationRate = models.CharField('胰 岛 素 用 药频率',db_column='insulinMedicationRate', max_length=1, blank=True, null=True)  # Field name made lowercase.
    insulinMedicationDose = models.DecimalField('胰 岛 素 用 药剂量',db_column='insulinMedicationDose', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    
    medicationList = models.CharField('用药情况',db_column='medicationList', max_length=10, blank=True, null=True)  # Field name made lowercase.
    
    referralReason = models.CharField('转诊原因',db_column='referralReason', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField('转诊机构',db_column='referralOrg', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralDepartment = models.CharField('转诊科室',db_column='referralDepartment', max_length=64, blank=True, null=True)  # Field name made lowercase.
    flupDoctorCode = models.CharField('随 访 医 生 代码',db_column='flupDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupDoctorName = models.CharField('随 访 医 生 名称',db_column='flupDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupOrgCode = models.CharField('随 访 机 构 代码',db_column='flupOrgCode', max_length=16,blank=True, null=True)  # Field name made lowercase.
    flupOrgName = models.CharField('随 访 机 构 名称',db_column='flupOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField('下 次 随 访 日期',db_column='nextFlupDate',blank=True, null=True)  # Field name made lowercase.
    
 
    class Meta:
        managed = True
        db_table = 'TbDiabetesFlup'
        verbose_name = '糖尿病随访记录'
        verbose_name_plural = '糖尿病随访记录'
    def __unicode__(self):
      return self.name  
    
class Tbchildspecial(models.Model):#儿童专项档案
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
#     personId = models.CharField('',db_column='personId', max_length=40)  # Field name made lowercase.
    #默认为ID=11 地区代码为500   重庆市
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='Tbchildspecial_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')
    #登陆名称    默认为 default  ID=12
    personProfile=models.ForeignKey(UserProfile,related_name='Tbchildspecial_personProfile',db_column='personProfile',default=12,verbose_name = '登录名')
    #责任医生 默认为ID=2   admin
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='Tbchildspecial_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
   
    organization=models.ForeignKey(Tbmedicalorganization,related_name='Tbchildspecial_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    specialNo = models.CharField('儿童专项编号',db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField('一体机代码',db_column='mechineCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mechineNo = models.CharField('一体机业务编号',db_column='mechineNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField('姓名',max_length=20, blank=True, null=True)
    genderCode = models.CharField('性别代码',db_column='genderCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField('出生日期', blank=True, null=True)

    childHealthCardNo = models.CharField('儿童保健卡编号',db_column='childHealthCardNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    homeAddress = models.CharField('家庭地址',db_column='homeAddress', max_length=60, blank=True, null=True)  # Field name made lowercase.
    birthWeight = models.DecimalField('出生体重',db_column='birthWeight', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    birthHeight = models.DecimalField('出生身长',db_column='birthHeight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    parity = models.DecimalField('胎次',max_digits=2, decimal_places=0, blank=True, null=True)
    deliveryTimes = models.DecimalField('产次',db_column='deliveryTimes', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deliveryGestationalWeeks = models.DecimalField('分娩孕周',db_column='deliveryGestationalWeeks', max_digits=2, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deliveryModeCode = models.CharField('分娩方式代码',db_column='deliveryModeCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    childbirth = models.CharField('产时情况',max_length=100, blank=True, null=True)
    birthHospital = models.CharField('出生医院',db_column='birthHospital', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fatherName = models.CharField('父亲姓名',db_column='fatherName', max_length=20)  # Field name made lowercase.
    motherName = models.CharField('母亲姓名',db_column='motherName', max_length=20)  # Field name made lowercase.
    fatherContac = models.CharField('父亲联系电话',db_column='fatherContac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    motherContac = models.CharField('母亲联系电话',db_column='motherContac', max_length=20, blank=True, null=True)  # Field name made lowercase.
    UNHSCode = models.CharField('新生儿听力筛查代码',db_column='UNHSCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CYP17Code = models.CharField('17-a-OHP',db_column='CYP17Code', max_length=1, blank=True, null=True)  # Field name made lowercase.
    PKUCode = models.CharField('苯丙酮尿症筛查代码',db_column='PKUCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CHCode = models.CharField('先天性甲状腺功能低下代码',db_column='CHCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    highRiskCode = models.CharField('是否高危代码',db_column='highRiskCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    highRiskFactors = models.CharField('高危因素',db_column='highRiskFactors', max_length=500, blank=True, null=True)  # Field name made lowercase.
    apgar1 = models.SmallIntegerField('Apgar 1 分钟评分',blank=True, null=True)
    apgar5 = models.SmallIntegerField('Apgar 5 分钟评分',blank=True, null=True)
    apgar10 = models.SmallIntegerField('Apgar 10 分钟评分',blank=True, null=True)
    pastHistory = models.CharField('既往病史',db_column='pastHistory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    allergicHistory = models.CharField('过敏史',db_column='allergicHistory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    childbirthHospital = models.CharField('接产医院',db_column='childbirthHospital', max_length=50, blank=True, null=True)  # Field name made lowercase.
    childbirthDoctor = models.CharField('接产主手',db_column='childbirthDoctor', max_length=20, blank=True, null=True)  # Field name made lowercase.
    childbirthAssistant = models.CharField('接产副手',db_column='childbirthAssistant', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registDate = models.DateField('建册日期',db_column='registDate', blank=True, null=True)  # Field name made lowercase.
    registerOrgCode = models.CharField('建册单位代码',db_column='registerOrgCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    registerOrgName = models.CharField('建册单位名称',db_column='registerOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorCode = models.CharField('建册人代码',db_column='registerDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorName = models.CharField('建册人姓名',db_column='registerDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        managed = True
        db_table = 'TbChildSpecial'
        verbose_name = '儿童专项档案'
        verbose_name_plural = '儿童专项档案'
    def __unicode__(self):
        return self.name 

class neonatalVisit(models.Model):#儿童随访记录
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    businessKey = models.CharField('业务序号',db_column='businessKey', max_length=40, blank=True, null=True)  # Field name made lowercase.
    #默认为ID=11 地区代码为500   重庆市
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='neonatalVisit_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')
    #登陆名称    默认为 default  ID=12
    personProfile=models.ForeignKey(UserProfile,related_name='neonatalVisit_personProfile',db_column='personProfile',default=12,verbose_name = '登录名')
    #默认为ID=2   admin
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='neonatalVisit_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
    
    organization=models.ForeignKey(Tbmedicalorganization,related_name='neonatalVisit_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    
    specialNo = models.CharField('儿童专项编号',db_column='specialNo', max_length=14, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField('一体机代码',db_column='mechineCode', max_length=40,blank=True, null=True)  # Field name made lowercase.
    mechineNo = models.CharField('一体机业务编号',db_column='mechineNo', max_length=40,blank=True, null=True)  # Field name made lowercase.
    name = models.CharField('姓名',max_length=20,blank=True, null=True)
    genderCode = models.CharField('性别',db_column='genderCode', max_length=1,blank=True, null=True)  # Field name made lowercase.
    birthday=models.DateField('出生日期',db_column='birthday',blank=True, null=True)
    idCard= models.CharField('身份证号',db_column='idCard',max_length=18,blank=True, null=True)
    homeAddress= models.CharField('家庭住址',db_column='homeAddress',max_length=60,blank=True, null=True)
    fatherName= models.CharField('父亲姓名',db_column='fatherName',max_length=20,blank=True, null=True)
    matherName= models.CharField('母亲姓名',db_column='matherName',max_length=20,blank=True, null=True)
    fatherOccupation= models.CharField('父亲职业',db_column='fatherOccupation',max_length=50,blank=True, null=True)
    matherOccupation= models.CharField('母亲职业',db_column='matherOccupation',max_length=50,blank=True, null=True)
    fatherContac= models.CharField('父亲联系电话',db_column='fatherContac',max_length=20,blank=True, null=True)
    matherContac= models.CharField('母亲联系电话',db_column='matherContac',max_length=20,blank=True, null=True)
    fatherBirthday=models.DateField('父亲出生日期',db_column='fatherBirthday',blank=True, null=True)
    matherBirthday=models.DateField('母亲出生日期',db_column='matherBirthday',blank=True, null=True)
    weekOfBirth=models.DecimalField('出生孕周',db_column='weekOfBirth',max_digits=2, decimal_places=0,blank=True, null=True)
    pregnancyBeIllCode= models.CharField('母亲妊娠期患病情况代码',db_column='pregnancyBeIllCode',max_length=1,blank=True, null=True)
    pregnancyBeIllOther= models.CharField('母亲妊娠期患病情况其他',db_column='pregnancyBeIllOther',max_length=100,blank=True, null=True)
    midwiferyOrgName= models.CharField('助产机构名称',db_column='midwiferyOrgName',max_length=60,blank=True, null=True)
    birthConditionCodes= models.CharField('出生情况代码',db_column='birthConditionCodes',max_length=30,blank=True, null=True)
    neonatalAsphyxiaCode= models.CharField('新生儿窒息代码',db_column='neonatalAsphyxiaCode',max_length=1,blank=True, null=True)
    apgar1= models.DecimalField('Apgar 1分钟评分',db_column='apgar1',max_digits=2, decimal_places=0,blank=True, null=True)
    apgar5= models.DecimalField('Apgar 5分钟评',db_column='apgar5',max_digits=2, decimal_places=0,blank=True, null=True)
    apgar10= models.DecimalField('Apgar 10 分钟评分',db_column='apgar10',max_digits=2, decimal_places=0,blank=True, null=True)
    deformityCode= models.CharField('是否有畸型',db_column='deformityCode',max_length=1,blank=True, null=True)
    deformityOther= models.CharField('畸型描述',db_column='deformityOther',max_length=100,blank=True, null=True)
    UNHSCode= models.CharField('新生儿听力筛查代码',db_column='UNHSCode',max_length=1,blank=True, null=True)
    neonatalScreeningCode= models.CharField('新生儿疾病筛查代码',db_column='neonatalScreeningCode',max_length=1,blank=True, null=True)
    neonatalScreeningOther= models.CharField('新生儿疾病筛查其他',db_column='neonatalScreeningOther',max_length=100,blank=True, null=True)
    birthWeight=models.DecimalField('出生体重',db_column='birthWeight',max_digits=7, decimal_places=2,blank=True, null=True)
    currentWeight=models.DecimalField('目前体重',db_column='currentWeight',max_digits=7, decimal_places=2,blank=True, null=True)
    birthHeight=models.DecimalField('出生身长',db_column='birthHeight',max_digits=5, decimal_places=2,blank=True, null=True)
    feedingPatternCode= models.CharField('喂养方式',db_column='feedingPatternCode',max_length=1,blank=True, null=True)
    feedingAmount=models.DecimalField('吃奶量',db_column='feedingAmount',max_digits=5, decimal_places=1,blank=True, null=True)
    feedingTimes=models.DecimalField('吃奶次数',db_column='feedingTimes',max_digits=2, decimal_places=0,blank=True, null=True)
    vomitCode= models.CharField('呕吐代码',db_column='vomitCode',max_length=1,blank=True, null=True)
    fecalCode= models.CharField('大便代码',db_column='fecalCode',max_length=1,blank=True, null=True)
    fecalTimes=models.DecimalField('大便次数',db_column='fecalTimes',max_digits=2, decimal_places=0,blank=True, null=True)
    temperature=models.DecimalField('体温',db_column='temperature',max_digits=3, decimal_places=1,blank=True, null=True)
    pulseRate=models.DecimalField('脉率',db_column='pulseRate',max_digits=3, decimal_places=0,blank=True, null=True)
    respiratoryRate=models.DecimalField('呼吸频率',db_column='respiratoryRate',max_digits=3, decimal_places=0,blank=True, null=True)
    complexionCode= models.CharField('面色代码',db_column='complexionCode',max_length=1,blank=True, null=True)
    complexionOther= models.CharField('面色其他',db_column='complexionOther',max_length=50,blank=True, null=True)
    jaundiceSiteCode= models.CharField('黄疸部位代码',db_column='jaundiceSiteCode',max_length=1,blank=True, null=True)
    bregma1=models.DecimalField('前囟 1',db_column='bregma1',max_digits=4, decimal_places=1,blank=True, null=True)
    bregma2=models.DecimalField('前囟 2',db_column='bregma2',max_digits=4, decimal_places=1,blank=True, null=True)
    bregmaCode= models.CharField('前囟代码',db_column='bregmaCode',max_length=1,blank=True, null=True)
    bregmaOther= models.CharField('前囟其他',db_column='bregmaOther',max_length=50,blank=True, null=True)
    eyeAppearanceCode= models.CharField('眼外观代码',db_column='eyeAppearanceCode',max_length=1,blank=True, null=True)
    eyeAppearanceDesc= models.CharField('眼外观异常',db_column='eyeAppearanceDesc',max_length=50,blank=True, null=True)
    limbsActivityCode= models.CharField('四肢活动度代码',db_column='limbsActivityCode',max_length=1,blank=True, null=True)
    limbsActivityDesc= models.CharField('四肢活动度异常',db_column='limbsActivityDesc',max_length=50,blank=True, null=True)
    earAppearanceCode= models.CharField('耳外观代码',db_column='earAppearanceCode',max_length=1,blank=True, null=True)
    earAppearanceDesc= models.CharField('耳外观异常',db_column='earAppearanceDesc',max_length=50,blank=True, null=True)
    neckMassCode= models.CharField('颈部包块代码',db_column='neckMassCode',max_length=1,blank=True, null=True)
    neckMassDesc= models.CharField('颈部包块描述',db_column='neckMassDesc',max_length=50,blank=True, null=True)
    noseCode= models.CharField('鼻代码',db_column='noseCode',max_length=1,blank=True, null=True)
    noseDesc= models.CharField('鼻异常',db_column='noseDesc',max_length=50,blank=True, null=True)
    skinCode= models.CharField('皮肤代码',db_column='skinCode',max_length=1,blank=True, null=True)
    skinOther= models.CharField('皮肤其他',db_column='skinOther',max_length=50,blank=True, null=True)
    oralCode= models.CharField('口腔代码',db_column='oralCode',max_length=1,blank=True, null=True)
    oralDesc= models.CharField('口腔异常',db_column='oralDesc',max_length=50,blank=True, null=True)
    anusCode= models.CharField('肛门代码',db_column='anusCode',max_length=1,blank=True, null=True)
    anusDesc= models.CharField('肛门异常',db_column='anusDesc',max_length=50,blank=True, null=True)
    heartLungAuscultationCode= models.CharField('心肺听诊代码',db_column='heartLungAuscultationCode',max_length=1,blank=True, null=True)
    heartLungAuscultationDesc= models.CharField('心肺听诊异常',db_column='heartLungAuscultationDesc',max_length=50,blank=True, null=True)
    externalGenitalCode= models.CharField('外生殖器代码',db_column='externalGenitalCode',max_length=1,blank=True, null=True)
    externalGenitalDesc= models.CharField('外生殖器异常',db_column='externalGenitalDesc',max_length=50,blank=True, null=True)
    abdominalPalpationCode= models.CharField('腹部触诊代码',db_column='abdominalPalpationCode',max_length=1,blank=True, null=True)
    abdominalPalpationDesc= models.CharField('腹部触诊异常',db_column='abdominalPalpationDesc',max_length=50,blank=True, null=True)
    spineCode= models.CharField('脊柱代码',db_column='spineCode',max_length=1,blank=True, null=True)
    spineDesc= models.CharField('脊柱异常',db_column='spineDesc',max_length=50,blank=True, null=True)
    umbilicalCordCode= models.CharField('脐带代码',db_column='umbilicalCordCode',max_length=1,blank=True, null=True)
    umbilicalCordOther= models.CharField('脐带其他',db_column='umbilicalCordOther',max_length=50,blank=True, null=True)
    referralCode= models.CharField('转诊建议',db_column='referralCode',max_length=1,blank=True, null=True)
    referralReason= models.CharField('转诊原因',db_column='referralReason',max_length=100,blank=True, null=True)
    referralOrg= models.CharField('转诊机构',db_column='referralOrg',max_length=50,blank=True, null=True)
    referralDepartment= models.CharField('转诊科室',db_column='referralDepartment',max_length=50,blank=True, null=True)
    guideCodes= models.CharField('指导代码',db_column='guideCodes',max_length=14,blank=True, null=True)
    flupDate= models.DateField('随访日期',db_column='flupDate',blank=True, null=True)
    flupDoctorCode= models.CharField('随访医生代码',db_column='flupDoctorCode',max_length=16,blank=True, null=True)
    flupDoctorName= models.CharField('随访医生名称',db_column='flupDoctorName',max_length=20,blank=True, null=True)
    flupOrgCode= models.CharField('随访机构代码',db_column='flupOrgCode',max_length=16,blank=True, null=True)
    flupOrgName= models.CharField('随访机构名称',db_column='flupOrgName',max_length=50,blank=True, null=True)
    nextFlupDate= models.DateField('下次随访日期',db_column='nextFlupDate',blank=True, null=True)
    nextFlupLocation= models.CharField('下次随访地点',db_column='nextFlupLocation',max_length=100,blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'neonatalVisit'
        verbose_name = '儿童随访'
        verbose_name_plural = '儿童随访'
    def __unicode__(self):
        return self.name 

class Tbhealthrecord(models.Model):#健康档案！
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    #登陆名称    默认为 default  ID=12
    personProfile = models.ForeignKey(UserProfile,related_name='Tbhealthrecord_personId',db_column='personProfile',default=12,verbose_name = '居民个人ID')
    machineCode = models.CharField('健康一体机编码',db_column='machineCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    machineNo = models.CharField('一体机业务序号',db_column='machineNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ###############################默认为ID=11 地区代码为500   重庆市
    nowLiveCode = models.IntegerField(db_column='nowLiveCode',default=11,verbose_name = '居住地')  # Field name made lowercase.
    
    nowLiveName = models.CharField('居住地名称',db_column='nowLiveName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nowLiveAddr = models.CharField('居住地地址',db_column='nowLiveAddr', max_length=100, blank=True, null=True)  # Field name made lowercase.
   
    #默认为ID=11 地区代码为500   重庆市
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='Tbhealthrecord_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')  # Field name made lowercase.  # Field name made lowercase.
    
    organization=models.ForeignKey(Tbmedicalorganization,related_name='Tbhealthrecord_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    householdRegisterName = models.CharField('户籍地名称',db_column='householdRegisterName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    householdRegisterAddr = models.CharField('户籍地地址',db_column='householdRegisterAddr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    registerOrgCode = models.CharField('建档单位代码',db_column='registerOrgCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    registerDoctorCode = models.CharField('建档人代码',db_column='registerDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorName = models.CharField('建档人姓名',db_column='registerDoctorName',  max_length=20, blank=True, null=True)  # Field name made lowercase.
    #默认为ID=2   admin
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='Tbhealthrecord_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
    
    responsibleDoctorName = models.CharField('责任医生姓名',db_column='responsibleDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDate = models.DateField('建档日期',db_column='registerDate')  # Field name made lowercase.
    healthFileNumber = models.CharField('健康档案编号',db_column='healthFileNumber', max_length=17)  # Field name made lowercase.
    name = models.CharField('姓名',max_length=20)
    genderCode = models.CharField('性别',db_column='genderCode', max_length=1)  # Field name made lowercase.
    birthday = models.DateField('出生日期',)
    idCard = models.CharField('身份证号',db_column='idCard', max_length=18)  # Field name made lowercase.
    workUnit = models.CharField('工作单位',db_column='workUnit', max_length=60, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField('本人电话',max_length=30, blank=True, null=True)
    contacts = models.CharField('联系人',max_length=20, blank=True, null=True)
    contactsPhone = models.CharField('联系人电话',db_column='contactsPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    residentType = models.CharField('常住类型代码',db_column='residentType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ethnicityCode = models.CharField('民族代码',db_column='ethnicityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ethnicityName = models.CharField('民族名称',db_column='ethnicityName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bloodGroupCode = models.CharField('血型代码',db_column='bloodGroupCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rhBloodGroupCode = models.CharField('Rh阴性代码',db_column='rhBloodGroupCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    eduBGCode = models.CharField('文化程度代码',db_column='eduBGCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    occupationCode = models.CharField('职业代码',db_column='occupationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    maritalStatusCode = models.CharField('婚姻状况代码',db_column='maritalStatusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    paymentMethodCodes = models.CharField('医疗费用支付代码',db_column='paymentMethodCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymentMethodOther = models.CharField('医疗费用支付其他',db_column='paymentMethodOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    drugAllergyHistoryCodes = models.CharField('药物过敏史代码',db_column='drugAllergyHistoryCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    drugAllergyHistoryOther = models.CharField('药物过敏史其他',db_column='drugAllergyHistoryOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    exposureHistoryCodes = models.CharField('暴露史代码',db_column='exposureHistoryCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pastHistoryListCol = models.CharField('既往史列表',db_column='pastHistoryList', max_length=120, blank=True, null=True)  # Field name made lowercase.
    familyHistoryFatherCodes = models.CharField('家族疾病史代码-父亲',db_column='familyHistoryFatherCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    familyHistoryFatherOther = models.CharField('家族疾病史父亲其他',db_column='familyHistoryFatherOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    familyHistoryMatherCodes = models.CharField('家族疾病史代码-母亲',db_column='familyHistoryMatherCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    familyHistoryMatherOther = models.CharField('家族疾病史母亲其他',db_column='familyHistoryMatherOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    brotherAndSisterCodes = models.CharField('家族疾病史代码-兄弟姐妹',db_column='brotherAndSisterCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    brotherAndSisterOther = models.CharField('家族疾病史兄弟姐妹其他',db_column='brotherAndSisterOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    familyHistoryChildrenCodes = models.CharField('家族疾病史代码-子女',db_column='familyHistoryChildrenCodes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    familyHistoryChildrenOther = models.CharField('家族疾病史子女其他',db_column='familyHistoryChildrenOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    geneticHistoryCode = models.CharField('遗传病史代码',db_column='geneticHistoryCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    geneticHistoryOther = models.CharField('遗传病史名称',db_column='geneticHistoryOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    disabilityCodes = models.CharField('残疾情况代码多选',db_column='disabilityCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disabilityOther = models.CharField('残疾情况-其他',db_column='disabilityOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    kitchenExhaustCode = models.CharField('厨房排风设施',db_column='kitchenExhaustCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fuelTypeCode = models.CharField('燃料类型代码',db_column='fuelTypeCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    waterCode = models.CharField('饮水代码',db_column='waterCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    toiletCode = models.CharField('厕所代码',db_column='toiletCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    livestockColumnCode = models.CharField('禽畜栏代码',db_column='livestockColumnCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     ownerMask=models.CharField('拥有者掩码',db_column='ownerMask',max_length=120, blank=True, null=True)
    CreateUser = models.CharField('创建人',db_column='CreateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField('创建时间',db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField('修改人',db_column='UpdateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField('修改时间',db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField('删除人',db_column='DeleteUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField('删除时间',db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'TbHealthRecord'
        verbose_name = '电子健康档案'
        verbose_name_plural = '电子健康档案'
    def __unicode__(self):
      return self.name


class Tbhypertensionflup(models.Model):#高血压随访
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    businessKey = models.CharField("业务记录",db_column='businessKey', max_length=40, blank=True, null=True)  # Field name made lowercase.
    #默认为ID=11 地区代码为500   重庆市
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='Tbhypertensionflup_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')
    #登陆名称    默认为 default  ID=12
    personProfile=models.ForeignKey(UserProfile,related_name='Tbhypertensionflup_personProfile',db_column='personProfile',default=12,verbose_name = '登录名')
    #责任医生 默认为ID=2   admin
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='Tbhypertensionflup_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
    
    organization=models.ForeignKey(Tbmedicalorganization,related_name='Tbhypertensionflup_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    
    specialNo = models.CharField("高血压专项编号",db_column='specialNo', max_length=17, blank=True, null=True)  # Field name made lowercase.
    healthFileNumber = models.CharField("健康档案编号",db_column='healthFileNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField("机器代码",db_column='mechineCode', max_length=40)  # Field name made lowercase.
    mechineNo = models.CharField("机器编号",db_column='mechineNo', max_length=40)  # Field name made lowercase.
    name = models.CharField("姓名",max_length=20)
    flupDate = models.DateField("随访日期",db_column='flupDate')  # Field name made lowercase.
    flupMode = models.CharField("随访模式",db_column='flupMode', max_length=4)  # Field name made lowercase.
    symptomCodes = models.CharField("症状代码",db_column='symptomCodes', max_length=30, blank=True, null=True)  # Field name made lowercase.
    symptomOther = models.CharField("其他症状",db_column='symptomOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField("收缩压",db_column='SBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    DBP = models.DecimalField("舒张压",db_column='DBP', max_digits=3, decimal_places=0)  # Field name made lowercase.
    bloodPressureLevel = models.CharField("血压分级",db_column='bloodPressureLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    heartRate = models.DecimalField("心率",db_column='heartRate', max_digits=4, decimal_places=0)  # Field name made lowercase.
    weight = models.DecimalField("体重",max_digits=5, decimal_places=2, blank=True, null=True)
    weightTarget = models.DecimalField("体重-目标",db_column='weightTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bmi = models.DecimalField("体质指数",max_digits=5, decimal_places=2, blank=True, null=True)
    bmiTarget = models.DecimalField("体质指数目标",db_column='bmiTarget', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    signsOther = models.CharField("体征-其他",db_column='signsOther', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dailySmoking = models.DecimalField("日吸烟量",db_column='dailySmoking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailySmokingTarget = models.DecimalField("日吸烟量-目标值",db_column='dailySmokingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinkingTarget = models.DecimalField("日饮酒量目标值",db_column='dailyDrinkingTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailyDrinking = models.DecimalField("日饮酒量",db_column='dailyDrinking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovements = models.DecimalField("每周运动次数",db_column='perWeekMovements', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekMovementsTarget = models.DecimalField("每周运动次数目标",db_column='perWeekMovementsTarget', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimes = models.DecimalField("每次运动时间（分钟）",db_column='perWeekTimes', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    perWeekTimesTarget = models.DecimalField("每次运动时间目标（分钟）",db_column='perWeekTimesTarget', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    saltIntakeCode = models.CharField("摄盐量编码",db_column='saltIntakeCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    saltIntakeTargetCode = models.CharField("摄盐量目标编码",db_column='saltIntakeTargetCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    psychologicalCode = models.CharField("心理调节代码",db_column='psychologicalCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    complianceCode = models.CharField("遵医行为代码",db_column='complianceCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aidCheck = models.CharField("辅助检查",db_column='aidCheck', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doseCode = models.CharField("服药依从性代码",db_column='doseCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    adverseReactionCode = models.CharField("药物不良反应代码",db_column='adverseReactionCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flupTypeCode = models.CharField(" 此次随访分类代码",db_column='flupTypeCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
   
    medicationList = models.CharField("用药情况",db_column='medicationList', max_length=10, blank=True, null=True)  # Field name made lowercase.
    
    referralReason = models.CharField("转诊原因",db_column='referralReason', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralOrg = models.CharField("转诊机构",db_column='referralOrg', max_length=64, blank=True, null=True)  # Field name made lowercase.
    referralDepartment = models.CharField("转诊科室",db_column='referralDepartment', max_length=64, blank=True, null=True)  # Field name made lowercase.
    flupDoctorCode = models.CharField("随访医生代码",db_column='flupDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupDoctorName = models.CharField("随访医生姓名",db_column='flupDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flupOrgCode = models.CharField("随访机构代码",db_column='flupOrgCode', max_length=16)  # Field name made lowercase.
    flupOrgName = models.CharField("随访机构名称",db_column='flupOrgName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField("下次随访日期",db_column='nextFlupDate')  # Field name made lowercase.
    UpdateUser = models.CharField("修改人",db_column='UpdateUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField("修改时间",db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField("删除人",db_column='DeleteUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField("创建人",db_column='CreateUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField("创建时间",db_column='CreateTime',blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField("删除时间",db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'TbHypertensionFlup'
        verbose_name = '高血压随访记录'
        verbose_name_plural ='高血压随访记录'
    def __unicode__(self):
        return self.name

class Tbhypertensionspecial(models.Model):#高血压专项档案
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    #默认为ID=11 地区代码为500   重庆市
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='Tbhypertensionspecial_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')
    #登陆名称    默认为 default  ID=12
    personProfile=models.ForeignKey(UserProfile,related_name='Tbhypertensionspecial_personProfile',db_column='personProfile',default=12,verbose_name = '登录名')
    #责任医生 默认为ID=2   admin
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='Tbhypertensionspecial_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
    organization=models.ForeignKey(Tbmedicalorganization,related_name='Tbhypertensionspecial_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    specialNo = models.CharField('高血压专项编号',db_column='specialNo', max_length=17, blank=True, null=True)  # Field name made lowercase.
    mechineCode = models.CharField('一体机代码',db_column='mechineCode', max_length=40,blank=True, null=True)  # Field name made lowercase.
    mechineNo = models.CharField('一体机业务编号',db_column='mechineNo', max_length=40,blank=True, null=True)  # Field name made lowercase.
    name = models.CharField('姓名',max_length=20,blank=True, null=True)
    genderCode = models.CharField('性别',db_column='genderCode', max_length=1,blank=True, null=True)  # Field name made lowercase.
    SBP = models.DecimalField('收缩压',db_column='SBP', max_digits=3, decimal_places=0,blank=True, null=True)  # Field name made lowercase.
    DBP = models.DecimalField('舒张压',db_column='DBP', max_digits=3, decimal_places=0,blank=True, null=True)  # Field name made lowercase.
    bloodPressureLevel = models.CharField('血压分级',db_column='bloodPressureLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nextFlupDate = models.DateField('下次随访日期',db_column='nextFlupDate',blank=True, null=True)  # Field name made lowercase.
    registDate = models.DateField('建档日期',db_column='registDate',blank=True, null=True)  # Field name made lowercase.
    registerOrgCode = models.CharField('建档单位代码',db_column='registerOrgCode', max_length=16,blank=True, null=True)  # Field name made lowercase.
    registerDoctorCode = models.CharField('建档人代码',db_column='registerDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registerDoctorName = models.CharField('建档人姓名',db_column='registerDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    diagnoseDate = models.DateField('确诊日期',db_column='diagnoseDate',blank=True, null=True)  # Field name made lowercase.
    diagnoseOrgCode = models.CharField('确诊单位代码',db_column='diagnoseOrgCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    diagnoseDoctorCode = models.CharField('确诊医生代码',db_column='diagnoseDoctorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    diagnoseDoctorName = models.CharField('确诊医生姓名',db_column='diagnoseDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbHypertensionSpecial'
        verbose_name = '高血压专项档案'
        verbose_name_plural = '高血压专项档案'
class Dicmedicationlist(models.Model):#用药情况
    ID = models.AutoField(db_column='ID', primary_key=True)
    drugCode = models.CharField('药品代码',db_column='drugCode', max_length=22, blank=True, null=True)  # Field name made lowercase.
    drugName = models.CharField('药品名称',db_column='drugName', max_length=32)  # Field name made lowercase.
    drugUsage = models.CharField('药品用法',db_column='drugUsage', max_length=32)  # Field name made lowercase.
    drugUsageAdd = models.CharField('药品用法补充',db_column='drugUsageAdd', max_length=32, blank=True, null=True)  # Field name made lowercase.
    drugDosage = models.CharField('药品用量',db_column='drugDosage', max_length=32)  # Field name made lowercase.
    drugDosageAdd = models.CharField('药品用量补充',db_column='drugDosageAdd', max_length=32, blank=True, null=True)  # Field name made lowercase.
    hypertension=models.ForeignKey(Tbhypertensionflup,related_name='hypertension',db_column='hypertension',blank=True,null=True)
    diabet=models.ForeignKey(Tbdiabetesflup,related_name='diabet',db_column='diabet',blank=True,null=True)
    class Meta:
        managed = True
        db_table = 'DicMedicationList'
        verbose_name = '用药情况'
        verbose_name_plural = '用药情况'
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





class Tbhealexamination(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    #登陆名称    默认为 default   ID=12
    personProfile = models.ForeignKey(UserProfile,related_name='Tbhealexamination_personProfile',db_column='personProfile',default=12,verbose_name = '居民个人ID')
   #默认为ID=11 地区代码为500   重庆市
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='Tbhealexamination_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')  # Field name made lowercase.
    organization=models.ForeignKey(Tbmedicalorganization,related_name='Tbhealexamination_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    healthFileNumber = models.CharField('健康档案编号',db_column='healthFileNumber', max_length=17, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField('姓名',max_length=20, blank=True, null=True)
    genderCode = models.CharField('性别代码',db_column='genderCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    
   
    # Field name made lowercase.
    idCard =models.CharField('身份证号',db_column='idCard', max_length=18, blank=True, null=True)
    machineCode = models.CharField('健康一体机编号',db_column='machineCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    machineNo = models.CharField('一体机业务编号',db_column='machineNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    businessKey = models.CharField('业务序列号',db_column='businessKey', max_length=40, blank=True, null=True)  # Field name made lowercase.
    examinationDate = models.DateField('体检日期',db_column='examinationDate', blank=True, null=True)  # Field name made lowercase.
    operatorName = models.CharField('操作员姓名',db_column='operatorName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    operatorCode = models.CharField('操作员代码',db_column='operatorCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    operateTime = models.DateTimeField('操作时间',db_column='operateTime', blank=True, null=True)  # Field name made lowercase.
    #默认为ID=2   责任医生为admin
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='Tbhealexamination_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')  # Field name made lowercase.
    
    responsibleDoctorName = models.CharField('责任医生姓名',db_column='responsibleDoctorName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    symptomCodes = models.CharField('症状代码',db_column='symptomCodes', max_length=60, blank=True, null=True)  # Field name made lowercase.
    symptomOther = models.CharField('症状 其他',db_column='symptomOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField('体温',max_digits=5, decimal_places=2, blank=True, null=True)
    pulseRate = models.DecimalField('脉搏',db_column='pulseRate', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    respiratoryRate = models.DecimalField('呼吸频率',db_column='respiratoryRate', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField('身高',max_digits=3, decimal_places=0, blank=True, null=True)
    weight = models.DecimalField('体重',max_digits=3, decimal_places=0, blank=True, null=True)
    bmi = models.DecimalField('体质指数',max_digits=5, decimal_places=2, blank=True, null=True)
    waistline = models.DecimalField('腰围',max_digits=5, decimal_places=2, blank=True, null=True)
    leftSBP = models.DecimalField('左侧血压 收缩压',db_column='leftSBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    leftDBP = models.DecimalField('左侧血压 舒张压',db_column='leftDBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rightSBP = models.DecimalField('右侧血压 收缩压',db_column='rightSBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rightDBP = models.DecimalField('右侧血压 舒张压',db_column='rightDBP', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    theAgedStatus = models.CharField('老年人健康状态自我评估代码',db_column='theAgedStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    selfCareAbilityCode = models.CharField('老年人生活自理能力自我评估',db_column='selfCareAbilityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cognitiveFunction = models.CharField('老年人认知能力',db_column='cognitiveFunction', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cognitiveFunctionScore = models.DecimalField('老年人认知能力评分',db_column='cognitiveFunctionScore', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    emotionalState = models.CharField('老年人情感状态',db_column='emotionalState', max_length=1, blank=True, null=True)  # Field name made lowercase.
    emotionalStateScore = models.DecimalField('老年人情感状态评分',db_column='emotionalStateScore', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    exerciseFrequencyCode = models.CharField('体育锻炼频率代码',db_column='exerciseFrequencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    everyWorkoutTime = models.CharField('每次锻炼时间',db_column='everyWorkoutTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    insistOnExerciseTime = models.CharField('坚持锻炼时间',db_column='insistOnExerciseTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    exerciseMode = models.CharField('锻炼方式',db_column='exerciseMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eatingHabitsCodes = models.CharField('饮食习惯',db_column='eatingHabitsCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    smokingStatusCode = models.CharField('吸烟状况代码',db_column='smokingStatusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dailySmoking = models.DecimalField('日吸烟量',db_column='dailySmoking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smokingAge = models.DecimalField('开始吸烟年龄',db_column='smokingAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    smokingCessationAge = models.DecimalField('戒烟年龄',db_column='smokingCessationAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    drinkingFrequencyCode = models.CharField('饮酒频率代码',db_column='drinkingFrequencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dailyDrinking = models.DecimalField('日饮酒量',db_column='dailyDrinking', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    temperanceCode = models.CharField('是否戒酒',db_column='temperanceCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    temperanceAge = models.DecimalField('戒酒年龄',db_column='temperanceAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    drinkingAge = models.DecimalField('开始饮酒年龄',db_column='drinkingAge', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    whetherDrunk = models.CharField('近一年是否醉酒',db_column='whetherDrunk', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alcoholTypeCodes = models.CharField('饮酒种类代码',db_column='alcoholTypeCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alcoholTypeOther = models.CharField('饮酒种类其他',db_column='alcoholTypeOther', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exposureStateCode = models.CharField('是否有职业暴露情况',db_column='exposureStateCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hazardousWork = models.CharField('危害工种',db_column='hazardousWork', max_length=60, blank=True, null=True)  # Field name made lowercase.
    workingTime = models.DecimalField('从业时间',db_column='workingTime', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dust = models.CharField('毒物种类 粉尘',max_length=50, blank=True, null=True)
    dustProtective = models.CharField('粉尘防护措施',db_column='dustProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dustProtectiveDesc = models.CharField('粉尘防护措施描述',db_column='dustProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    radiogen = models.CharField('毒物种类 放射性物质',max_length=50, blank=True, null=True)
    radiogenProtective = models.CharField('放射性物质防护措施',db_column='radiogenProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    radiogenProtectiveDesc = models.CharField('放射性物质防护措施描述',db_column='radiogenProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    physical = models.CharField('毒物种类 物理因素',max_length=50, blank=True, null=True)
    physicalProtective = models.CharField('物理因素防护措施',db_column='physicalProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    physicalProtectiveDesc = models.CharField('物理因素防护措施描述',db_column='physicalProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.CharField('毒物种类 化学因素',max_length=50, blank=True, null=True)
    chemistryProtective = models.CharField('化学物质防护措施',db_column='chemistryProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chemistryProtectiveDesc = models.CharField('化学物质防护措施描述',db_column='chemistryProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    otherToxicant = models.CharField('毒物种类 其他',db_column='otherToxicant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otherProtective = models.CharField('其他防护措施',db_column='otherProtective', max_length=1, blank=True, null=True)  # Field name made lowercase.
    otherProtectiveDesc = models.CharField('其他防护措施描述',db_column='otherProtectiveDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    lipsCode = models.CharField('口唇代码',db_column='lipsCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dentitionCodes = models.CharField('齿列',db_column='dentitionCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    missingTeethLeftUp = models.CharField('缺齿左上',db_column='missingTeethLeftUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    missingTeethRightUp = models.CharField('缺齿右上',db_column='missingTeethRightUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    missingTeethLeftDown = models.CharField('缺齿左下',db_column='missingTeethLeftDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    missingTeethRightDown = models.CharField('缺齿右下',db_column='missingTeethRightDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesLeftUp = models.CharField('龋齿左上',db_column='cariesLeftUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesRightUp = models.CharField('龋齿右上',db_column='cariesRightUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesLeftDown = models.CharField('龋齿左下',db_column='cariesLeftDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cariesRightDown = models.CharField('龋齿右下',db_column='cariesRightDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureLeftUp = models.CharField('假齿左上',db_column='dentureLeftUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureRightUp = models.CharField('假齿右上',db_column='dentureRightUp', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureLeftDown = models.CharField('假齿左下',db_column='dentureLeftDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dentureRightDown = models.CharField('假齿右下',db_column='dentureRightDown', max_length=40, blank=True, null=True)  # Field name made lowercase.
    throatCode = models.CharField('咽部代码',db_column='throatCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visionRight = models.CharField('右眼视力',db_column='visionRight', max_length=12, blank=True, null=True)  # Field name made lowercase.
    visionLeft = models.CharField('左眼视力',db_column='visionLeft', max_length=12, blank=True, null=True)  # Field name made lowercase.
    redressVisionRight = models.CharField('右眼矫正视力',db_column='redressVisionRight', max_length=12, blank=True, null=True)  # Field name made lowercase.
    redressVisionLeft = models.CharField('左眼矫正视力',db_column='redressVisionLeft', max_length=12, blank=True, null=True)  # Field name made lowercase.
    hearingCode = models.CharField('听力代码',db_column='hearingCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motorFunctionCode = models.CharField('运动功能代码',db_column='motorFunctionCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fundusCode = models.CharField('眼底代码',db_column='fundusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fundusAbnormal = models.CharField('眼底异常情况',db_column='fundusAbnormal', max_length=60, blank=True, null=True)  # Field name made lowercase.
    skinCode = models.CharField('皮肤代码',db_column='skinCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    skinOther = models.CharField('皮肤其他',db_column='skinOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    scleraCode = models.CharField('虹膜代码',db_column='scleraCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    scleraOther = models.CharField('虹膜其他',db_column='scleraOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    lymphNodeCode = models.CharField('淋巴结代码',db_column='lymphNodeCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lymphNodeOther = models.CharField('淋巴结其他',db_column='lymphNodeOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    barrelChestCode = models.CharField('肺-桶状胸',db_column='barrelChestCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    breathSoundCode = models.CharField('肺 -呼吸音',db_column='breathSoundCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    breathSoundOther = models.CharField('肺呼吸音 异常',db_column='breathSoundOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    raleCode = models.CharField('肺 罗音代码',db_column='raleCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    raleOther = models.CharField('肺 罗音 其他',db_column='raleOther', max_length=60, blank=True, null=True)  # Field name made lowercase.
    heartRate = models.DecimalField('心脏 心率',db_column='heartRate', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rhythmCode = models.CharField('心脏 -心律',db_column='rhythmCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cardiacSouffleCode = models.CharField('心脏 杂音',db_column='cardiacSouffleCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cardiacSouffleDesc = models.CharField('心脏 杂音描述',db_column='cardiacSouffleDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenTendernessCode = models.CharField('腹部 压痛',db_column='abdomenTendernessCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenTendernessDesc = models.CharField('腹部压痛 描述',db_column='abdomenTendernessDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenMassCode = models.CharField('腹部 包块',db_column='abdomenMassCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenMassDesc = models.CharField('腹部 包块 描述',db_column='abdomenMassDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenLiverCode = models.CharField('腹部 肝大',db_column='abdomenLiverCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenLiverDesc = models.CharField('腹部 肝大 描述',db_column='abdomenLiverDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenSplenomegalyCode = models.CharField('腹部 脾大',db_column='abdomenSplenomegalyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenSplenomegalyDesc = models.CharField('腹部 脾大 描述',db_column='abdomenSplenomegalyDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    abdomenShiftingDullnessCode = models.CharField('腹部 -移动性浊音',db_column='abdomenShiftingDullnessCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    abdomenShiftingDullnessDesc = models.CharField('腹部 -移动性浊音描述',db_column='abdomenShiftingDullnessDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    legEdemaCode = models.CharField('下肢水肿',db_column='legEdemaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dorsalisPedisPulseCode = models.CharField('足背动脉',db_column='dorsalisPedisPulseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    analFingerCodes = models.CharField('肛门指诊代码',db_column='analFingerCodes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    breastCodes = models.CharField('乳腺代码',db_column='breastCodes', max_length=32, blank=True, null=True)  # Field name made lowercase.
    breastDesc = models.CharField('乳腺描述',db_column='breastDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    vulvaCode = models.CharField('妇科 外阴代码',db_column='vulvaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vulvaDesc = models.CharField('妇科 外阴描述',db_column='vulvaDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    vaginaCode = models.CharField('妇科 阴道代码',db_column='vaginaCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vaginaDesc = models.CharField('妇科 阴道描述',db_column='vaginaDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cervixCode = models.CharField('妇科 宫颈代码',db_column='cervixCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cervixDesc = models.CharField('妇科 宫颈描述',db_column='cervixDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    uterusCode = models.CharField('妇科 宫体代码',db_column='uterusCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uterusDesc = models.CharField('妇科 宫体描述',db_column='uterusDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    uterineAccessoriesCode = models.CharField('妇科 附件代码',db_column='uterineAccessoriesCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uterineAccessoriesDesc = models.CharField('妇科 附件描述',db_column='uterineAccessoriesDesc', max_length=64, blank=True, null=True)  # Field name made lowercase.
    examinationOther = models.CharField('查体 其他',db_column='examinationOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hemoglobin = models.DecimalField('血常规 -血红蛋白',max_digits=12, decimal_places=0, blank=True, null=True)
    leucocyte = models.DecimalField('血常规 -白细胞',max_digits=12, decimal_places=2, blank=True, null=True)
    platelet = models.DecimalField('血常规-血小板',max_digits=12, decimal_places=2, blank=True, null=True)
    bloodOther = models.CharField('血常规-其他',db_column='bloodOther', max_length=128, blank=True, null=True)  # Field name made lowercase.
    urineProteinCode = models.CharField('尿常规-尿蛋白',db_column='urineProteinCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineSugarCode = models.CharField('尿常规-尿糖',db_column='urineSugarCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineKetoneCode = models.CharField('尿常规-尿酮体',db_column='urineKetoneCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineOccultBloodCode = models.CharField('尿常规-尿潜血',db_column='urineOccultBloodCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    urineOther = models.CharField('尿常规-其他',db_column='urineOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fastingPlasmaGlucose1 = models.DecimalField('空腹血糖mol/L',db_column='fastingPlasmaGlucose1', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fastingPlasmaGlucose2 = models.DecimalField('空腹血糖 mg/L',db_column='fastingPlasmaGlucose2', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ECGCode = models.CharField('心电图代妲代码',db_column='ECGCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ECGDesc = models.CharField('心电图描述',db_column='ECGDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    ECGData = models.TextField('心电图数据',db_column='ECGData', blank=True, null=True)  # Field name made lowercase.
    urineTraceAlbuminCode = models.CharField('尿微量白蛋白',db_column='urineTraceAlbuminCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    fecalOccultBloodCode = models.CharField('大便潜血',db_column='fecalOccultBloodCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    glycatedHemoglobin = models.CharField('糖化血红蛋白',db_column='glycatedHemoglobin', max_length=16, blank=True, null=True)  # Field name made lowercase.
    HBsAgCode = models.CharField('乙肝表面抗原',db_column='HBsAgCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    GPT = models.DecimalField('肝功能-血清谷丙转氨酶',db_column='GPT', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    GOT = models.DecimalField('肝功能-血清谷草转氨酶',db_column='GOT', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    albumin = models.DecimalField('肝功能-白蛋白',max_digits=5, decimal_places=2, blank=True, null=True)
    TBIL = models.DecimalField('肝功能-总胆红素',db_column='TBIL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    DBIL = models.DecimalField('肝功能-结合胆红素',db_column='DBIL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    serumCreatinine = models.DecimalField('肾功能-血清肌酐',db_column='serumCreatinine', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    BUN = models.DecimalField('肾功能-血尿素氮',db_column='BUN', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    serumPotassiumConcentration = models.DecimalField('肾功能 -血钾浓度',db_column='serumPotassiumConcentration', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    serumSodiumConcentration = models.DecimalField('肾功能 -血钠浓度',db_column='serumSodiumConcentration', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    TCHO = models.DecimalField('血脂 -血脂总胆固醇',db_column='TCHO', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    triglyceride = models.DecimalField('血脂 -甘油三脂',max_digits=5, decimal_places=2, blank=True, null=True)
    LDL = models.DecimalField('血脂-血清低密度值蛋白胆固醇',db_column='LDL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    HDL = models.DecimalField('血脂-血清高密度值蛋白胆固醇',db_column='HDL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chestXRayCode = models.CharField('胸部X线片代码',db_column='chestXRayCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chestXRayDesc = models.CharField('胸部X线片（描述）',db_column='chestXRayDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    BScanCode = models.CharField('B超代码',db_column='BScanCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    BScanDesc = models.CharField('B超（描述）',db_column='BScanDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    papSmearCode = models.CharField('宫颈涂片代码',db_column='papSmearCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    papSmearDesc = models.CharField('宫颈涂片（描述）',db_column='papSmearDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    checkOther = models.CharField('辅助检查-其他',db_column='checkOther', max_length=100, blank=True, null=True)  # Field name made lowercase.
    flatAndQualityCode = models.CharField('中医平和质代码',db_column='flatAndQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qiDeficiencyCode = models.CharField('中医气虚质代码',db_column='qiDeficiencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yangXuzhiCode = models.CharField('中医阳虚质代码',db_column='yangXuzhiCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yinDeficiencyCode = models.CharField('中医阴虚质代码',db_column='yinDeficiencyCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    phlegmDampnessQualityCode = models.CharField('中医痰湿质代码',db_column='phlegmDampnessQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hotAndHumidQualityCode = models.CharField('中医热质代码',db_column='hotAndHumidQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bloodStasisCode = models.CharField('医血瘀质代码',db_column='bloodStasisCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qiStagnationCode = models.CharField('中医气郁质代码',db_column='qiStagnationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    specialQualityCode = models.CharField('中医特秉质代码',db_column='specialQualityCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cerebrovascularCodes = models.CharField('脑血管疾病代码',db_column='cerebrovascularCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cerebrovascularDesc = models.CharField('脑血管疾病（补充）',db_column='cerebrovascularDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    kidneyDiseaseCodes = models.CharField('肾脏疾病代码',db_column='kidneyDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kidneyDiseaseDesc = models.CharField('肾脏疾病（补充）',db_column='kidneyDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    heartDiseaseCodes = models.CharField('心脏疾病代码',db_column='heartDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    heartDiseaseDesc = models.CharField('心脏疾病疾病（补充）',db_column='heartDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    vascularDiseaseCodes = models.CharField('血管疾病代码',db_column='vascularDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vascularDiseaseDesc = models.CharField('血管疾病（补充）',db_column='vascularDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    eyeDiseaseCodes = models.CharField('眼部疾病代码（多选）',db_column='eyeDiseaseCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eyeDiseaseDesc = models.CharField('眼部疾病（补充） ',db_column='eyeDiseaseDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    nerveSystemDiseaseCode = models.CharField('神经系统疾病代码',db_column='nerveSystemDiseaseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nerveSystemDiseaseDesc = models.CharField('神经系统疾病（补充）',db_column='nerveSystemDiseaseDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    otherSystemDiseaseCode = models.CharField('其他系统疾病代码',db_column='otherSystemDiseaseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    otherSystemDiseaseDesc = models.CharField('其他系统疾病（补充）',db_column='otherSystemDiseaseDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    hospitalizedHistoryCol = models.TextField('住院史',db_column='hospitalizedHistory', blank=True, null=True)  # Field name made lowercase.
    familyBedHistoryCol = models.TextField('家庭病床史',db_column='familyBedHistory', blank=True, null=True)  # Field name made lowercase.
    medicationListCol = models.TextField('主要用药情况',db_column='medicationList', blank=True, null=True)  # Field name made lowercase.
    vaccinationHistoryCol = models.TextField('非免疫规划预防接种史',db_column='vaccinationHistory', blank=True, null=True)  # Field name made lowercase.
    healthEvaluationCode = models.CharField('健康评价',db_column='healthEvaluationCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    diseaseName1 = models.CharField('健康评价疾病名称1',db_column='diseaseName1', max_length=120, blank=True, null=True)  # Field name made lowercase.
    diseaseName2 = models.CharField('健康评价疾病名称2',db_column='diseaseName2', max_length=120, blank=True, null=True)  # Field name made lowercase.
    diseaseName3 = models.CharField('健康评价疾病名称3',db_column='diseaseName3', max_length=120, blank=True, null=True)  # Field name made lowercase.
    diseaseName4 = models.CharField('健康评价疾病名称4',db_column='diseaseName4', max_length=120, blank=True, null=True)  # Field name made lowercase.
    healthGuidanceCodes = models.CharField('健康指导代码',db_column='healthGuidanceCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    healthGuidanceDesc = models.CharField('健康指导（补充）',db_column='healthGuidanceDesc', max_length=120, blank=True, null=True)  # Field name made lowercase.
    riskFactorsCodes = models.CharField('危险因素控制代码',db_column='riskFactorsCodes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weightReduction = models.CharField('减体重目标',db_column='weightReduction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vaccinationName = models.CharField('建议疫苗接种名称',db_column='vaccinationName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    riskFactorsOther = models.CharField('危险因素控制-其他',db_column='riskFactorsOther', max_length=120, blank=True, null=True)  # Field name made lowercase.
    CreateUser = models.CharField('创建人',db_column='CreateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField('创建时间',db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField('修改人',db_column='UpdateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField('修改时间',db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField('删除人',db_column='DeleteUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField('删除时间',db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbhealExamination'
        verbose_name = '健康体检'
        verbose_name_plural='健康体检'
    def __unicode__(self):
        return self.name


class Tbhospitalizedhistory(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    admissionDate = models.DateField(db_column='admissionDate', blank=True, null=True)  # Field name made lowercase.
    dischargeDate = models.DateField(db_column='dischargeDate', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=100, blank=True, null=True)
    orgName = models.CharField(db_column='orgName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    medicalRecordNumber = models.CharField(db_column='medicalRecordNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    tbhealExamination= models.ForeignKey(Tbhealexamination,related_name='hospitalizedHistory')
    CreateUser = models.CharField(db_column='CreateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16, blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbhospitalizedHistory'

class Tbfamilybedhistory(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    admissionDate = models.DateField(db_column='admissionDate', blank=True, null=True)  # Field name made lowercase.
    dischargeDate = models.DateField(db_column='dischargeDate', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=100, blank=True, null=True)
    orgName = models.CharField(db_column='orgName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    medicalRecordNumber = models.CharField(db_column='medicalRecordNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    tbhealExamination= models.ForeignKey(Tbhealexamination,related_name='familyBedHistory')
    CreateUser = models.CharField(db_column='CreateUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime',blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbfamilyBedHistory'
        
class Tbmedicationlist(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    drugName = models.CharField(db_column='drugName', max_length=50)  # Field name made lowercase.
    usage = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    dosage = models.CharField(max_length=20, blank=True, null=True)
    medicationTime = models.CharField(db_column='medicationTime', max_length=120, blank=True, null=True)  # Field name made lowercase.
    doseCode = models.CharField(db_column='doseCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tbhealExamination= models.ForeignKey(Tbhealexamination,related_name='medicationList')
    CreateUser = models.CharField(db_column='CreateUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime',blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser', max_length=16,blank=True, null=True)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbmedicationList'
class Tbpasthistorylist(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    pastHistoryType = models.CharField('既往史类型',db_column='pastHistoryType', max_length=1)  # Field name made lowercase.
    pastHistoryCode = models.CharField('既往史疾病代码',db_column='pastHistoryCode', max_length=2)  # Field name made lowercase.
    pastHistoryAdd = models.CharField('既往史疾病附加',db_column='pastHistoryAdd', max_length=122, blank=True, null=True)  # Field name made lowercase.
    pastHistoryDate = models.DateField('既往史日期',db_column='pastHistoryDate', blank=True, null=True)  # Field name made lowercase.  
    tbhealthRecord = models.ForeignKey(Tbhealthrecord,related_name='pastHistoryList')
    
    class Meta:
        managed = True
        db_table = 'TbpastHistoryList'
        verbose_name = '既往病史'
    def __unicode__(self):
        return self.pastHistoryAdd
    
class Vip(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)
    name=models.CharField(db_column='Name', max_length=60, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'TbVIP'
        verbose_name = 'VIP用户列表'
    def __unicode__(self):
        return self.name
class Tbvaccinationhistory(models.Model):
    ID = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    inoculationName = models.CharField(db_column='inoculationName', max_length=120)  # Field name made lowercase.
    inoculationDate = models.DateField(db_column='inoculationDate', blank=True, null=True)  # Field name made lowercase.
    orgName = models.CharField(db_column='orgName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tbhealExamination= models.ForeignKey(Tbhealexamination,related_name='vaccinationHistory')
    CreateUser = models.CharField(db_column='CreateUser',  blank=True, null=True,max_length=16)  # Field name made lowercase.
    CreateTime = models.DateField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    UpdateUser = models.CharField(db_column='UpdateUser',  blank=True, null=True,max_length=16)  # Field name made lowercase.
    UpdateTime = models.DateField(db_column='UpdateTime', blank=True, null=True)  # Field name made lowercase.
    DeleteUser = models.CharField(db_column='DeleteUser',  blank=True, null=True,max_length=16)  # Field name made lowercase.
    DeleteTime = models.DateField(db_column='DeleteTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TbvaccinationHistory'





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

class YTJMeasure(models.Model):
    ID=models.AutoField(db_column='ID',primary_key=True)
    personProfile = models.ForeignKey(UserProfile,related_name='YTJMeasure_personId',db_column='personProfile',default=12,verbose_name = '居民个人ID')
    idCard=models.CharField("身份证号码",db_column='idCard', max_length=18, blank=True, null=True)
    machineCode = models.CharField('健康一体机编码',db_column='machineCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    householdRegisterCode =  models.ForeignKey(Tbarea,related_name='YTJMeasure_Area',db_column='householdRegisterCode',default=11,verbose_name = '所属区域')
    responsibleDoctorCode = models.ForeignKey(UserProfile,related_name='YTJMeasure_Doctor_ID',db_column='responsibleDoctorCode',default=2,verbose_name = '责任医生')
    organization=models.ForeignKey(Tbmedicalorganization,related_name='YTJMeasure_organization',db_column='organization',default=17,verbose_name = '医疗机构')  # Field name made lowercase.
    name=models.CharField('姓名',max_length=20,blank= True,null=True)
    genderCode = models.CharField('性别',db_column='genderCode', max_length=1,blank=True, null=True)
    time=models.DateTimeField('测量时间',blank=True,null=True)
    data=JSONField()
    class Meta:
        managed = True
        db_table = 'YTJMeasure'
        verbose_name = '一体机测量'
        verbose_name_plural = '一体机测量'
    def __unicode__(self):
      return self.name

