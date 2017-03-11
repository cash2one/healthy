#-*- coding: UTF-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from website.models import YTJMeasure
from website.models import UserProfile

class YTJMeasureListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        record = YTJMeasure.objects.create(**(validated_data[0]))
        userId = self.context[0]
        userObj = User.objects.get(id=userId)
        userProfileObj = UserProfile.objects.get(user=userObj)        
        if userProfileObj is not None:
            record.personProfile = userProfileObj
        record.save()
        return record

class YTJMeasureSeri(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = YTJMeasureListSerializer
        model = YTJMeasure
        # Foreign key fields are personProfile, householdRegisterCode, responsibleDoctorCode.
        fields = ('personProfile', 'idCard', 'machineCode', 'householdRegisterCode', 'responsibleDoctorCode',
                  'organization', 'name', 'genderCode', 'time', 'data')
        

