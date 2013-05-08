# Create your views here.
from responses.data.models import Response
from django.shortcuts import render_to_response
from datetime import datetime

def index(request):
	all_responses = Response.objects.filter(response_time__gte=1, response_time__lte=100, year=2012).order_by('inci_no')
	
	return render_to_response('index.html', {'responses': all_responses})
