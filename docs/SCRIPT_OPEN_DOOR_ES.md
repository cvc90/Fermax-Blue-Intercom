# Fermax Blue Intercom (Script open_door.py)

<a href="#" style="text-align: center;">
 <img src="https://github.com/cvc90/Fermax-Blue-Intercom/assets/76731844/b417dcc5-9b5f-49b2-8084-2e56338ed68e" width="15%" height="15%" alt="Fermax Blue" text-align="center" margin="0 0 0 0">
</a>

## 📑 Descripción

Fermax Blue script para conectar con la API y poder abrir la puerta

## 📑 Uso

1. Clona el repositorio y navega hasta el directorio raíz.
2. Instala el módulo requests ejecutando `pip install requests`.
3. Ejecuta el script con los argumentos requeridos: `python3 open_door.py --username <USERNAME> --password <PASSWORD>`.
4. Si desea evitar la búsqueda adicional, también puede proporcionar los argumentos opcionales `--deviceId` y `--accessId`.
5. El script mostrará un mensaje indicando si la puerta se ha abierto correctamente o no.

## 📑 Argumentos

- `--username`: Obligatorio. Nombre de usuario de la cuenta Fermax Blue.
- `--password`: Requerido. Contraseña de la cuenta Fermax Blue.
- `--deviceId`: Opcional. ID del dispositivo para evitar la búsqueda adicional (requiere accessId).
- accessId`: Opcional. ID de acceso para evitar búsquedas adicionales (se utiliza con deviceId).
- `--cache`: Opcional. Establézcalo en False si no desea utilizar la caché para guardar el token de autenticación (activada por defecto).
- `--reauth`: Opcional. Úsalo para forzar la autenticación, cuando uses esta opción no se abrirá ninguna puerta, sólo úsala para refrescar el token, comprobar tus credenciales...
  
## Ejemplos

### 🏠 Home Assistant

Puedes usar este script con Home Assistant usando la integración `shell_command`.

Guárdalo en un directorio bajo `config`, algo como `your_home_assistant_dir/config/python_scripts/open_door.py`, luego añade lo siguiente a tu `configuration.yaml`:

*NOTA: Comprueba cómo se usa en los ejemplos de abajo.*

```
shell_command:
  open_door: 'python3 python_scripts/open_door.py --username USERNAME --password PASSWORD ...'
```

### Apertura de la primera puerta (¿tal vez CERO?)

```bash
open_door.py --username email@domain.com --password yourpassword
```

### Abrir la primera puerta y desactivar la caché de autentificadores

```bash
open_door.py --username email@domain.com --password yourpassword --cache False
```

### Abrir la puerta proporcionada

```bash
open_door.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}'
```

### Abrir varias puertas

```bash
open_door.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}' '{"subblock": 1, "block": 1, "number": 1}'
```

### Forzar autenticación

```bash
open_door.py --username email@domain.com --password yourpassword --reauth
```

## 👷 Cómo funciona

El script envía una petición HTTP a los Servidores Fermax Blue para autenticar al usuario y obtener un token de acceso. El token de acceso se almacena en caché en un archivo JSON (en el directorio del script) para evitar llamadas API innecesarias en el futuro.

Luego, el script envía otra solicitud HTTP a los Servidores Fermax Blue para obtener el ID del dispositivo y el ID de acceso, necesarios para abrir la puerta.

Finalmente, el script envía una tercera petición HTTP a la API de Fermax Blue para abrir la puerta.

## ⚠️ Aviso

Este script fue probado en un Fermax 9449.

## 📚 Documentación

- Configuración inicial de Docker: [Instrucciones para Docker](/docs/DOCKER_INSTALLATION.md)
- Uso y configuración de la aplicación: [Toda la documentación](docs/README.md)

## 📑 Requisitos mínimos del sistema

- [Python3](https://www.python.org/downloads/)

## 📑 Requisitos del sistema recomendados

- [Python3.8](https://www.python.org/downloads/)

## 🏴 Traducciones de este archivo

* <a href="/docs/SCRIPT_OPEN_DOOR.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/gb.svg" alt="SCRIPT_OPEN_DOOR.md" width="3%" height="3%"> Ingles
  </a>

* <a href="/docs/SCRIPT_OPEN_DOOR_DE.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/de.svg" alt="SCRIPT_OPEN_DOOR_DE.md" width="3%" height="3%"> Alemán
  </a> 

## ☕ Apoyame

Apóyame para mejorar el script Fermax Blue Intercom

Siéntete libre de donar lo que quieras a las siguientes direcciones:

- Bitcoin (BTC): `1BughfdxS2zpqZUhtS5jhkbxDWHhtqTaxN`
- Ethereum (ETH): `0xbE3A0FcD3f1BB61CCeEC94Ab9FE683E071331E00`
- Dash: `XjZgQAeVuLcfywDpp2JxfmpvQn3MrmAEC2`
- Zcash (ZEC): `t1J5dnHVeaWvdv3L43A62fVC6YAajKFEMbX`
- XMR: `47HLtavHyu2UgXVb4apyNnE55mqQTuy1fgPzbNYosqaRak7nkksoqj9enP4eMjBems4kM577T8yRZagnsyB5yrXP32cBN3F`
- RTM: `RWRYFXpXwrWnWFzPSrp4oyCV6QYaWD3eqX`

## 📑 Licencia
  GPL 3.0 | [Lea más aquí](LICENSE.md) | Fuente del [GIF animado (Animación de carga)](https://commons.wikimedia.org/wiki/File:Loading_Animation.gif) | Fuente de las [Fuentes autoalojadas](https://github.com/adobe-fonts/source-sans)
