from fastapi import FastAPI
from pydantic import BaseModel
from note import Note

class NoteSchema(BaseModel):
    title: str
    content: str
    author: str

app = FastAPI()

@app.get("/notes")
async def root():
    return Note.get_notes()

@app.post("/notes")
async def create_note(note: NoteSchema):
    new_note = Note(note.title, note.content, note.author)
    print(Note.notes)
    return new_note

@app.put("/notes/{id}")
async def modify_note(id, note: NoteSchema):
    id = int(id)
    note  = note.model_dump()
    for val in note:
        setattr(Note.notes[id], val, note[val])
    return Note.get_note(id)