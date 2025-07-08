
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from uuid import uuid4

router= APIRouter()

app= FastAPI(title="Python Application Documentation API")

documents: Dict[str,dict] = {}

class Document(BaseModel):
    title: str
    content: str

@router.post("/documents/", response_model=dict)
def create_document(doc: Document):
    doc_id = str(uuid4())
    documents[doc_id] = doc.dict() 
    return {"id": doc_id, "document": documents[doc_id]}


@router.get("/documents/{doc_id}", response_model=Document)
def get_document(doc_id: str):
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")
    return  documents[doc_id]

@router.get("/documents/", response_model=dict)
def list_documents():
    return {"documents": documents}

@router.put("/documents/{doc_id}", response_model=dict)
def update_document(doc_id: str, doc: Document):
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")
    documents[doc_id] = doc.dict()
    return {"id": doc_id, "document": documents[doc_id]}

@router.delete("/documents/{doc_id}", response_model=dict)
def delete_document(doc_id: str):
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")
    deleted= documents.pop(doc_id)
    return {"id": doc_id, "deleted" : deleted}
  
