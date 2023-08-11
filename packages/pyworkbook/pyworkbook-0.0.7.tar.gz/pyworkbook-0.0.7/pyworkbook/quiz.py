import functools
import ipywidgets as widgets
from IPython.display import display, HTML
import random
import string


def css_laden():
    """CSS, das zum korrekten Anzeigen von Widgets benötigt wird"""

    display(
        HTML(
            """
<style>
    .cell-output-ipywidget-background {
        background-color: rgb(29,29,29) !important;
    }
    .jp-OutputArea-output {
        background-color: rgb(29,29,29);
    }
    
    .jupyter-widgets-view {
        background-color: rgb(29,29,29) !important;
    }

    .widget-label, .jupyter-matplotlib-header{
        color: #fff !important;
    }

    .jupyter-widgets {
        color: white !important;
        --jp-widgets-label-color = white;
    }

    .widget-checkbox {
        color: white !important;
    }
    
    .widget-label-basic {
        color: white !important;
    }

    .widget-input {
        background-color: rgba(255,255,255, 0.08) !important;
        border: 1px solid orange !important;
        color: white !important;
        font-size: 13px !important;
        min-width: 10em !important;
        padding: 1em !important;
        margin-bottom: 0 !important;
    }

    .widget-input:hover {
        background-color: rgba(255,255,255, 0.15) !important;
    }

    .jupyter-button {
        color: #fff;
        padding: 2px 5px !important;
        border-bottom-left-radius: 0.6em !important;
        border-bottom-right-radius: 0.6em !important;
        width: max-content !important;
        font-size: 13px !important;
        min-width: 23em !important;
        height: max-content !important;
        cursor: pointer !important;
        border: 1px solid #246685 !important;
        background: #102b38 !important;
        white-space: normal !important;
        margin-top: 0 !important;
    }

    .jupyter-button:hover {
        background: #134258 !important;
    }
</style>
    """
        )
    )


def multiple_choice(
    korr_antw: list[str], falsche_antw: list[str], frage: str = ""
) -> None:
    """bettet ein Multiple-Choice-Quiz im Notebook ein
    :param list[str] korr_antw: Liste aller korrekten Antworten
    :param list[str] falsche_antw: Liste aller falschen Antworten
    :param str frage: Frage, die über dem Quiz angezeigt werden soll (default: nicht darstellen)
    """

    css_laden()
    output = widgets.Output()
    if frage != "":
        display(HTML("<p style='font-size: 1.2em;'>{}</p>".format(frage)))

    checkboxen = []
    for antw in falsche_antw:
        checkboxen.append(
            {
                "wahr": False,
                "widget": widgets.Checkbox(
                    value=False, description=antw, disabled=False, indent=False
                ),
            }
        )

    for antw in korr_antw:
        checkboxen.append(
            {
                "wahr": True,
                "widget": widgets.Checkbox(
                    value=False, description=antw, disabled=False, indent=False
                ),
            }
        )

    random.shuffle(checkboxen)
    for checkbox in checkboxen:
        display(checkbox["widget"], output)

    btn = widgets.Button(
        value=False,
        description="Antworten prüfen",
        disabled=False,
        button_style="",
        tooltip="Description",
        icon="check",
    )

    display(btn, output)

    eval = widgets.HTML(value="", disabled=True)
    display(eval, output)

    def on_button_clicked(b):
        anz_antworten = 0
        korrekt = 0
        for checkbox in checkboxen:
            anz_antworten += 1
            if checkbox["wahr"] == checkbox["widget"].value:
                korrekt += 1
        if korrekt == anz_antworten:
            eval.value = "<p style='color: green'>{}/{} Antworten korrekt</p>".format(
                korrekt, anz_antworten
            )
        else:
            eval.value = "<p style='color: red'>{}/{} Antworten korrekt</p>".format(
                korrekt, anz_antworten
            )

    btn.on_click(on_button_clicked)


def quizfrage(korr_antw: list[str], frage: str = "", gross_klein_egal: bool = False):
    """bettet eine Quizfrage mit freier Texteingabe ins Notebook ein
    :param list[str] korr_antw: Liste aller Antworten, die als korrekt gewertet werden
    :param str frage: Frage, die über der Eingabe angezeigt werden soll (default: keine Frage anzeigen)
    :param bool gross_klein_egal: Falls auf True gesetzt, wird Groß-/Kleinschreibung bei der Auswertung der Eingabe nicht beachtet
    """

    def zufaelligen_string_erzeugen(laenge: int) -> str:
        letters = string.ascii_letters + string.digits
        random_string = "".join(random.choice(letters) for _ in range(laenge))
        return random_string

    css_laden()
    output = widgets.Output()
    eingabe = widgets.Text(value="", disabled=False)
    # zufälliger Class Name, um Farbe nachträglich ändern zu können
    eingabe_class: str = zufaelligen_string_erzeugen(12)
    eingabe.add_class(eingabe_class)
    btn = widgets.Button(
        value=False,
        description="Antwort prüfen",
        disabled=False,
        button_style="",
        tooltip="Description",
        icon="check",
    )

    rueckmeldung = widgets.HTML(value="")
    if frage != "":
        display(HTML("<p style='font-size: 1.2em;''>{}</p>".format(frage)))
    display(eingabe, output)
    display(btn, output)
    display(rueckmeldung, output)

    def on_button_clicked(korr_antw, b):
        nutzer_eingabe: str = eingabe.value
        if gross_klein_egal:
            nutzer_eingabe: str = nutzer_eingabe.lower()
            korr_antw = [antw.lower() for antw in korr_antw]

        if eingabe.disabled:
            return

        if nutzer_eingabe in korr_antw and rueckmeldung.value != "Eingabe korrekt":
            # Korrekte Eingabe
            rueckmeldung.value = "Eingabe korrekt"
            eingabe.disabled = True
            display(
                HTML(
                    """
                <style>
                    .{} {{
                        background-color: green !important;
                    }}
                </style>
            """.format(
                        eingabe_class
                    )
                )
            )
        elif rueckmeldung.value != "Eingabe nicht korrekt":
            rueckmeldung.value = "Eingabe nicht korrekt"
            display(
                HTML(
                    """
                <style>
                    .{} {{
                        background-color: red;
                    }}
                </style>
            """.format(
                        eingabe_class
                    )
                )
            )

    # https://stackoverflow.com/questions/50951403/in-python-how-to-call-a-function-with-an-argument-on-a-click-event
    btn.on_click(functools.partial(on_button_clicked, korr_antw))
