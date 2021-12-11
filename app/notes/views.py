from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializers import NoteLiteSerializer

from integration.clients import StatisticClient

from app.integration.clients import increment_access_counter


class NoteViewSet(ModelViewSet):

    serializer_class = NoteLiteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        return (
            Note.objects
            .exclude(is_deleted=True)
            .exclude(is_archived=True)
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # statistics_client = StatisticClient()
        # statistics_client.increment_access_counter(model_name='Note', object_id=instance.pk)
        is_metric_sent_succeeded = increment_access_counter('Note', instance.pk)
        if not is_metric_sent_succeeded:
            return HttpResponseBadRequest()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
