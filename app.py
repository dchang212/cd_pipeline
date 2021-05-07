from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://en.wikipedia.org/wiki/File:Frances_Gertrude_McGill_working_in_laboratory.png",
    "https://en.wikipedia.org/wiki/File:Mark_Selby_at_Snooker_German_Masters_(DerHexer)_2015-02-08_16_(cropped).jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")