import csv
from note import Note

def read_csv():
    with open("../notes_data.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter='|')
        for row in csvreader:
            new_note = Note(row[0], row[1], row[2])
    print(Note.get_notes())
