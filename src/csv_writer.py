import csv

header = ['title', 'content', 'author']

rows = [
    {'title': 'Journey Begins', 'content': 'Today marks the start of our grand adventure. We set out at dawn.', 'author': 'Alex Journey'},
    {'title': 'Mystery of the Lost Key', 'content': 'The old mansion on the hill hides a secret. A key lost in time.', 'author': 'Casey Holmes'},
    {'title': 'Gardening Tips', 'content': 'Gardening is not just a hobby; it\'s a way of life. Here are some tips to get you started.', 'author': 'Morgan Green'},
    {'title': 'The Art of Baking', 'content': 'Baking is both an art and a science. This guide introduces the basics of making perfect bread.', 'author': 'Pat Baker'},
    {'title': 'Night Sky Wonders', 'content': 'Exploring the constellations and stories written in the night sky.', 'author': 'Stella Cosmos'},
    {'title': 'Programming 101', 'content': 'An introductory guide to the world of programming. Where logic meets creativity.', 'author': 'Devon Coder'},
    {'title': 'The World of Coffee', 'content': 'From bean to cup. Discover the journey of coffee.', 'author': 'Sam Brewster'},
    {'title': 'History\'s Mysteries', 'content': 'Unraveling the mysteries that history books don\'t tell you.', 'author': 'Taylor Epoch'},
    {'title': 'Photography Basics', 'content': 'Capture the world through your lens. A beginner\'s guide to photography.', 'author': 'Jordan Shutter'},
    {'title': 'Mindfulness and Meditation', 'content': 'Find peace in a chaotic world. Starting your journey towards mindfulness.', 'author': 'Dana Calm'},
    {'title': 'Cycling Across Continents', 'content': 'The tale of a two-wheeled journey across the vast landscapes of our planet.', 'author': 'Chris Pedal'},
    {'title': 'The Joy of Painting', 'content': 'Exploring the expression of emotions through the stroke of a brush.', 'author': 'Robin Artiste'}
]

def populate_csv():
    with open("../notes_data.csv", 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=header, delimiter='|')
        csv_writer.writeheader()
        csv_writer.writerows(rows)
