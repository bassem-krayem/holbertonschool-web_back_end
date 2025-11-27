#!/usr/bin/env python3
"""A simple Flask application."""
from flask import Flask, render_template
from babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
