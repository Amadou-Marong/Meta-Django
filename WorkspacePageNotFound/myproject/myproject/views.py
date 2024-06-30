from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse('404: Page Not Found! <br><br> <button onclick="" href='',"">Go to Homepage</button>')

def home(request):
    return HttpResponseNotFound('Hello and Welcome to Little Lemon')

