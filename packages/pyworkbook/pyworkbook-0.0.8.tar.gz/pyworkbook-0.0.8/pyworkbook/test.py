from IPython.display import display, HTML
import re
import traceback


def tabelle_funktion(func_name: str, test_res: list) -> None:
    header = [
        "Funktionsaufruf",
        "Gewünschtes Ergebnis",
        "Ergebnis Ihrer Implementierung",
    ]
    code = (
        """
    <style>
        td, th {
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        padding: 15px !important;
        text-align: center !important;
        }
    </style>
    <h2>Test der Funktion: """
        + func_name
        + """</h2>
    <table><tr>"""
    )
    for h in header:
        code += "<th>" + h + "</th>"
    code += "</tr>"
    for row in test_res:
        code += "<tr style='background-color: "
        if (
            type(row[-1]) == str
            and len(row[-1]) >= 25
            and row[-1][:25] == "Fehler bei der Ausführung"
        ):
            code += "rgba(100,100,10, 0.8);"
        elif row[-1] == row[-2]:
            code += "rgba(20, 100, 20, 0.5)"
        else:
            code += "rgba(100, 20, 20, 0.5)"
        code += ";'>"

        # Funktionaufruf
        code += "<td>" + func_name + "("
        for param in row[0]:
            if type(param) == str:
                code += "'" + param + "', "
            else:
                code += str(param) + ", "
        code = code[:-2]
        code += ")</td>"

        # Gew. und tatsächliches Ergebnis
        for row in row[1:3]:
            if type(row) == str:
                code += "<td>'" + row + "'</td>"
            else:
                code += "<td>" + str(row) + "</td>"

        code += "</tr>"
    code += "</table>"

    display(HTML(code))


def formatiere_trace(trace: str):
    trace.replace("Traceback (most recent call last):", "Rückverfolgung des Fehlers:")
    # File-Bezeichungen löschen für das Notebook
    file_pattern = r"File(.*?)\,"
    file_texts = re.findall(file_pattern, trace)
    for text in file_texts:
        if "ipykernel" in text:
            trace = trace.replace(text, "")
    trace = trace.replace("File,", "")

    # Aufruf des Tests aus dem Trace löschen
    test_call_pattern1 = r"\sFile(.*?)teste_funktion"
    trace = re.sub(test_call_pattern1, "", trace)

    trace = trace.replace("res = func(*params)", "")

    # Leere Zeilen entfernen
    trace = "\n".join([line for line in trace.splitlines() if len(line.strip()) > 0])

    return trace.replace("\n", "<br>")


def teste_funktion(func, testfaelle: list) -> None:
    """führt geg. Tests durch und bettet eine Tabelle zur Übersicht der Test-Ergebnisse ins Notebook ein
    :param func: Funktion, die getestet werden soll (wichtig: Funktion selbst übergeben, nicht Funktionsname)
    :param list testfaelle: Liste, die die Testfälle enthält. Jeder Testfall ist wieder eine Liste und besteht aus einer Liste der Eingaben und der erwarteten Ausgabe (Beispiel-Testfall für Addierfunktion: [[1,1], 2] )
    """

    test_res = []
    for case in testfaelle:
        params = case[0]
        exp_res = case[1]
        try:
            res = func(*params)
        except Exception as e:
            res = (
                "Fehler bei der Ausführung: <br>"
                + str(e)
                + """
            <style>
            .btn {
                border: 1px solid rgba(10, 10, 50, 0.5);
                border-radius: 0.3em;
                margin-top: 1.5em;
                background: rgba(23, 42, 55, 0.5);
                color: white;
                padding: 0.5em;
            }
            .btn:hover {
                background: rgba(33, 65, 80, 0.5);
                cursor: pointer;
            }
            </style>
            <div>
            <button class="btn" onclick="this.parentElement.getElementsByClassName('fehler-komplett')[0].style.display = 'block'; this.style.display = 'none';">Vollständige Fehlermeldung anzeigen</button>
            <p class='fehler-komplett' style='display: none;'>"""
                + formatiere_trace(traceback.format_exc())
                + "</div>"
            )
            # print(traceback.format_exc())
        test_res.append([params, exp_res, res])

    tabelle_funktion(func.__name__, test_res)


def tabelle_variable(gew_wert, wert):
    code = """
    <style>
        table {
            margin: 1em;
        }
        td, th {
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        padding: 15px !important;
        text-align: center !important;
        max-width: 500px;
        min-width: 200px;
        }
    </style>"""
    code += "<table><tr>"
    code += "<th>Gewünschter Datentyp</th><th>Tatsächlicher Datentyp</th>"
    code += "</tr>"
    code += "<tr style='background-color: "

    # Special char '<' escapen
    gew_dt = str(type(gew_wert)).replace("<", "&#60;")
    tats_dt = str(type(wert)).replace("<", "&#60;")

    if gew_dt == tats_dt:
        code += "rgba(20, 100, 20, 0.5)"
    else:
        code += "rgba(100, 20, 20, 0.5)"
    code += ";'>"
    code += "<td>{}</td><td>{}</td>".format(gew_dt, tats_dt)
    code += "</tr></table>"

    code += "<table><tr><th>Gewünschter Wert</th><th>Tatsächlicher Wert</th>"
    code += "</tr>"
    code += "<tr style='background-color: "
    if gew_wert == wert:
        code += "rgba(20, 100, 20, 0.5)"
    else:
        code += "rgba(100, 20, 20, 0.5)"
    code += ";'>"
    for wert in [gew_wert, wert]:
        if type(wert) == str:
            code += "<td>'{}'</td>".format(wert)
        else:
            code += "<td>{}</td>".format(wert)

    code += "</tr></table><br>"

    return code


def teste_variable(globals: dict, name: str, wert):
    """Testet Existenz und Wert einer Variable
    :param dict globals: globals()-Objekt aus dem Notebook
    :param str name: Name der Variable
    :param wert: Gewünschter Wert der Variable"""

    if name in globals:
        html_code = "<div border: 2px solid green; background: red;><p style='color: rgb(30, 150, 30); margin-left: 1em; margin-bottom: 0em; font-size: 1.5em; font-weight: 600;'>Variable '{}' wurde angelegt:</p>".format(
            name
        )
        html_code += tabelle_variable(wert, globals[name])
        html_code += "</div>"
        display(HTML(html_code))
    else:
        display(
            HTML(
                "<p style='color: rgb(180, 35, 35); margin-left: 1em; margin-bottom: 0em; font-size: 1.5em; font-weight: 600;'>Variable '{}' wurde noch nicht angelegt</p>".format(
                    name
                )
            )
        )
