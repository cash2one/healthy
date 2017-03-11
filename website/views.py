# -*- coding:utf-8 -*- 
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import template
from django.template.loader import get_template 
from django.template.context import Context, RequestContext
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group,Permission
import json
import os
from django.core import serializers
from models import *
from website.filter import *
from django.contrib.auth.models import User,Group
import uuid
from matplotlib.axis import XAxis
#import pandas as pd
# Create your views here.
#===============================================================================
# #未完成的功能
#===============================================================================
def todo(request):
    return render(request,"base.html",{})
#===============================================================================
#基本上每个表都有三个页面:list,qlist,details。 每张表的格式都相似
#===============================================================================
#===============================================================================
# 成人健康体检查询  
#===============================================================================
@login_required
def phy_list(request):
    Author_word = 'website.change_tbhealexamination'
    navigation = '成人健康体检'
    if request.user.has_perm(Author_word): 
        #arealist1、2、3 是县镇乡三级区域
        arealist1 = Tbarea.objects.filter(areaType__exact=20)#户籍地址
        arealist2 = Tbarea.objects.filter(areaType__exact=21)#乡村街道
        arealist3 = Tbarea.objects.filter(areaType__exact=22)#村
        orglist = Tbmedicalorganization.objects.all()
        area = { 'arealist1':arealist1,'arealist2':arealist2,'arealist3':arealist3,'orglist':orglist}
        return render(request,'phy/phy_list.html',{ 'key_name':navigation, 'area':area})
    else:
        return render(request,"authority.html",{})
#===============================================================================
# #显示查询列表（查询函数，结果列表的模板名）
#===============================================================================
def phy_list_q(request):
    if request.method == 'POST':
        dict = request.POST        #获取post所有参数
        (num,records) = healExaminationCheck(dict,int(dict['page_n']),int(dict['nperpage']),request.user) #查询函数，来自filter，根据user获取相应权限的结果
        d=get_template("phy/phy_qlist.html")
        c = {"records":records}
        html = d.render(c)
    #   c = RequestContext(request, {"records":records})/c = Context({"records":records}) # 有警告(RemovedInDjango110Warning) render() must be called with a dict, not a RequestContext ；原因是Passing RequestContext to Template.render is deprecated, see django/django#3883
    #   html = render(request,"qlist_pages/phy_qlist.html",{"records":records}) #返回HttpResponse,不能被序列化  <HttpResponse > is not JSON serializable
        data2 = {'html':html,'number':num}
        d1 = json.dumps(data2)
        return HttpResponse(d1)  
    else:
        return HttpResponse("<p>请求错误</p>")
#===============================================================================
# 详细信息，和查询列表对应
#===============================================================================

def phy_details(request,id):
    try:
        records = healExaminationCheck_Detail(int(id))
        hospitalizedHistory_list =records.hospitalizedHistory.all() #住院史
        familyBedHistory_list=records.familyBedHistory.all()#家庭病床史
        medical_list=records.medicationList.all()#用药历史
        vaccinationHistory_list=records.vaccinationHistory.all()#非免疫规划预防接种史 
        Navigation = {'first':'首页','second': '业务处理 '}
        return render(request,"phy/phy_details.html",{'navigation':Navigation,'key_name':'成人健康体检表','record':records,
                                  'hospitalizedHistory_list':hospitalizedHistory_list,
                                  'familyBedHistory_list':familyBedHistory_list,
                                  'medicationList_list':medical_list,
                                  'vaccinationHistory_list':vaccinationHistory_list,
                                  })
    except:
        print "错误：phy_details(views)"
        return 0

  
 #==============================================================================
 # # 电子健康档案查询
 #==============================================================================
@login_required
def ehr_list(request):
    Author_word = 'website.change_tbhealthrecord'
    navigation = '电子健康档案'
    if request.user.has_perm(Author_word): 
        #arealist1、2、3 是县镇乡三级区域
        arealist1 = Tbarea.objects.filter(areaType__exact=20)#户籍地址
        arealist2 = Tbarea.objects.filter(areaType__exact=21)#乡村街道
        arealist3 = Tbarea.objects.filter(areaType__exact=22)#村
        orglist = Tbmedicalorganization.objects.all()
        area = { 'arealist1':arealist1,'arealist2':arealist2,'arealist3':arealist3,'orglist':orglist}
        return render(request, 'ehr/ehr_list.html', { 'key_name':navigation,'area':area})
    else:
        return render(request, 'authority.html', {})
def ehr_list_q(request):
    if request.method == 'POST':
        dict = request.POST        #获取post所有参数
        (num,records) = healthRecordCheck(dict,int(dict['page_n']),int(dict['nperpage']),request.user)
        d=get_template("ehr/ehr_qlist.html")
        c = {"records":records}
        html = d.render(c)
        data2 = {'html':html,'number':num}
        d1 = json.dumps(data2)
        return HttpResponse(d1)  
    else:
        return HttpResponse("<p>请求错误</p>")
def ehr_details(request,id):
    try:
        records = helthRecordCheck_Detail(id)
        historys=history_read(id)
    #    print records
    #    print "======================================"
    #    records = Tbhealthrecord.objects.filter(healthFileNumber__exact=id)
        Navigation = {'first':'首页','second': '业务处理 '}
        return render(request, 'ehr/ehr_details.html',{'navigation':Navigation,'key_name':'个人基本信息','record':records,'historys':historys})
    except:
        print "错误：ehr_details （views）函数"
        return 0

#===============================================================================
# 高血压随访记录：hypet
#===============================================================================
@login_required
def hypet_list(request):
    Author_word = 'website.change_tbhypertensionflup'
    navigation = '高血压随访记录'
    if request.user.has_perm(Author_word): 
        return render(request,'hypet/hypet_list.html',{ 'key_name':navigation,})
    else:
        return render(request, 'authority.html', {})
def hypet_list_q(request):
    if request.method == 'POST':
        dict = request.POST        #获取post所有参数
        (num,records) = hypertensionflupCheck(dict,int(dict['page_n']),int(dict['nperpage']),request.user)
        d=get_template("hypet/hypet_qlist.html")
        c = {"records":records}
        html = ''
        if num != 0:
            html = d.render(c)
        data2 = {'html':html,'number':num}
        d1 = json.dumps(data2)
        return HttpResponse(d1)  
    else:
        return HttpResponse("<p>请求错误</p>")
def hypet_details(request,id):
    try:
        records = Tbhypertensionflup.objects.get(ID=id)
        d=get_template("hypet/hypet_details.html")
        Navigation = {'first':'首页','second': '业务处理 '}
        return render(request,"hypet/hypet_details.html",{'navigation':Navigation,'key_name':'高血压患者随访服务记录表','record':records})
    except:
        print "错误：ehr_details （views）函数"
        return 0

#===============================================================================
# 糖尿病人随访记录查询
#===============================================================================
@login_required
def diabet_list(request):
    Author_word = 'website.change_tbdiabetesflup'
    navigation = '糖尿病随访记录'
    if request.user.has_perm(Author_word): 
        return render(request,'diabet/diabet_list.html',{ 'key_name':navigation,})
    else:
        return render(request, 'authority.html', {})
def diabet_list_q(request):
    if request.method == 'POST':
        dict = request.POST        #获取post所有参数
        (num,records) = diabetesflupCheck(dict,int(dict['page_n']),int(dict['nperpage']),request.user)
        d=get_template("diabet/diabet_qlist.html")
        c = {"records":records}
        if num !=0:
            html = d.render(c)
        else:
            html = ''
        data2 = {'html':html,'number':num}
        d1 = json.dumps(data2)
        return HttpResponse(d1)  
    else:
        return HttpResponse("<p>请求错误</p>")
def diabet_details(request,id):
    try:  
        records = Tbdiabetesflup.objects.get(ID=id)
        d=get_template("diabet/diabet_details.html")
        c=RequestContext(request,{'key_name':'糖尿病患者随访服务记录表','record':records,})
        #return HttpResponse(d.render(c))
        return render(request,"diabet/diabet_details.html",{'key_name':'糖尿病患者随访服务记录表','record':records,})
    except:
        print "错误：ehr_details （views）函数"
        return 0

#@login_required
#@permission_required('website.change_tbarea')
def area_manager(request):
    Author_word = 'website.change_tbarea'
    if request.user.has_perm(Author_word): 
        area=Tbarea.objects.get(ID=4)
        d=get_template("area_manager.html")
        c=RequestContext(request,{'area':area})
        return HttpResponse(d.render(c))
    else:
        d=get_template("authority.html")
        c=RequestContext(request,{})
        return HttpResponse(d.render(c))  
def update_area(request):
#     request.POST["state"]=='0':只是查数据库返回，1修改数据库返回，2添加数据库返回
    if request.method == 'POST':
        arguments = request.POST
        try:
            
            if arguments["state"]=='1':#修改数据库

                a = Tbarea.objects.filter(areaCode__exact=arguments["codeold"])[0]#areaCode是唯一的
                a.areaName = arguments["name"]
                a.areaCode = arguments["code"]
                try:
                    a.areaType = int(arguments["type"]) #这个字段是整形的//且必须非空
                except TypeError:
                    print "错误：类型错误"
                print arguments
                a.save()
            if arguments["state"]=='2':#插入  新增下级区域
                p = Tbarea(areaName=arguments["name"],areaCode = arguments["code"],areaType = arguments["type"],parentAreaCode=arguments["codeparent"]) 
                p.save()  
            userProfile=UserProfile.objects.get(user=request.user)
            print userProfile.areaCode
            areas=Tbarea.objects.filter(areaCode__startswith=userProfile.areaCode)
            arealist0=[]
            arealist1=[]
            arealist2=[]
            arealist3=[]
            for each in areas:
                if(each.areaType==19):
                    arealist0.append(each)
                if(each.areaType==20):
                    arealist1.append(each)
                if(each.areaType==21):
                    arealist2.append(each)
                if(each.areaType==22):
                    arealist3.append(each)
            
        except:
            print "error：数据库错误（update_area）"
            return HttpResponse("<p>数据库错误</p>")
        print "访问update_area函数"
        d=get_template("area_tree.html")
        c=RequestContext(request,{'arealist0':arealist0,'arealist1':arealist1,'arealist2':arealist2,'arealist3':arealist3,})
        #c=RequestContext(request,{'areas':areas,'Type':area.areaType,})
        html = d.render(c)
        data2 = {'html':html,'number':"test"}
        d1 = json.dumps(data2)#这样json传递一个模板和一个数字
        return HttpResponse(d1)
    else:
        print "error：请求错误（phy_list_q）"
        return HttpResponse("<p>请求错误</p>")
    
def update_org(request):
#     request.POST["state"]=='0':只是查数据库返回，1修改数据库返回，2添加数据库返回
    if request.method == 'POST':
        arguments = request.POST
        try:
            if arguments["state"]=='1':
                a = Tbmedicalorganization.objects.filter(orgCode__exact=arguments["code"])[0]#areaCode是唯一的
                a.orgName=arguments["name"]
                a.save()
            if arguments["state"]=='2':
                p=Tbmedicalorganization(orgCode=uuid.uuid1(),#orgCode=arguments["code"],#uuid 为自动生成的编码
                                        orgName=arguments["name"],orgType=arguments["type"],
                                        parentOrgCode=arguments["codeparent"],areaCode=arguments["areacode"],levelOrder=arguments["levelorder"])
                #整形变量，需要调整类型
                p.save()
            orglist = Tbmedicalorganization.objects.filter(areaCode__exact=arguments["areacode"])
        except Exception, e:
            print "error：数据库错误（update_org）",e
            return HttpResponse("<p>数据库错误</p>")
        print "访问update_org函数"
        d=get_template("area_org_list.html")
        c=RequestContext(request,{'orglist':orglist})
        html = d.render(c)
        data2 = {'html':html }
        d1 = json.dumps(data2)#这样json传递一个模板和一个数字
        return HttpResponse(d1)
    else:
        print "error：请求错误（update_org）"
        return HttpResponse("<p>请求错误</p>")
    
def JKCL_list(request):
    navigation = '健康测量'
    return render(request,'JKCL/JKCL_list.html',{ 'key_name':navigation,})
def JKCL_list_q(request):

    if request.method == 'POST':
        dict = request.POST        #获取post所有参数
         
        (num,records) = YTJMeasureCheck(dict,int(dict['page_n']),int(dict['nperpage']),request.user)
        print "7/4:",records
        print num
        d=get_template("JKCL/JKCL_qlist.html")
        html = d.render({"records":records})
        data2 = {'html':html,'number':num}
        d1 = json.dumps(data2)
        return HttpResponse(d1)  
    else:
        return HttpResponse("<p>请求错误</p>") 
def JKCL_details(request,idCard):
    navigation = '健康测量'
    return render(request,'JKCL/JKCL_details.html',{ 'key_name':navigation,'idCard':idCard,})
def JKCL_details_q(request):
    dic = request.POST
    DIC = {'idCard':dic['idCard'],
           'filter':json.loads(dic['filter']),
           'item':[json.loads(dic['item'])],
           'start':dic['start'],
           'end':dic['end']
           }
    result = JKCL_Check(DIC)
    data3 = serializers.serialize('json',result)
    print data3
    return HttpResponse(data3)

def test(request):
    try:
        #records=YTJMeasure.objects.filter(data__has_key='weight')
        
        #records=YTJMeasure.objects.filter(data__has_key='weight')
        
        #records=YTJMeasure.objects.filter(data__weight__has_key='80')#只要weight有80就可以，value如果是列表也可以
        
        #records=YTJMeasure.objects.filter(data__has_any_keys=['jaskdfj','weight'])#只要满足查询参数列表的一条即可
        #records=YTJMeasure.objects.filter(data__weight__has_any_keys=['79','81'])
        #records=YTJMeasure.objects.filter(data__has_keys=['weight','diabet'])
        records=YTJMeasure.objects.all()
        for each in records:
            print each.name,each.data
    except:
        print "**********wrong in YTJtest*************"
    return HttpResponse("hello world")
#     try:
#         ytj=YTJMeasure(name="李四",time="2016-3-29",data={'sbp':'120','dbp':'80','diabet':'12','weight':'80'})
#         ytj.save()
#     except:
#         print "test wrong"
#    d=get_template("details_pages/YTJMeasure_details.html")
#    c=RequestContext(request,{})
#     date=pd.read_csv("E://healthy/trunk/healthy/website/area_code.csv",encoding='gbk')
#     print date["name"]
#     print len(date)
#     print "nnn",date.loc[5]["name"]
#     try:
#         for i in range(len(date)):
#             print i
#             name=date.loc[i]["name"]
#             record=Tbmedicalorganization(orgCode=str(uuid.uuid1()),
#                                          orgName=name,
#                                          orgType='13',
#                                          parentOrgCode="83eda4c5-faf1-11e5-937d-f8bc12a0bbdc",
#                                          areaCode=date.loc[i]["code"],
#                                          levelOrder=1)
#             record.save()
#     except:
#         print "**********wrong in insert Tbmedicalorganization********"
#    return HttpResponse(d.render(c))


