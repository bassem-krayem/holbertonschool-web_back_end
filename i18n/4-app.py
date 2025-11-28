#!/usr/bin/env python3
"""
A simple Flask application.
It uses Flask-Babel to support internationalization (i18n) and localization
 (l10n).
"""
from flask import Flask, render_template, request
from flask_babel import Babel


def get_locale():
    """Determine the best match with our supported languages."""
    if (
        request.args.get('locale') and
        request.args.get('locale') in app.config['LANGUAGES']
    ):
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config:
    """Configuration for Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)

babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
