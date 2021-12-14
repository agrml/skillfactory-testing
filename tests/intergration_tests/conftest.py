from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
import pytest

from notes.models import Note


@pytest.fixture
def user():
    User = get_user_model()
    return User.objects.create(username='test_user')


@pytest.fixture
def client(user):
    client = APIClient()
    client.login(login='test_user')
    return client


@pytest.fixture
def note():
    return Note.objects.create(title='Title', text='Text')
