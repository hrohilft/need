from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _

from .models import Need
from .forms import NeedForm

def index(request):
    latest_need_list = Need.objects.order_by('-pub_date')[:50]
    return render(request, 'need/index.html', {'latest_need_list': latest_need_list})

#def index(request):
#	# Translators: This message appears on the index page
#	output = _("Hello")
#	return HttpResponse(output)

def detail(request, pk):
	need = get_object_or_404(Need, pk=pk)
	return render(request, 'need/detail.html', {'need': need})
	
def new(request):
	if request.method == "POST":
		form = NeedForm(request.POST)
		if form.is_valid():
			need = form.save(commit=False)
			need.pub_date = timezone.now()
			need.save()
			return HttpResponseRedirect(reverse('need:index'))
		else:
			form = NeedForm()
			# Translators: This error message appears on the new need form page
			return render(request, 'need/new.html', {'error_message': _("wrong input"), 'form': form})
	form = NeedForm()
	return render(request, 'need/new.html', {'form': form})
	
def done(request, pk):
	need = get_object_or_404(Need, pk=pk)
	need.done = True
	need.save()
	return HttpResponseRedirect(reverse('need:index'))
