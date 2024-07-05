from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

from rest_framework.response import Response
@api_view(['GET','POST'])
def virat(request):
    return Response({'msg':'i love virat'})
