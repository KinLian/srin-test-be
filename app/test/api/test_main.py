import uuid
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

from app.main import app
from app.models.phone import Phone

client = TestClient(app)

def test_get_all_phones():
    mock_supabase_client = Mock()

    with patch('app.api.main.supabase_phone', return_value=mock_supabase_client):
        response = client.get('/phone')

        # Verify that the mocked methods were called
        mock_supabase_client.select.assert_called_with('*')
        mock_supabase_client.select.return_value.execute.assert_called_once()


def test_get_single_phone():
    mock_supabase_client = Mock()
    mock_supabase_client.select.return_value.eq.return_value.execute.return_value = Mock(
        data={"data": {"ID": "0"}},
        error=None
    )

    with patch('app.api.main.supabase_phone', return_value=mock_supabase_client):
        response = client.get('/phone/0')

        # Verify that the mocked methods were called
        mock_supabase_client.select.assert_called_with()
        mock_supabase_client.select.return_value.eq.assert_called_with(
            "id", "0")
        mock_supabase_client.select.return_value.eq.return_value.execute.assert_called_once()


def test_add_phone():
    mock_supabase_client = Mock()
    dummy_phone = Phone(id=str(uuid.uuid4()), model="MODEL", price="",
                        processor="", ram="", battery="", display="", camera="", card="", os="")

    with patch('app.api.main.supabase_phone', return_value=mock_supabase_client):
        response = client.post('/phone', json=dummy_phone.model_dump_json())

        # Verify that the mocked methods were called
        mock_supabase_client.insert.assert_called_with(dummy_phone)
        mock_supabase_client.insert.return_value.execute.assert_called_once()


def test_update_phone():
    mock_supabase_client = Mock()
    dummy_phone = Phone(id=str(uuid.uuid4()), model="MODEL", price="",
                        processor="", ram="", battery="", display="", camera="", card="", os="")

    with patch('app.api.main.supabase_phone', return_value=mock_supabase_client):
        response = client.put('/phone/0', json=dummy_phone.model_dump_json())

        # Verify that the mocked methods were called
        mock_supabase_client.update.assert_called_with(dummy_phone)
        mock_supabase_client.update.return_value.eq.assert_called_with(
            "id", "0")
        mock_supabase_client.select.return_value.eq.return_value.execute.assert_called_once()


def test_delete_phone():
    mock_supabase_client = Mock()

    with patch('app.api.main.supabase_phone', return_value=mock_supabase_client):
        response = client.delete('/phone/0')

        # Verify that the mocked methods were called
        mock_supabase_client.delete.assert_called_with()
        mock_supabase_client.delete.return_value.eq.assert_called_with(
            "id", "0")
        mock_supabase_client.delete.return_value.eq.return_value.execute.assert_called_once()
