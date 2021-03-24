from django.db import models

# Create your models here.

class Orthoepy(models.Model):
	name_stressed = models.CharField(max_length=100, null=True)
	name_stressed_wrong = models.CharField(max_length=100, null=True)
	mistakes = models.IntegerField(null=False, default = 0)
	total_count = models.IntegerField(null=False, default = 0)

	def __str__(self):
		return self.name_stressed

class Spelling(models.Model):
	name = models.CharField(max_length=100, null=True)
	name_with_blanks = models.CharField(max_length=100, null=True)
	mistakes = models.IntegerField(null=False, default = 0)
	total_count = models.IntegerField(null=False, default = 0)

	def __str__(self):
		return self.name

class Punctuation(models.Model):
	text = models.CharField(max_length=100, null=True)
	comma_pos = models.CharField(max_length=100, null=True)
	mistakes = models.IntegerField(null=False, default = 0)
	total_count = models.IntegerField(null=False, default = 0)

	def __str__(self):
		return self.text