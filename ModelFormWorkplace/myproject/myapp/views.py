from django.shortcuts import render

# Create your views here.

from .forms import LogForm

def form_view(request):
    form = LogForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)
