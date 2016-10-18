from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import View

from mysite.models import Question, MyHome
from mysite.serializers import QuestionSerializer, MyHomeSerializer #, ChoiceSerializer

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




class DRFView(APIView):

	template_name = 'drf.html'

	def get(self, request, format=None):
		if request.is_ajax():
			return Response({'data': 'Ajax call'})
		# print request.GET.get('longitude', None)	
		# print(request.data)
		serializer = MyHomeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			homes = MyHome.objects.all()
			homes_serializer = MyHomeSerializer(homes, many=True)
			data = homes_serializer.data
			return Response({'data': data})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


		# questions = Question.objects.all()
		# questions_serializer = QuestionSerializer(questions, many=True)
		# data = questions_serializer.data
		# homes = MyHome.objects.all()
		# homes_serializer = MyHomeSerializer(homes, many=True)
		# data = homes_serializer.data
		# return Response({'data': data})



	def post(self, request):

		if request.is_ajax():
			return Response({'data': 'Ajax call'})
		MyHome.objects.all().delete()
		serializer = MyHomeSerializer(data=request.data)
		if serializer.is_valid():
			print(serializer)
			serializer.save()
			homes = MyHome.objects.all()
			homes_serializer = MyHomeSerializer(homes, many=True)
			data = homes_serializer.data
			return Response ({'data': data})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)