# Fermax Blue Intercom Script

<a href="#" style="text-align: center;">
 <img src="https://github.com/cvc90/Fermax-Blue-Intercom/assets/76731844/b417dcc5-9b5f-49b2-8084-2e56338ed68e" width="15%" height="15%" alt="Fermax Blue" text-align="center" margin="0 0 0 0">
</a>

## 📑 Description

Fermax Blue script to connect with the API (Show user information, Show intercom information, Intercom history, open the door)

## 📑 Usage

1. Clone the repository and navigate to the root directory.
2. Install the requests module by running `pip install requests`.
3. Run the script with the required arguments: `python3 Fermax-Blue-Intercom.py --username <USERNAME> --password <PASSWORD>`.
4. If you want to avoid extra fetching, you can also provide the optional `--deviceId` and `--accessId` arguments.
5. The script will output a message indicating whether the door was successfully opened or not.

## 📑 Arguments

-   `--username`: Required. Fermax Blue account username.
-   `--password`: Required. Fermax Blue account password.
-   `--deviceId`: Optional. Device ID to avoid extra fetching (requires accessId).
-   `--accessId`: Optional. Access ID(s) to avoid extra fetching (use with deviceId).
-   `--cache`: Optional. Set to False if you don't want to use the cache to save the auth token (enabled by default).
-   `--reauth`: Optional. Use it to just force reauth, when using this option no door will be open, just use it to refresh the token, check your credentials...
-   `--user-info`: Optional. Fermax Blue user account information.
-   `--user-info-json`: Optional. Fermax Blue user account information in .json format.
-   `--pairings-info`: Optional. Information about the paired devices of the Fermax Blue user account.
-   `--pairings-info-json`: Optional. Information about the paired devices of the Fermax Blue user account in .json format.
-   `--mydevice-info`: Optional. Information about the Fermax Blue user account devices.
-   `--mydevice-info-json`: Optional. Information about the Fermax Blue user account devices in .json format.
-   `--mydevice-history`: Optional. History of Fermax Blue user account devices.
-   `--mydevice-history-json`: Optional. History of Fermax Blue user account devices in .json format.
-   `--open-door`: Optional. Action to open the door.
-   `--credits`: Optional. Show script version.
-   `--version`: Optional. Show script credits.

## Examples

### 🏠 Home Assistant

You can use this script with Home Assistant using the `shell_command` integration.

Save it in a directory under `config`, something like `your_home_assistant_dir/config/python_scripts/Fermax-Blue-Intercom.py`, then add the following to your `configuration.yaml`:

*NOTE: Check how it is used in the examples below.*

```
shell_command:
  open_door: 'python3 python_scripts/Fermax-Blue-Intercom.py --username USERNAME --password PASSWORD ...'
```

### Opening first door (maybe ZERO?)

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword
```

### Opening first door and disabling auth token cache

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --cache False
```

### Opening the provided door

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}'
```

### Opening multiple doors

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --deviceId 12345 --accessId '{"subblock": 0, "block": 0, "number": 0}' '{"subblock": 1, "block": 1, "number": 1}'
```

### Force authentication

```bash
Fermax-Blue-Intercom.py --username email@domain.com --password yourpassword --reauth
```

## 👷 How it works

The script sends an HTTP request to the Fermax Blue Servers to authenticate the user and obtain an access token. The access token is cached into a JSON file (in the script directory) to avoid unnecessary API calls in the future.

The script then sends another HTTP request to the Fermax Blue Servers to obtain the device ID and access ID, which are required to open the door.

Finally, the script sends a third HTTP request to the Fermax Blue API to open the door.

## ⚠️ Disclaimer

This script was tested on a Fermax VEO-XS WIFI 4,3" DUOX PLUS (REF: 9449)

## 📚 Documentation

- Initial Docker Setup: [Docker instructions](/docs/DOCKER_INSTALLATION.md)
- App Usage and Configuration: [All Documentation](docs/README.md)

## 📑 Minimum System Requirements

- [Python3](https://www.python.org/downloads/)

## 📑 Recommended System Requirements

- [Python3.11](https://www.python.org/downloads/)

## 🏴 Translations of this file

* <a href="README_ES.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/es.svg" alt="README_ES.md" width="3%" height="3%"> Spanish
  </a>

* <a href="README_DE.md">
   <img src="https://github.com/lipis/flag-icons/blob/main/flags/4x3/de.svg" alt="README_DE.md" width="3%" height="3%"> German
  </a> 

## ☕ Support me

Support me to improve Fermax Blue Intercom script

Feel free to donate whatever you want to the following addresses:

- Bitcoin (BTC): `1BughfdxS2zpqZUhtS5jhkbxDWHhtqTaxN`
- Ethereum (ETH): `0xbE3A0FcD3f1BB61CCeEC94Ab9FE683E071331E00`
- Dash: `XjZgQAeVuLcfywDpp2JxfmpvQn3MrmAEC2`
- Zcash (ZEC): `t1J5dnHVeaWvdv3L43A62fVC6YAajKFEMbX`
- XMR: `47HLtavHyu2UgXVb4apyNnE55mqQTuy1fgPzbNYosqaRak7nkksoqj9enP4eMjBems4kM577T8yRZagnsyB5yrXP32cBN3F`
- RTM: `RWRYFXpXwrWnWFzPSrp4oyCV6QYaWD3eqX`

## 📑 License
  GPL 3.0 | [Read more here](LICENSE.md) | Source of the [animated GIF (Loading Animation)](https://commons.wikimedia.org/wiki/File:Loading_Animation.gif) | Source of the [selfhosted Fonts](https://github.com/adobe-fonts/source-sans)
