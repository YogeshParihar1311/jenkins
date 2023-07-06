from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(r):
    return HttpResponse("<h1>Jenkins First Project (CI/CD) Deployment with AWS Completed Successfully..</h1>")