from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
import json

models_ = {
	'Orthoepy': Orthoepy,
	'Spelling': Spelling,
	'Punctuation': Punctuation,
}

# Create your views here.

# служебный функции
def get_amount_and_level(request):
	try:
		amount = int(request.GET.get('amount'))
	except:
		amount = None

	try:
		level = int(request.GET.get('level'))/100
	except:
		level = None
	return amount, level


# views
def landing_page(request):
	return render(request, 'front/about.html')

def exercises(request):
	try:
		_type = request.GET.get('type')
	except:
		_type = None
	print(_type)

	return render(request, 'front/tests.html', {'type': _type})

def orthoepy_page(request):
	amount, level = get_amount_and_level(request)

	if level != None:
		all_words = Orthoepy.objects.all()
		words = []
		for word in all_words:
			print(word)
			if word.total_count == 0:
				if 0.5 >= level:
					words.append(word)
			elif word.mistakes/word.total_count >= level:
				words.append(word)
			if amount!=None and len(words)==amount:
				break
		if len(words) == 0:
			return redirect("/exercises?type=_orthoepy")
	else:
		words = Orthoepy.objects.all()
		print(words)

	words_serialized = OrthoepySerializer(words, many=True)
	return render(request, 'front/orthoepy.html', {'data': words_serialized.data})

def spelling_page(request):
	amount, level = get_amount_and_level(request)

	if level != None:
		all_words = Spelling.objects.all()
		words = []
		for word in all_words:
			print(word)
			if word.total_count == 0:
				if 0.5 >= level:
					words.append(word)
			elif word.mistakes/word.total_count >= level:
				words.append(word)
			if amount!=None and len(words)==amount:
				break
		if len(words) == 0:
			return redirect("/exercises?type=_spelling")
	else:
		words = Spelling.objects.all()
		print(words)
	words_serialized = SpellingSerializer(words, many=True)
	return render(request, 'front/spelling.html', {'data': words_serialized.data})

def punctuation_page(request):
	amount, level = get_amount_and_level(request)

	if level != None:
		all_words = Punctuation.objects.all()
		words = []
		for word in all_words:
			print(word)
			if word.total_count == 0:
				if 0.5 >= level:
					words.append(word)
			elif word.mistakes/word.total_count >= level:
				words.append(word)
			if amount!=None and len(words)==amount:
				break
		if len(words) == 0:
			return redirect("/exercises?type=_punctuation")
			# return render(request, 'front/tests.html', {'type': 'no records'})
	else:
		words = Punctuation.objects.all()
		print(words)

	words_serialized = PunctuationSerializer(words, many=True)
	return render(request, 'front/punctuation.html', {'data': words_serialized.data})

@csrf_exempt
def practice_end(request):
	res = json.loads(request.body)
	model_name = res['model_name']
	data = res['data']
	for item in data:
		word = models_[model_name].objects.get(id=item['id'])
		word.total_count += 1
		if item['correct'] == False:
			word.mistakes += 1 
		word.save()
	return render(request, 'front/tests.html')
	# redirect(request, exercises) 