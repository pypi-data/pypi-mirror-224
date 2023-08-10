import ipywidgets as widgets
from IPython.display import display, HTML


def tipp(tipp_text: str, vorschau_text: str = "Tipp anzeigen:"):
    """Einbettung eines optionalen Tipps ins Notebook
    :param str tipp_text: Tipp, der beim Klick angezeigt werden soll
    :param str vorschau_text: Text, der direkt im Notebook angezeigt wird und angeklickt werden kann, um den Tipp anzuzeigen (default: Tipp anzeigen)
    """

    code = """
    <style>
    .tipp-anzeigen {{
        opacity: 0.8;
        color: rgb(200,200,100);
        font-size: 1.2em;
    }}
    .tipp-anzeigen:hover {{
        opacity: 1;
        cursor: pointer;
    }}
    .tipp {{ display: none; font-size: 1.2em; }}
    </style>
    <div>
        <p class="tipp-anzeigen" onclick="this.innerHTML = '💡 Tipp: ' + this.parentElement.getElementsByClassName('tipp')[0].innerHTML">💡 {}</p>
        <p class="tipp">{}</p>
    </div>
    """.format(
        vorschau_text, tipp_text
    )
    display(HTML(code))


def aufgabe(text: str, nr: int = 0):
    """formatierte Darstellung von Aufgaben
    Aufgaben werden im Notebook automatisch durchnummeriert"""

    code = """
    <style>
    .aufgabe {{
        color: rgb(18, 29, 36);
        background-color: white;
        width: 1.5em;
        padding: 1px;
        padding-left: 5px;
        border-radius: 3px;
        display: inline-block;
    }}
    </style>
    <div style='font-size: 1.2em;'>
        <span class="aufgabe">{}:</span>
        <span">{}</span>
    </div>
    """.format(
        nr if nr != 0 else "A", text
    )
    display(HTML(code))
