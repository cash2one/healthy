#-*- coding: utf-8 -*-
"""healthy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include

from django.contrib import admin
from rest_framework import routers

import website.views
import api.chongqing.views
import api.xinruishi.views

urlpatterns = [
    url(r'^admin/website/tbhealexamination/$', website.views.phy_list,name='phy_list' ), #重新定向 健康体检
    url(r'^admin/website/tbhealthrecord/$', website.views.ehr_list,name='ehr_list' ),#重新定向 健康档案
    url(r'^admin/website/tbhypertensionflup/$', website.views.hypet_list,name='hypet_list' ),#重新定向高血压随访记录
    url(r'^admin/website/tbdiabetesflup/$', website.views.diabet_list,name='diabet_list' ),#重新定向糖尿病随访记录
   
    
    url(r'^area_manager/$', website.views.area_manager, name='area_manager' ),
    url(r'^update_area/$', website.views.update_area, name='update_area' ),
    url(r'^update_org/$', website.views.update_org, name='update_org' ),
    url(r'^todo/', website.views.todo, name='todo' ), #未完成功能页面
    url(r'^$', website.views.phy_list,name='phy' ), #默认页面
    
    url(r'^phy_list/', website.views.phy_list,name='phy_list' ),   # 成人健康体检查询、
    url(r'^phy_list_q/', website.views.phy_list_q,name='phy_list_q' ),   # 成人健康体检查询、   
    url(r'^phy_details/(\d+)/$', website.views.phy_details, name='phy_details' ), # 详细信息
    
    url(r'^ehr_list/', website.views.ehr_list, name='ehr_list' ),  # 电子健康档案查询
    url(r'^ehr_list_q/', website.views.ehr_list_q, name='ehr_list_q' ),  # 电子健康档案查询
    url(r'^ehr_details/(\d+)/$',website.views.ehr_details,name='ehr_details' ), # 个人基本信息
     
    url(r'^hypet_list/', website.views.hypet_list, name='hypet_list' ),  # 高血压随访
    url(r'^hypet_list_q/', website.views.hypet_list_q, name='hypet_list_q' ),  # 高血压随访
    url(r'^hypet_details/(\d+)/$',website.views.hypet_details,name='hypet_details' ), # 高血压随访
     
    url(r'^diabet_list/', website.views.diabet_list, name='diabet_list' ),  # 糖尿病随访
    url(r'^diabet_list_q/', website.views.diabet_list_q, name='diabet_list_q' ),  # 糖尿病随访
    url(r'^diabet_details/(\d+)/$',website.views.diabet_details,name='diabet_details' ), #糖尿病随访    
    
    url(r'^JKCL_list/', website.views.JKCL_list, name='JKCL_list' ),  # 健康测量
    url(r'^JKCL_list_q/', website.views.JKCL_list_q, name='JKCL_list_q' ),  # 健康测量
    url(r'^JKCL_details/(\d+)/$',website.views.JKCL_details,name='JKCL_details' ), # 健康测量
    url(r'^JKCL_details_q/$',website.views.JKCL_details_q,name='JKCL_details_q' ), # 健康测量

    # ChongQing API (Web Service over SOAP)
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/test/$', api.chongqing.views.TestView.as_view()),
    url(r'^api/PlatformService.wsdl', api.chongqing.views.dispatcher_handler, name='soap'),
    # XinRuiShi API (REST over HTTP)
    url('bizservice2', api.xinruishi.views.YTJMeasureView),
    url(r'^nruaservice/', api.xinruishi.views.UserLogin),
    
    url(r'^admin/', include(admin.site.urls)),  

#     url(r'^aged_list/', website.views.aged_list, name='aged_list' ),  # 老年人随访
#     url(r'^aged_details/(\d+)/$',website.views.aged_details,name='aged_details' ), #老年人随访
    ]
