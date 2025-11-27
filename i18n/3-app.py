#!/usr/bin/env python3
"""
A simple Flask application.
It uses Flask-Babel to support internationalization (i18n) and localization (l10n).

_ is imported from flask_babel and is used to mark strings for translation.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
