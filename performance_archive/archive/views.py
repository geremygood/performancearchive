from django.template import Context, loader
from archive.models import Performance
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

def index(request):
    latest_performance_list = Performance.objects.all().order_by('-add_date')[:5]
    return render_to_response('performance/index.html', {'latest_performance_list': latest_performance_list})

def detail(request, archive_performance_id):
    p = get_object_or_404(Performance, pk=archive_performance_id)
    return render_to_response('performance/detail.html', {'performance': p})

def results(request, archive_performance_id):
    return HttpResponse("You're looking at the results of poll %s." % archive_performance_id)
