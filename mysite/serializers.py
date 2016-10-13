#encoding: UTF-8
from rest_framework import serializers
# from django.db import models

from mysite.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Question