from rest_framework import serializers
from .models import *

class OrthoepySerializer(serializers.ModelSerializer):
	class Meta:
		model = Orthoepy
		fields = '__all__'

class SpellingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Spelling
		fields = '__all__'

class PunctuationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Punctuation
		fields = '__all__'