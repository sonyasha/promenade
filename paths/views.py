# from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import render_to_string
from datetime import datetime

def index(request):
    return HttpResponse('Hi everybody!!')

def curr_time(request):
    current_time = datetime.now()
    
    # html_time = template.Template('<html><body><div>It is {{current_time}}</div></body></html>')
    context = template.Context({'current_time': current_time})
    html_time = render_to_string('paths/test_template.html', context)
    html = html_time.render(context)
    return HttpResponse(html)