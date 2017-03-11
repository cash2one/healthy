#-*- coding: utf-8 -*-
'''
Created on 2016年3月15日

此文件是定制admin内容
@author: 刘浩东
'''

from django.contrib import admin
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from models import *
import time
import datetime
#===============================================================================
# 在电子健康档案下方显示既往病史，用Django的stack inline实现
#  显示外键下拉框      登录名       责任医生
#===============================================================================
class pasthistorylist(admin.StackedInline):#在电子健康档案上显示既往病史
    model=Tbpasthistorylist
    extra=0

class Customhealthrecord(admin.ModelAdmin):
    inlines=[pasthistorylist]
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
        if db_field.name == "responsibleDoctorCode": #在电子健康档案的责任医生下拉框中显示类型为医生的          type 为0表示管理员   为1表示医生   2表示患者
            kwargs["queryset"] =UserProfile.objects.filter(type='1')  #选择医生
#             print db_field
        if db_field.name == "personProfile":
            kwargs["queryset"] =UserProfile.objects.filter(type='2')  #选择患者
        return super(Customhealthrecord, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def save_model(self, request, obj, form, change):
        name= obj.responsibleDoctorCode.user.last_name+obj.responsibleDoctorCode.user.first_name
        obj.responsibleDoctorName =name
        obj.nowLiveCode=obj.householdRegisterCode.ID
        obj.nowLiveName= obj.householdRegisterCode.areaName
        obj.nowLiveAddr= obj.householdRegisterCode.areaName
        if(len(obj.healthFileNumber)<10):
            obj.healthFileNumber=str(int(time.time()))+str(datetime.datetime.now().microsecond)
        
        obj.save()
    def get_form(self, request, obj, **kwargs):
        self.exclude = ("responsibleDoctorName", )
        form = super(Customhealthrecord, self).get_form(request, obj, **kwargs)
        return form
#===============================================================================
# 在user界面显示扩展的字段
#===============================================================================
class ProfileInline(admin.StackedInline):#在User界面显示
    model = UserProfile
    #fk_name = 'user'
    max_num = 1
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    
#===============================================================================
# 健康体检 相关操作
#===============================================================================
class Customhealexamination(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "responsibleDoctorCode": #在电子健康档案的责任医生下拉框中显示类型为医生的          type 为0表示管理员   为1表示医生   2表示患者
            kwargs["queryset"] =UserProfile.objects.filter(type='1')  #选择医生
#             print db_field
        if db_field.name == "personProfile":
            kwargs["queryset"] =UserProfile.objects.filter(type='2')  #选择患者 
        return super(Customhealexamination, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def save_model(self, request, obj, form, change):
        name= obj.responsibleDoctorCode.user.last_name+obj.responsibleDoctorCode.user.first_name
        obj.responsibleDoctorName =name
        obj.householdRegisterName= obj.householdRegisterCode.areaName
        obj.householdRegisterAddr= obj.householdRegisterCode.areaName
        if(len(obj.healthFileNumber)<10):
            obj.healthFileNumber=str(int(time.time()))+str(datetime.datetime.now().microsecond)
        obj.save()
    def get_form(self, request, obj, **kwargs):
        self.exclude = ("responsibleDoctorName", )
        form = super(Customhealexamination, self).get_form(request, obj, **kwargs)
        return form
#===============================================================================
# 高血压随访记录相关操作
#===============================================================================
class medicationlist(admin.StackedInline):#在高血压随访记录下方显示用药情况
    model=Dicmedicationlist
    extra=0
class Customhypertensionflup(admin.ModelAdmin): 
    inlines = [medicationlist]
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "responsibleDoctorCode":#在高血压随访记录的责任医生下拉框中显示类型为医生的记录。
             kwargs["queryset"] =UserProfile.objects.filter(type='1')  #选择医生
    
        if db_field.name == "personProfile":#选择患者，一旦选择某个用户，该用户登陆网站就会看到这条记录。
            kwargs["queryset"] =UserProfile.objects.filter(type='2')  #选择患者
        return super(Customhypertensionflup, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
    
    
#===============================================================================
# 糖尿病随访记录相关操作
#===============================================================================
class Customdiabetflup(admin.ModelAdmin):
    inlines=[medicationlist]
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "responsibleDoctorCode":#在高血压随访记录的责任医生下拉框中显示类型为医生的记录。
             kwargs["queryset"] =UserProfile.objects.filter(type='1')  #选择医生
    
        if db_field.name == "personProfile":#选择患者，一旦选择某个用户，该用户登陆网站就会看到这条记录。
            kwargs["queryset"] =UserProfile.objects.filter(type='2')  #选择患者
        return super(Customdiabetflup, self).formfield_for_foreignkey(db_field, request, **kwargs)