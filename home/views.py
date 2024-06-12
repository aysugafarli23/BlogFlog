import requests
from django.shortcuts import render
from django.http import HttpResponse

def blog__list(request):
    # try:
    #     response = requests.get('http://127.0.0.1:8000/homeapi/list/')
    #     response.raise_for_status()  # Raise an exception for HTTP errors
    #     blogs = response.json()
    # except requests.exceptions.RequestException as e:
    #     return HttpResponse(f"An error occurred: {e}", status=500)
    
    # return render(request, 'base.html', {'blogs': blogs})
    return render(request, 'base.html')