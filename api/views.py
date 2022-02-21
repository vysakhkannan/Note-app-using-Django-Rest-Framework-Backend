from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NotesSerializers
from rest_framework import status




# Create your views here.
@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NotesSerializers(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note(request,pk):
    note = Note.objects.get(id = pk)
    serializer = NotesSerializers(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_note(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    print(data)
    serializer = NotesSerializers(note, many=False)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['PUT'])
def update_note(request,pk):
    data = request.data
    note = Note.objects.get(id = pk)
    serializer = NotesSerializers(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_note(request,pk):
    note = Note.objects.get(id = pk)
    note.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

