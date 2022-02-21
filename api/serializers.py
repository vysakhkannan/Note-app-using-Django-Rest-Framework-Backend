from django.forms import models
from rest_framework import serializers
from .models import Note as Notes

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'