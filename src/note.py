import datetime

class Note:

    notes = {}
    id_counter = 1

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.creation_date = datetime.datetime.now()
        self.id = Note.id_counter
        Note.id_counter += 1
        self.notes[self.id] = self
        print(f"Note {len(self.notes)} created")
    
    def __repr__(self):
        return (f"Note(title: '{self.title}', author: {self.author}, content: {self.content}, creation_date: {self.creation_date})")
    
    def remove(self):
        self.notes.remove(self)

    @staticmethod
    def get_notes():
        return Note.notes
    
    @staticmethod
    def get_note(id):
        return Note.notes[id]