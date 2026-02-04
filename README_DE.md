# Fermax Blue Intercom Script

<a href="#" style="text-align: center;">
 <img src="https://github.com/cvc90/Fermax-Blue-Intercom/assets/76731844/b417dcc5-9b5f-49b2-8084-2e56338ed68e" width="15%" height="15%" alt="Fermax Blue" text-align="center" margin="0 0 0 0">
</a>

## 📑 Beschreibung

Fermax Blue Skript zur Verbindung mit der API (Benutzerinformationen anzeigen, Gegensprechanlageninformationen anzeigen, Gegensprechanlagenverlauf, Tür öffnen)

## 📑 Verwendung

1. Klonen Sie das Repository und navigieren Sie zum Stammverzeichnis.
2. Installieren Sie das Requests-Modul, indem Sie `pip install requests` ausführen.
3. Führen Sie das Skript mit den erforderlichen Argumenten aus: `python3 Fermax-Blue-Intercom.py --username <USERNAME> --password <PASSWORD>`.
4. Wenn Sie zusätzliche Abrufe vermeiden wollen, können Sie auch die optionalen Argumente `--deviceId` und `--accessId` angeben.
5. Das Skript gibt eine Meldung aus, die angibt, ob die Tür erfolgreich geöffnet wurde oder nicht.

## 📑 Argumente

-   `--username`: Erforderlich. Fermax Blue Konto-Benutzername.
-   `--password`: Erforderlich. Passwort des Fermax Blue-Kontos.
-   `--deviceId`: Optional. Geräte-ID, um zusätzliche Abrufe zu vermeiden (erfordert accessId).
-   `--accessId`: Optional. Zugriffs-ID(s) zur Vermeidung zusätzlicher Abrufe (Verwendung mit deviceId).
-   `--cache`: Optional. Setzen Sie auf False, wenn Sie den Cache nicht zum Speichern des Auth-Tokens verwenden wollen (standardmäßig aktiviert).
-   `--reauth`: Optional. Verwenden Sie diese Option, um eine erneute Authentifizierung zu erzwingen. Wenn Sie diese Option verwenden, wird keine Tür geöffnet, sondern nur das Token aktualisiert, Ihre Anmeldedaten überprüft...
-   `--user-info`: Optional. Fermax Blue Benutzerkontoinformationen.
-   `--user-info-json`: Optional. Fermax Blue Benutzerkontoinformationen im .json-Format.
-   `--pairings-info`: Wahlweise. Informationen über die gepaarten Geräte des Fermax Blue Benutzerkontos.
-   `--pairings-info-json`:  Optional. Informationen über die gepaarten Geräte des Fermax Blue-Benutzerkontos im .json-Format.
-   `--mydevice-info`: Optional. Informationen über die Geräte des Fermax Blue Benutzerkontos.
-   `--mydevice-info-json`: Optional. Informationen über die Geräte des Fermax Blue-Benutzerkontos im .json-Format.
-   `--mydevice-history`: Optional. Historie der Fermax Blue Benutzerkonto-Geräte.
-   `--mydevice-history-json`: Optional. Historie der Fermax Blue Benutzerkonto-Geräte im .json-Format.
-   `--open-door`: Optional. Aktion zum Öffnen der Tür.
-   `--credits`: Optional. Skript-Credits anzeigen.
-   `--version`: Optional. Skriptversion anzeigen.

## Beispiele

### 🏠 Home Assistant

Sie können dieses Skript mit Home Assistant unter Verwendung der `shell_command`-Integration verwenden.

Speichern Sie es in einem Verzeichnis unter `config`, etwa `Ihr_home_assistant_dir/config/python_scripts/Fermax-Blue-Intercom.py`, und fügen Sie dann Folgendes zu Ihrer `configuration.yaml` hinzu:

*HINWEIS: Prüfen Sie, wie es in den Beispielen unten verwendet wird.*

```
shell_command:
  open_door: 'python3 python_scripts/Fermax-Blue-Intercom.py --username USERNAME --password PASSWORD ...'
```

### Erste Tür öffnen (vielleicht NULL?)

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword
```

### Öffnen der ersten Tür und Deaktivieren des Zwischenspeichers für Authentifizierungstoken

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --cache False
```

### Öffnen der vorgesehenen Tür

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}'
```

### Mehrere Türen öffnen

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}' '{"subblock": 1, "block": 1, "number": 1}'
```

### Force authentication

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --reauth
```

## 👷 So funktioniert es

Das Skript sendet eine HTTP-Anfrage an die Fermax Blue Server, um den Benutzer zu authentifizieren und ein Zugangs-Token zu erhalten. Das Zugriffstoken wird in einer JSON-Datei (im Skriptverzeichnis) zwischengespeichert, um in Zukunft unnötige API-Aufrufe zu vermeiden.

Anschließend sendet das Skript eine weitere HTTP-Anfrage an die Fermax Blue Server, um die Geräte-ID und die Zugangskennung zu erhalten, die zum Öffnen der Tür erforderlich sind.

Schließlich sendet das Skript eine dritte HTTP-Anfrage an die Fermax Blue API, um die Tür zu öffnen.

## ⚠️ Haftungsausschluss

Dieses Skript wurde auf einem Fermax VEO-XS WIFI 4,3" DUOX PLUS (REF: 9449)

## 📚 Dokumentation

- Erste Docker-Einrichtung: [Docker-Anleitung](/docs/DOCKER_INSTALLATION.md)
- Verwendung und Konfiguration der Anwendung: [Alle Dokumentation](docs/README.md)

## 📑 Minimale Systemanforderungen

- [Python3](https://www.python.org/downloads/)

## 📑 Empfohlene Systemanforderungen

- [Python3.11](https://www.python.org/downloads/)

## 🏴 Übersetzungen dieser Datei

* <a href="README.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/gb.svg" alt="README.md" width="3%" height="3%"> Englisch
  </a> 

* <a href="README_ES.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/es.svg" alt="README_ES.md" width="3%" height="3%"> Spanisch
  </a>

## ☕ Unterstützen Sie mich

Unterstützen Sie mich bei der Verbesserung des Fermax Blue Intercom Skripts

Sie können an die folgenden Adressen spenden, was immer Sie wollen:

- Bitcoin (BTC): `1BughfdxS2zpqZUhtS5jhkbxDWHhtqTaxN`
- Ethereum (ETH): `0xbE3A0FcD3f1BB61CCeEC94Ab9FE683E071331E00`
- Dash: `XjZgQAeVuLcfywDpp2JxfmpvQn3MrmAEC2`
- Zcash (ZEC): `t1J5dnHVeaWvdv3L43A62fVC6YAajKFEMbX`
- XMR: `47HLtavHyu2UgXVb4apyNnE55mqQTuy1fgPzbNYosqaRak7nkksoqj9enP4eMjBems4kM577T8yRZagnsyB5yrXP32cBN3F`
- RTM: `RWRYFXpXwrWnWFzPSrp4oyCV6QYaWD3eqX`

## 📑 Lizenz
  AGPL 3.0 | [Hier mehr lesen](LICENSE.md) | Quelle des [animierten GIF (Ladeanimation)](https://commons.wikimedia.org/wiki/File:Loading_Animation.gif) | Quelle der [selbst gehosteten Schriftarten](https://github.com/adobe-fonts/source-sans)
