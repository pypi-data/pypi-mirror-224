from flask import Flask
from contextlib import contextmanager
import sys, os
import logging


@contextmanager
def stdout_umleiten():
    with open(os.devnull, "w") as devnull:
        stdout_regulaer = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = stdout_regulaer


def start_server(port: int, html: str) -> None:
    app = Flask(__name__)

    @app.route("/")
    def startseite():
        return html

    log = logging.getLogger("werkzeug")
    log.disabled = True
    with stdout_umleiten():
        # Keine Flask-Meldungen ausgeben
        app.run(port=port)
