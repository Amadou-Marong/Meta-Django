from django.shortcuts import render

# Create your views here.
from myapp.forms import DemoForm

def form_view(request):
    form = DemoForm()
    context = {"form": form}
    return render(request, "home.html", context)