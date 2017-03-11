# -*- coding:utf-8 -*- 
from django.contrib import admin

# Register your models here.
from models import *
from admin_form import *

#===============================================================================
# 注册模块
#===============================================================================
admin.site.unregister(User)#
admin.site.register(User, CustomUserAdmin)#重新定制User
admin.site.register(Tbhealthrecord,Customhealthrecord) #定制健康档案
admin.site.register(Tbhealexamination,Customhealexamination)#定制健康体检
admin.site.register(Tbarea)#行政区域
admin.site.register(UserProfile)#扩展User
admin.site.register(Tbhypertensionflup,Customhypertensionflup)#高血压随访记录
admin.site.register(Tbmedicalorganization)#用药情况
admin.site.register(Tbdiabetesflup,Customdiabetflup)#糖尿病随访记录
admin.site.register(YTJMeasure)#一体机测量
# per=Permission.objects.all()
# for each in per:
#     perm=Permission.objects.get(id=each.id)
#     if 'add' in perm.name:
#         perm.name='增加'
#     if 'change' in perm.name:
#         perm.name='修改'
#     if 'add' in perm.name:
#         perm.name='删除'