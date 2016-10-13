from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from mysite.models import Question
from mysite.serializers import QuestionSerializer#, ChoiceSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

def index(request):
	return HttpResponse('Hello world')

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'detail.html', {'question': question})


class GreetingView(View):
	greeting = 'Good Day'
	template_name = 'index.html'

	def get(self, request):
		return render(request, self.template_name, {'greeting': self.greeting})


# Django Rest Framework  DRF
class DRFView(APIView):
	template_name = 'drf.html';

	def get(self, request, format=None):
		questions = Question.objects.all()
		questions_serializer = QuestionSerializer(questions, many=True)
		data = questions_serializer.data

		return Response({'data': data})


	def post(self, request):
		serializer = QuestionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			questions = Question.objects.all()
			questions_serializer = QuestionSerializer(questions, many=True)
			data = questions_serializer.data
			return Response ({'data': data})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)