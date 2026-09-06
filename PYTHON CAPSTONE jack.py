import sqlite3

def analyze_text(text):
    words = text.split()
    characters = len(text)
    word_count = len(words)
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    return characters, word_count, sentence_count

def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?")
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

db = sqlite3.connect("text_analysis.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    characters INTEGER,
    words INTEGER,
    sentences INTEGER
)
""")

db.commit()

text = input("Enter the text to analyse: ")

characters, words, sentences = analyze_text(text)
frequency = word_frequency(text)

cursor.execute("""
INSERT INTO analysis
(text, characters, words, sentences)
VALUES (?, ?, ?, ?)
""", (text, characters, words, sentences))

db.commit()

print("\n--- TEXT ANALYSIS ---")
print("Characters :", characters)
print("Words      :", words)
print("Sentences  :", sentences)

print("\n--- WORD FREQUENCY ---")

for word, count in frequency.items():
    print(word, ":", count)

print("\nData stored successfully!")
