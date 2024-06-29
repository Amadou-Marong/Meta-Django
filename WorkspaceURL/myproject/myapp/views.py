from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from combination of wheat, water or eggs',
        'falafel': 'Falafel are deep fried patties or balls made from ',
        'cheesecake': 'Cheesecake is a type of dessert made with cream, soft cheese on top of cookie, pastry crust or graham cracker and fruit sauce topping.',
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)