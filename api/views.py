from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.


def home(request, *args, **kwargs):
    response = dict(request.GET)
    response['content_type'] = request.content_type
    try:
        response['data'] = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        response['data'] = None
    return JsonResponse(response)
