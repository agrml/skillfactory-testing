from rest_framework import routers

from notes.views import NoteViewSet

router = routers.SimpleRouter()
router.register(r'notes', NoteViewSet)
