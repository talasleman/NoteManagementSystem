import datetime
import time

class Note:

    notes = []

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.creation_date = datetime.datetime.now()
        self.notes.append(self)
        print(f"Note {len(self.notes)} created")
    
    def __repr__(self):
        return (f"Note(title: '{self.title}', author: {self.author}, content: {self.content}, creation_date: {self.creation_date})")
    
    def remove(self):
        self.notes.remove(self)

    @staticmethod
    def get_notes():
        print(Note.notes)


note1 = Note('the first note', 'Hello World!', 'Steve Wozniak')
note2 = Note('the second note', 'Hello Friend!', 'Fred Ali')
note1.remove()

Note.get_notes()
