#-*- coding: UTF-8 -*-
import time
import base64
from types import NoneType
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.backends.db import SessionStore
from api.xinruishi.convert import ConvertProtocol
from api.xinruishi.serializers import YTJMeasureSeri

apiSessionExpireTime = 30 * 60 # usually smaller than global session expire time

def saveToSession(key, value):
    sess = SessionStore()
    sess[key] = value
    sess.save()
    return sess

def getValueFromSession(sessionKey):
    try:
        sess = Session.objects.get(pk=sessionKey)
        if type(sess) != NoneType:
            authorize = sess.get_decoded()
            uId = authorize.keys()[0]
            expireTimestamp = authorize.values()[0]
            if time.time() < expireTimestamp:
                return uId
        return None
    except:
        return None

@csrf_exempt # not using CSRF protection
def YTJMeasureView(request):
    response = HttpResponse()        
    uId = getValueFromSession(request.META.get("HTTP_NZTOKEN"))
    if type(uId) == NoneType:
        response.status_code = 449 # session is expired
        return response
    newData = ConvertProtocol().convert(request.body)
    seriResult = YTJMeasureSeri(data=newData, many=True, context=uId)
    if seriResult.is_valid():
        print "XinRuiShi API alert:: Create new measure records."
        seriResult.save()
        response.status_code = 200 # OK
    else:
        print "XinRuiShi API ERROR:: Data is not valid."
        response.status_code = 500 # server error
    return response

@csrf_exempt # not using CSRF protection
def UserLogin(request): # HTTPS require
    authorizeToken = base64.decodestring(request.META.get("HTTP_AUTHORIZATION")[6:])
    username, password = authorizeToken.split(":")
    response = HttpResponse()
    try:
        userObj = User.objects.get(username=username)
        if userObj.check_password(password):
            print "XinRuiShi API alert:: Login success. Welcome %s." % username
            expireTimestamp = time.time() + apiSessionExpireTime
            sess = saveToSession(userObj.id, expireTimestamp)
            response.status_code = 200 # OK
            response["nztoken"] = sess.session_key
        else:
            print "XinRuiShi API alert:: Login password is wrong."
            response.status_code = 401 # authorize error
            pass
    except User.DoesNotExist:
            print "XinRuiShi API alert:: Login user does not exist."
            response.status_code = 401 # authorize error
            pass
    return response


