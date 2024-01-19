from django.http import HttpResponse
from django.shortcuts import render


#  - Home Page 
def home_page(request):

    return render(request, 'index.html')

