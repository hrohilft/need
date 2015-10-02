from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse, Http404

from .models import Need

def index(request):
    latest_need_list = Need.objects.order_by('-pub_date')[:5]
    return render(request, 'need/index.html', {'latest_need_list': latest_need_list})

    
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, pk):
	need = get_object_or_404(Need, pk=pk)
	return render(request, 'need/detail.html', {'need': need})
