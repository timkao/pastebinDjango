from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
  if request.method == 'GET':
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = SnippetSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
