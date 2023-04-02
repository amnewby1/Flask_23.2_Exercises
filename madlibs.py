from flask import Flask, request, render_template
from stories import story

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "Melama22!"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page_questions():
    prompts = story.prompts
    return render_template('home.html', questions=prompts)

@app.route('/story')
def my_story():
    story_text = story.generate(request.args)
    return render_template("story.html", story_text = story_text)
    