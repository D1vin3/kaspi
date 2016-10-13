#encoding: UTF-8
from rest_framework import serializers
# from django.db import models

from mysite.models import Question, Choice, MyHome
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class QuestionSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Question

class MyHomeSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = MyHome
        geo_field = "point"