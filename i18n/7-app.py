#!/usr/bin/env python3
"""
A simple Flask application.
It uses Flask-Babel to support internationalization (i18n) and localization
 (l10n).
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    """Determine the best match with our supported languages."""
    if (
        request.args.get('locale') and
        request.args.get('locale') in app.config['LANGUAGES']
    ):
        return request.args.get('locale')
    elif (
        g.get('user') and
        g.user.get('locale') in app.config['LANGUAGES']
    ):
        return g.user.get('locale')
    elif request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    else:
        return app.config['BABEL_DEFAULT_LOCALE']


def get_user():
    """
    Get a user dictionary if a user ID is present in the request
    """
    if (
        request.args.get('login_as') and
        int(request.args.get('login_as')) in users
    ):
        return users.get(int(request.args.get('login_as')))
    return None


class Config:
    """Configuration for Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@babel.timezoneselector
def get_timezone():
    """Select the best timezone for the request."""

    # 1. Check ?timezone= URL param
    tz_param = request.args.get("timezone")
    if tz_param:
        try:
            pytz.timezone(tz_param)
            return tz_param
        except UnknownTimeZoneError:
            pass  # ignore invalid timezone

    # 2. Check user settings (if logged in)
    user = g.user
    if (
        user and
        user.get("timezone")
    ):
        try:
            pytz.timezone(user.timezone)
            return user.timezone
        except UnknownTimeZoneError:
            pass  # ignore invalid timezone

    # 3. Fallback to UTC
    return "UTC"


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('5-index.html')


@app.before_request
def before_request():
    """Get user before each request if any."""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


if __name__ == '__main__':
    app.run()
