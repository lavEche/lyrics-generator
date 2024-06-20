from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_lyrics', methods=['POST'])
def generate_lyrics():
    starter_text = request.json['starter_text']

    # Replace this with your actual lyrics generation logic
    generated_lyrics = generate_lyrics_function(starter_text)

    # Simulate musician data
    musicians = ["Taylor Swift", "David Bowie", "Billy Joel", "Eric Clapton", "Billie Eilish"]
    musician = random.choice(musicians)

    # Simulate GIF or image URL
    gif_url = "https://example.com/your-gif-url.gif"

    return jsonify({'generated_lyrics': generated_lyrics, 'musician': musician, 'gif_url': gif_url})

def generate_lyrics_function(starter_text):
    # Replace this with your actual lyrics generation logic
    # Example: Concatenate the starter_text with some generated text
    return f"{starter_text} - Generated lyrics..."

if __name__ == '__main__':
    app.run(debug=True)
