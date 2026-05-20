import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.config import Base
from database.config import SessionLocal
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app.dependency_overrides[SessionLocal] = override_get_db

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "This is a test task."})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task."
    assert "id" in data
    
def test_create_task_invalid():
    response = client.post("/tasks/", json={"title": "Te"})
    assert response.status_code == 422
    
def test_list_task():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_get_task():
    create = client.post("/tasks/", json={"title": "Test task"})
    task_id = create.json()["id"]
    
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id
    
def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404

def test_update_task():
    create = client.post("/tasks/", json={"title": "Test task"})
    task_id = create.json()["id"]
    
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    
    
def test_delete_task():
    create = client.post("/tasks/", json={"title":"task delete"})
    task_id = create.json()["id"]
    
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404