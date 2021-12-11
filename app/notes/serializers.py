from rest_framework import serializers

from notes.models import Note


class NoteLiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        exclude = ('author',)
