import pytest
import sys
sys.path.insert(0, '.')
from app import app

def test_home():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200

def test_health():
    client = app.test_client()
    r = client.get('/health')
    assert r.status_code == 200

def test_version():
    client = app.test_client()
    r = client.get('/version')
    assert r.status_code == 200

def test_metrics():
    client = app.test_client()
    r = client.get('/metrics')
    assert r.status_code == 200
