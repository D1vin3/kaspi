import datetime
from django.contrib.gis import geos
# from django.contrib.db import models
# superr - parrent(adj)
# *args - tuple, **kwargs - dict, etc
from django.contrib.gis.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=120)
	pub_date = models.DateTimeField(default=timezone.now)

	def was_published_recently(self):
		return self.pub_date == timezone.now() - datetime.timedelta

		class Meta:
			verbose_name = 'Question'
			verbose_name_plural = 'Questions'

		def __unicode__(self):
			return unicode(self.question_text)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)	

	# ORM  - models, migrations

class MyHome(models.Model):
	address = models.CharField(max_length=1000, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	point = models.PointField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if self.latitude and self.longitude:
			self.point = geos.Point(self.longitude, self.latitude)
		return super(MyHome, self).save(*args, **kwargs)


