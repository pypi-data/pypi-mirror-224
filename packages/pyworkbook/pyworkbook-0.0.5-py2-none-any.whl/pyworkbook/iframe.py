from .flask_call import start_server
import ipywidgets as widgets
import socket
import webbrowser
import time
from multiprocessing import Process
from IPython.display import display, HTML


def port_wird_genutzt(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def button_erzeugen(text: str) -> widgets.Button:
    """erzeugt einen Button und zeigt diesen an
    :param str text: Text, den der Button anzeigen soll
    """
    output = widgets.Output()
    btn = widgets.Button(
        value=False,
        description=text,
        disabled=False,
        button_style="",
        tooltip="Description",
        icon="check",
        layout=widgets.Layout(width="max-content", height="max-content"),
    )

    display(btn, output)
    return btn


def iframe(
    link: str, breite: int, hoehe: int, start_y: int = 0, scrollen_aktiv: bool = True
) -> None:
    """bettet einen iframe zum geg. Link in das Notebook ein
    :param str link: Link zur gewünschten Webseite
    :param int breite: Breite des IFrames
    :param int hoehe: Höhe des IFrames
    :param int start_y: Starthöhe innerhalb der eingebetteten Webseite (default 0 -> Ganz oben)
    :param bool scrollen_aktiv: Soll Scrollen im Iframe aktiviert sein? (default: aktiv)
    """
    code = """
    <style>
    iframe {{
        border:none;
        border-radius: 5px;
        position: relative;
    }}

    .ifr-container {{
        max-width: {}px;
        max-height: {}px;
        margin: auto;
        margin-top: 2%;
        overflow: hidden;
        border-radius: 5px;
    }}
</style>
<div class="ifr-container">
    <iframe src="{}" width={} height={} scrolling="{}" style="top:-{}px;"></iframe>
</div>
    """.format(
        breite,
        hoehe,
        link,
        breite,
        hoehe + start_y,
        "yes" if scrollen_aktiv else "no",
        start_y,
    )
    display(HTML(code))


def webseite_oeffnen(html_pfad: str, text: str) -> None:
    """erzeugt einen Button in der Ausgabe mit dem geg. Text
    Button-Klick öffnet die HTML-Datei aus html_pfad über einen temporären lokalen Flask-Server im Browser
    Anwendungsszenario: Ansicht einzelner Web-Anwendungen
    IFrames direkt in VS Code ermöglichen Copy-Paste nicht
    """

    btn = button_erzeugen(text)

    def on_button_clicked(b):
        with open(html_pfad, "r") as f:
            html = f.read()
        webseite_verteilen(html)

    btn.on_click(on_button_clicked)


def iframe_browser(
    link: str,
    text: str,
    breite: int,
    hoehe: int,
    start_y: int = 0,
    scrollen_aktiv: bool = True,
):
    """öffnet ein HTML-File mit dem eingebetteten Iframe über einen temporären lokalen Flask-Server im Browser
    Anwendungsszenario: Ansicht einzelner Web-Anwendungen
    IFrames direkt in VS Code ermöglichen Copy-Paste nicht

    :param str link: Link zur Webseite, die eingebettet werden soll
    :param str text: Text des Buttons zum Öffnen der Seite
    :param int breite: Breite des Iframes
    :param int hoehe: Höhe des IFrames
    :param int start_y: Starthöhe innerhalb der eingebetteten Webseite (default 0 -> Ganz oben)
    :param bool scrollen_aktiv: Soll Scrolling im Iframe aktiviert sein? (default: aktiv)
    """

    btn = button_erzeugen(text)

    scrolling = "yes" if scrollen_aktiv else "no"

    html = """
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
        body {{
            background: rgb(15, 20, 25);
        }}

        .ifr-container {{
            max-height: {};
            max-width: {};
            margin: auto;
            margin-top: 2%;
            overflow: hidden;
            border-radius: 5px;
        }}

        iframe {{
            border:none;
            border-radius: 5px;
            position: relative;
        }}
    </style>
</head>
<body>
    <div class="ifr-container">
        <iframe src="{}" width={} height={} scrolling="{}" style="top:-{}px;"></iframe>
    </div>
</body>
</html>
    """.format(
        hoehe, breite, link, breite, hoehe, scrolling, start_y
    )

    def on_button_clicked(b):
        webseite_verteilen(html)

    btn.on_click(on_button_clicked)


def webseite_verteilen(html: str):
    # ersten freien Port auswählen
    for port in range(1024, 36000):
        if not port_wird_genutzt(port):
            server = Process(
                target=start_server,
                args=(
                    port,
                    html,
                ),
            )
            server.start()

            time.sleep(0.5)
            webbrowser.open_new("http://127.0.0.1:{}".format(port))
            time.sleep(5)

            server.terminate()
            server.join()
            break
        else:
            print("Port {} belegt".format(port))
