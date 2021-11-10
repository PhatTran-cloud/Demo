from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def req(request):
    return HttpResponse("Hello may cung")


def req1(request):
    return render(request, 'ec2connect/html.html')