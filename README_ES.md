# Fermax Blue Intercom Script

<a href="#" style="text-align: center;">
 <img src="https://github.com/cvc90/Fermax-Blue-Intercom/assets/76731844/b417dcc5-9b5f-49b2-8084-2e56338ed68e" width="15%" height="15%" alt="Fermax Blue" text-align="center" margin="0 0 0 0">
</a>

## 📑 Descripción

Script Fermax Blue para conectar con la API (Mostrar información de usuario, Mostrar información de intercomunicador, Historial de intercomunicación, abrir puerta)

## 📑 Uso

1. Clone el repositorio y navegue hasta el directorio raíz.
2. Instale el módulo de solicitudes ejecutando `pip install request`.
3. Ejecute el script con los argumentos requeridos: `python3 Fermax-Blue-Intercom.py --username <NOMBRE DE USUARIO> --contraseña <CONTRASEÑA>`.
4. Si desea evitar búsquedas adicionales, también puede proporcionar los argumentos opcionales `--deviceId` y `--accessId`.
5. El script generará un mensaje indicando si la puerta se abrió correctamente o no.

## 📑 Argumentos

- `--nombre de usuario`: Requerido. Nombre de usuario de la cuenta Fermax Blue.
- `--contraseña`: Requerido. Contraseña de la cuenta Fermax Blue.
- `--deviceId`: Opcional. ID del dispositivo para evitar búsquedas adicionales (requiere accessId).
- `--accessId`: Opcional. Acceda a los ID para evitar búsquedas adicionales (úselo con deviceId).
- `--cache`: Opcional. Configúrelo en Falso si no desea utilizar el caché para guardar el token de autenticación (habilitado de forma predeterminada).
- `--reauth`: Opcional. Úselo solo para forzar la reautenticación, cuando use esta opción no se abrirá ninguna puerta, solo úselo para actualizar el token, verificar sus credenciales...
- `--user-info`: Opcional. Información de la cuenta de usuario de Fermax Blue.
- `--user-info-json`: Opcional. Información de la cuenta de usuario de Fermax Blue en formato .json.
- `--pairings-info`: Opcional. Información sobre los dispositivos vinculados de la cuenta de usuario de Fermax Blue.
- `--pairings-info-json`: Opcional. Información de los dispositivos vinculados de la cuenta de usuario de Fermax Blue en formato .json.
- `--mydevice-info`: Opcional. Información sobre los dispositivos de la cuenta de usuario de Fermax Blue.
- `--mydevice-info-json`: Opcional. Información de los dispositivos de la cuenta de usuario de Fermax Blue en formato .json.
- `--mydevice-info`: Opcional. Historial de dispositivos de la cuenta de usuario de Fermax Blue.
- `--mydevice-info-json`: Opcional. Historial de dispositivos de la cuenta de usuario de Fermax Blue en formato .json.
- `--open-door`: Opcional. Acción para abrir la puerta.

## Ejemplos

### 🏠 Home Assistant

Puedes usar este script con Home Assistant usando la integración `shell_command`.

Guárdelo en un directorio bajo `config`, algo así como `your_home_assistant_dir/config/python_scripts/Fermax-Blue-Intercom.py`, luego agregue lo siguiente a su `configuration.yaml`:

*NOTA: Compruebe cómo se utiliza en los ejemplos siguientes.*

```
shell_command:
  open_door: 'python3 python_scripts/Fermax-Blue-Intercom.py --username USERNAME --password PASSWORD ...'
```

### Abriendo la primera puerta (¿tal vez CERO?)

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword
```

### Abrir la primera puerta y deshabilitar la caché del token de autenticación

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --cache False
```

### Abrir la puerta proporcionada

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}'
```

### Abrir varias puertas

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}' '{"subblock": 1, "block": 1, "number": 1}'
```

### Forzar autenticación

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --reauth
```

## 👷 Funcionamiento

El script envía una petición HTTP a los servidores de Fermax Blue para autenticar al usuario y obtener un token de acceso. El token de acceso se almacena en caché en un archivo JSON (en el directorio del script) para evitar llamadas innecesarias a la API en el futuro.

A continuación, el script envía otra petición HTTP a los servidores Fermax Blue para obtener el ID del dispositivo y el ID de acceso, necesarios para abrir la puerta.

Por último, el script envía una tercera petición HTTP a la API de Fermax Blue para abrir la puerta.

## ⚠️ Aviso

Este script fue probado en un Fermax VEO-XS WIFI 4,3" DUOX PLUS (REF: 9449)

## 📚 Documentación

- Configuración inicial de Docker: [Instrucciones Docker](/docs/DOCKER_INSTALLATION.md)
- Uso y configuración de la app: [Toda la documentación](docs/README.md)

## 📑 Requisitos mínimos del sistema

- [Python3](https://www.python.org/downloads/)

## 📑 Requisitos del sistema recomendados

- [Python3.11](https://www.python.org/downloads/)

## 🏴 Traducciones de este archivo

* <a href="README.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/gb.svg" alt="README.md" width="3%" height="3%"> Ingles
  </a>

* <a href="README_DE.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/de.svg" alt="README_DE.md" width="3%" height="3%"> Alemán
  </a> 

## ☕ Apóyame

Apóyame para mejorar el script Fermax Blue Intercom.

Siéntete libre de donar lo que quieras a las siguientes direcciones:

- Bitcoin (BTC): `1BughfdxS2zpqZUhtS5jhkbxDWHhtqTaxN`
- Ethereum (ETH): `0xbE3A0FcD3f1BB61CCeEC94Ab9FE683E071331E00`
- Dash: `XjZgQAeVuLcfywDpp2JxfmpvQn3MrmAEC2`
- Zcash (ZEC): `t1J5dnHVeaWvdv3L43A62fVC6YAajKFEMbX`
- XMR: `47HLtavHyu2UgXVb4apyNnE55mqQTuy1fgPzbNYosqaRak7nkksoqj9enP4eMjBems4kM577T8yRZagnsyB5yrXP32cBN3F`
- RTM: `RWRYFXpXwrWnWFzPSrp4oyCV6QYaWD3eqX`

## 📑 Licencia
  GPL 3.0 | [Lea más aquí](LICENSE.md) | Fuente del [GIF animado (Animación de carga)](https://commons.wikimedia.org/wiki/File:Loading_Animation.gif) | Fuente de las [Fuentes autoalojadas](https://github.com/adobe-fonts/source-sans)
