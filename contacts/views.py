from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method == 'POST':
        print('Hello')
        return