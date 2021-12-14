from unittest.mock import patch

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
@patch('notes.views.increment_access_counter')
def test_get_note__negative(mocked_increment_access_counter, client, note):
    mocked_increment_access_counter.return_value = False
    client = APIClient()

    response = client.get(f'/api/notes/{note.pk}/')

    assert response.status_code == 400
    # assert mocked_increment_access_counter.called
    mocked_increment_access_counter.assert_called_once_with('Note', note.pk)

