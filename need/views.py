from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.utils.translation import get_language, get_language_info
from django.contrib.auth.decorators import login_required

from .models import Need, Transl
from .forms import NeedForm, TranslForm

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
		print(request)
		form = NeedForm(request.POST)
		if form.is_valid():
			print("valid")
			need = form.save(commit=False)
			need.pub_date = timezone.now()
			need.save()
			return HttpResponseRedirect(reverse('need:index'))
		else:
			print("not valid")
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

@login_required	
def delete(request, pk):
	need = get_object_or_404(Need, pk=pk)
	need.delete()
	return HttpResponseRedirect(reverse('need:index'))
	
def langchoice(request):
	ar = get_language_info('ar')
	#fa = get_language_info('fa')
	de = get_language_info('de')
	en = get_language_info('en')
	languages = [ar, de, en] #fa,
	return render(request, 'need/langchoice.html', {'languages': languages})
	
def about(request):
	return render(request, 'need/about.html', {})
	
def add_transl(request, pk):
    need = get_object_or_404(Need, pk=pk)
    if request.method == "POST":
        form = TranslForm(request.POST)
        if form.is_valid():
            transl = form.save(commit=False)
            transl.need = need
            transl.publish()
            transl.save()
            return redirect('need:detail', pk=need.pk)
    else:
        form = TranslForm()
    return render(request, 'need/add_transl.html', {'form': form, 'need': need})

@login_required	
def remove_transl(request, pk):
	transl = get_object_or_404(Transl, pk=pk)
	transl.hide()
	return redirect('need:detail', pk=transl.need.pk)




