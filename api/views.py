from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Note
from . serializers import NoteSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response('Our API')


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data # can use data because we using rest_framework otherwise we do request.body or request.POST
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance = note, data = data)
                            #serializing this particular note, and passing in new data into note
 
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')
