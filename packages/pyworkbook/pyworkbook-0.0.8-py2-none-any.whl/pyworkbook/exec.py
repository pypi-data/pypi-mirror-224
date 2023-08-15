import sqlite3

# relativer import
from .iframe import *
from .quiz import *
from .test import *
from .vorlagen import *


def laden_und_ausfuehren(tabelle: str, nr: int, globals_jup: dict = {}):
    """Code aus der angegebenen Tabelle der db-Datei mit dieser Nr ausführen"""
    db = sqlite3.connect("kursdaten.db")
    c = db.cursor()
    c.execute("SELECT code FROM {} WHERE nr = ?".format(tabelle), [nr])
    code: str = c.fetchall()[0][0]
    if isinstance(code, str):
        # Globalen Kontext aus dem Notebook nutzen, falls notwendig
        exec(code) if globals_jup == {} else exec(code, globals_jup)


def aufgaben(nr: int) -> None:
    laden_und_ausfuehren("AufgabenCells", nr)


def tests(nr: int, globals_jup: dict) -> None:
    laden_und_ausfuehren("TestCells", nr, globals_jup)


def visualisierung(nr: int, globals_jup: dict) -> None:
    laden_und_ausfuehren("VisCells", nr, globals_jup)
