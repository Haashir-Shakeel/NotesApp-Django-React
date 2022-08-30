from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from . models import Note
from . serializers import NoteSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE

@api_view(['GET'])
def getRoutes(request):
    return Response('Our API')


@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('-updated')
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        note = Note.objects.create(
            body=data['body']
        )
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def getNote(request, pk):
    if request.method == 'GET':
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes,many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = request.data # can use data because we using rest_framework otherwise we do request.body or request.POST
        note = Note.objects.get(id=pk)
        serialzer = NoteSerializer(note, data = data)

        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('Note was deleted')

        




# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)

# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data # can use data because we using rest_framework otherwise we do request.body or request.POST
#     note = Note.objects.get(id=pk)
#     serialzer = NoteSerializer(note, data = data)

#     if serialzer.is_valid():
#         serialzer.save()
#         return Response(serialzer.data)
#     return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted')
