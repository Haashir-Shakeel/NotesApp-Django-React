from rest_framework.response import Response
from . serializers import NoteSerializer
from django.http import JsonResponse
from .models import Note



def getNoteList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)
    
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def getNoteDetail(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes,many=False)
    return Response(serializer.data)

def updateNote(request, pk):
    data = request.data # can use data because we using rest_framework otherwise we do request.body or request.POST
    note = Note.objects.get(id=pk)
    serialzer = NoteSerializer(note, data = data)

    if serialzer.is_valid():
        serialzer.save()
        return Response(serialzer.data)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')