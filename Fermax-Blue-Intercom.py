#######################################################################################
#                                  Fermax-Blue-Intercom                               #
#                      https://github.com/cvc90/Fermax-Blue-Intercom/                 #
#                                                                                     #
#                     Fermax Blue script to connect with the API                      #
# (Show user information, Show intercom information, Intercom history, open the door) #
#                                                                                     #
#                         Script file Fermax-Blue-Intercom.py                         #
#               A script that manages Fermax services through the Fermax API          #
#                                                                                     #
#   Usage: python3 Fermax-Blue-Intercom.py --username username --password password    #
#######################################################################################

# Imports required

import requests
import json
import logging
import argparse
import datetime
import os
import time

from urllib.parse import quote

# Version Script

version_script = "1.1"

# Github URL 

url_script = "https://github.com/cvc90/Fermax-Blue-Intercom/"

# Input values

parser = argparse.ArgumentParser()
parser.add_argument('--username', type=str,
                    help='Fermax Blue account username', required=True)
parser.add_argument('--password', type=str,
                    help='Fermax Blue account password', required=True)
parser.add_argument('--deviceId', type=str,
                    help='Optional deviceId to avoid extra fetching (requires accessId)')
parser.add_argument('--accessId', type=str, nargs='+',
                    help='Optional accessId(s) to avoid extra fetching (use with deviceId)')
parser.add_argument('--cache', type=bool,
                    help='Optionally set if cache is used to save/read auth token (enabled by default)', default=True)
parser.add_argument('--reauth', action='store_true',
                    help='Forces authentication (when using this option no door will be open)')	
parser.add_argument('--user-info', action='store_true',
                    help='Shows user account information')
parser.add_argument('--user-info-json', action='store_true',
                    help='Shows user account information in .json format')							
parser.add_argument('--pairings-info', action='store_true',
                    help='Shows information about the devices paired in the user account.')
parser.add_argument('--pairings-info-json', action='store_true',
                    help='Shows information about the devices paired in the user account in .json format.')
parser.add_argument('--mydevice-info', action='store_true',
                    help='Shows information about the device in the user account.')
parser.add_argument('--mydevice-info-json', action='store_true',
                    help='Shows information about the device in the user account in .json format')	
parser.add_argument('--mydevice-history', action='store_true',
                    help='Shows history about the device in the user account.')
parser.add_argument('--mydevice-history-json', action='store_true',
                    help='Shows history about the device in the user account in .json format')				
parser.add_argument('--open-door', action='store_true',
                    help='Action of opening the door')
parser.add_argument('--version', action='store_true',
                    help='Show script version')	
args = parser.parse_args()

username = args.username
password = args.password
deviceId = args.deviceId
accessIds = args.accessId
cache = args.cache
reauth = args.reauth
info_user = args.user_info
info_user_json = args.user_info_json
pairings_info = args.pairings_info
pairings_info_json = args.pairings_info_json
mydevice_info = args.mydevice_info
mydevice_info = args.mydevice_info_json
mydevice_info = args.mydevice_history
mydevice_info = args.mydevice_history_json
opendoor = args.open_door

if (deviceId and not accessIds) or (accessIds and not deviceId):
    raise Exception('Both deviceId and accessId must be provided')

provided_doors = deviceId and accessIds

if provided_doors:
    accessIds = list(map(lambda accessId: json.loads(accessId), accessIds))

# Cache file name

CACHE_FILENAME = 'Fermax-Blue-Intercom-cache.json'

# Date format

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# Get current directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cache file path
cache_file_path = os.path.join(script_dir, CACHE_FILENAME)

# Function - Update cached token

def update_cached_token(access_token: str, max_age: int):
    logging.info('Caching token...')

    current_datetime = datetime.datetime.now().strftime(DATETIME_FORMAT)

    cached_content = {
        'access_token': access_token,
        'max_age': max_age,
        'updated_at': current_datetime,
    }

    with open(cache_file_path, 'w') as file:
        json.dump(cached_content, file)

# Function - Read cached token

def read_cached_token() -> str:
    try:
        with open(cache_file_path, 'r') as file:
            cached_content = json.load(file)

            access_token = cached_content['access_token']
            max_age = cached_content['max_age']
            cache_datetime = datetime.datetime.strptime(
                cached_content['updated_at'], DATETIME_FORMAT)

        current_age = datetime.datetime.now() - cache_datetime
        if current_age.total_seconds() >= max_age:
            logging.info('Cached token has expired')
            return None
        else:
            return access_token
    except FileNotFoundError:
        logging.info('Cache file not found')
        return None


# Fake client app and iOS device

COMMON_HEADERS = {
    'app-version': '3.3.2',
    'accept-language': 'en-ES;q=1.0, es-ES;q=0.9, ru-ES;q=0.8',
    'phone-os': '16.4',
    'user-agent': 'Blue/3.3.2 (com.fermax.bluefermax; build:3; iOS 16.4.0) Alamofire/3.3.2',
    'phone-model': 'iPad14,5',
    'app-build': '3'
}

# Token access URL

AUTH_URL = 'https://oauth.blue.fermax.com/oauth/token'

# Authorization headers

AUTH_HEADERS = {
    'Authorization': 'Basic ZHB2N2lxejZlZTVtYXptMWlxOWR3MWQ0MnNseXV0NDhrajBtcDVmdm81OGo1aWg6Yzd5bGtxcHVqd2FoODV5aG5wcnYwd2R2eXp1dGxjbmt3NHN6OTBidWxkYnVsazE=',
    'Content-Type': 'application/x-www-form-urlencoded'
}
AUTH_HEADERS.update(COMMON_HEADERS)

# Function - Authentication 

def auth(cache: bool, username: str, password: str) -> str:
    username = quote(username)
    password = quote(password)
    auth_payload = f'grant_type=password&password={password}&username={username}'

    response = requests.request(
        'POST', AUTH_URL, headers=AUTH_HEADERS, data=auth_payload)

    parsed_json = response.json()
    if 'error' in parsed_json:
        raise RuntimeError(parsed_json['error_description'])

    access_token = parsed_json['access_token']
    max_age = parsed_json['expires_in']

    if cache:
        update_cached_token(access_token, max_age)

    return access_token

# Function - Get json headers 

def get_json_headers(bearer_token: str) -> str:
    headers = {'Authorization': bearer_token,
               'Content-Type': 'application/json'}
    headers.update(COMMON_HEADERS)

    return headers

# Pairing url

PAIRINGS_URL = 'https://blue.fermax.com/pairing/api/v3/pairings/me'

# Function - Pairings

def pairings(bearer_token: str) -> tuple:
    response = requests.request(
        'GET', PAIRINGS_URL, headers=get_json_headers(bearer_token), data={})

    parsed_json = response.json()

    if not parsed_json:
        raise Exception('There are no pairings')

    pairing = parsed_json[0]
    tag = pairing['tag']
    deviceId = pairing['deviceId']
    accessDoorMap = pairing['accessDoorMap']

    accessIds = []
    for d in accessDoorMap.values():
        if d['visible']:
            accessIds.append(d['accessId'])

    return (tag, deviceId, accessIds)

# Function - Directed opendoor

def directed_opendoor(bearer_token: str, deviceId: str, accessId: str) -> str:
    directed_opendoor_url = f'https://blue.fermax.com/deviceaction/api/v1/device/{deviceId}/directed-opendoor'

    payload = json.dumps(accessId)

    response = requests.request(
        'POST', directed_opendoor_url, headers=get_json_headers(bearer_token), data=payload)

    return response.text

# Function - Get token

def get_token():

	# Obtenemos Token
	access_token = None

	if cache and not reauth:
		access_token = read_cached_token()

	if not access_token:
		logging.info('Logging in into Blue...')

		access_token = auth(cache, username, password)

	bearer_token = f'Bearer {access_token}'
	
	return bearer_token

# Function - Get user info

def get_user_info():
	"""Gets user information"""
	
	# Perform the GET request
	url = "https://blue.fermax.com/user/api/v1/users/me"
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"Error obtaining user information: Error {response.status_code}")
		return
			
	# Decode the content of the response
	data = response.json()

	# Display user information
	print(f"\n------------")
	print(f"USER INFO")
	print(f"------------")
	print(f"Name: {data['name']}")
	print(f"Language: {data['locale']}")
	print(f"Email: {data['email']}")
	print(f"Accept Sharing: {data['acceptSharing']}")
	print(f"Accept Privacy: {data['acceptPrivacy']}")
	print(f"Enabled: {data['enabled']}")
	print(f"Created at: {data['createdAt']}")
	print(f"City: {data['city']}")
	print(f"Area: {data['area']}")
	print(f"Zone: {data['zone']}")
	print(f"Subzone: {data['subzone']}")
	print(f"Pin: {data['pin']}")
	print(f"Date of the pin: {data['pinDate']}")
	print(f"Unique session: {data['uniqueSession']}")
	print(f"Provider: {data['provider']}")

# Function - Get user info json

def get_user_info_json():
	"""Gets the user information in json format"""
	
	# Perform the GET request
	url = "https://blue.fermax.com/user/api/v1/users/me"
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"Error obtaining user information in json format: Error {response.status_code}")
		return
			
	# Decode the content of the response
	data = response.json()

	# Display user information in json format
	print(f"\n------------")
	print(f"USER INFO (JSON)")
	print(f"------------")
	print(f"{data}")

# Function - Get pairings info

def get_pairings_info():
	"""Obtains information from the user's paired devices"""

	# Perform the GET request
	url = "https://blue.fermax.com/pairing/api/v3/pairings/me"
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"\nError al obtener la información de los dispositivos pareados: Error{response.status_code}")
		return

	# Decode the content of the response
	data2 = response.json()

	# Show the information of the user's paired devices
	print(f"\n------------")
	print(f"INFO PAIRED DEVICES")
	print(f"------------")
	print(f"ID: {data2[0].get('id')}")
	print(f"Device Id: {data2[0].get('deviceId')}")
	print(f"Tag: {data2[0].get('tag')}")
	print(f"Status: {data2[0].get('status')}")
	print(f"Updated at: {data2[0].get('updatedAt')}")
	print(f"Created at: {data2[0].get('createdAt')}")
	print(f"App Build: {data2[0].get('appBuild')}")
	print(f"App Version: {data2[0].get('appVersion')}")
	print(f"Phone Model: {data2[0].get('phoneModel')}")
	print(f"phone OS: {data2[0].get('phoneOS')}")	
	print(f"Home: {data2[0].get('home')}")
	print(f"Address: {data2[0].get('address')}")
	print(f"Access door map: {data2[0].get('accessDoorMap')}")	
	print(f"Master: {data2[0].get('master')}")

# Function - Get pairings info json

def get_pairings_info_json():
	"""Gets the user's paired device information in .json format"""
	
	# Perform the GET request
	url = "https://blue.fermax.com/pairing/api/v3/pairings/me"
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"\nError in obtaining information from paired devices: Error {response.status_code}")
		return
			
	# Decode the content of the response
	data2 = response.json()

	# Show the information of the paired devices
	print(f"\n------------")
	print(f"INFO PAIRED DEVICES (JSON)")
	print(f"------------")
	print(f"ID: {data2}")

# Function - Get mydevice info

def get_mydevice_info():
	"""Obtains information from the user's intercom"""

	# Perform the GET request
	url = "https://blue.fermax.com/deviceaction/api/v1/device/{}".format(deviceId)
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"\nError obtaining Intercom information: Error {response.status_code}")
		return
			
	# Decode the content of the response
	data = response.json()

	# Show the user's intercom information
	print(f"\n------------")
	print(f"INTERCOM INFO")
	print(f"------------")
	print(f"Device ID: {data['deviceId']}")
	print(f"Connection stat: {data['connectionState']}")
	print(f"Status: {data['status']}")
	print(f"Installation ID: {data['installationId']}")
	print(f"Family: {data['family']}")
	print(f"Type: {data['type']}")
	print(f"Subtype: {data['subtype']}")
	print(f"Num block: {data['numBlock']}")
	print(f"Num subblock: {data['numSubblock']}")
	print(f"Unit number: {data['unitNumber']}")
	print(f"Connectable: {data['connectable']}")
	print(f"Icc ID: {data['iccid']}")
	print(f"Divert service: {data['divertService']}")
	print(f"Photocaller: {data['photocaller']}")
	print(f"Wireless signal: {data['wirelessSignal']}")
	print(f"BlueStream: {data['blueStream']}")
	print(f"Phone: {data['phone']}")
	print(f"Monitor: {data['monitor']}")
	print(f"Panel or edibox: {data['panelOrEdibox']}")
	print(f"Monitor or guard unit: {data['monitorOrGuardUnit']}")
	print(f"Terminal: {data['terminal']}")
	print(f"Streaming mode: {data['streamingMode']}")
	print(f"Panel: {data['panel']}")

# Function - Get mydevice info json

def get_mydevice_info_json():
	"""Gets the user's intercom information in .json format"""
	
	# Perform the GET request
	url = "https://blue.fermax.com/deviceaction/api/v1/device/{}".format(deviceId)
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"\nError when obtaining information from the Intercom: Error {response.status_code}")
		return
			
	# Decode the content of the response
	data = response.json()

	# Show the information of the Intercom:
	print(f"\n------------")
	print(f"INTERCOM INFO (JSON)")
	print(f"------------")
	print(f" {data}")

# Function - Get mydevice history

def get_mydevice_history():
	"""Get the user's intercom history"""
	
	# Perform the GET request
	url = "https://blue.fermax.com/services2/api/v1/services/{}".format(deviceId)
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"\nError when obtaining information from the Intercom: Error {response.status_code}")
		return
			
	# Decode the content of the response
	data = response.json()

	# Show the user's intercom history
	print(f"\n------------")
	print(f"INTERCOM HISTORY")
	print(f"------------")	
	print(f"Access name: {data[0].setdefault('AccessName', None)}")
	print(f"Auto on: {data[0]['AutoOn']}")
	print(f"Call divert: {data['CallDivert']}")
	print(f"Call registry: {data['CallRegistry']}")
	print(f"Change video source: {data['ChangeVideoSource']}")
	print(f"Check information': {data['CheckInformation']}")
	print(f"DND: {data['DND']}")
	print(f"Doormatic: {data['Doormatic']}")
	print(f"Event registry: {data['EventRegistry']}")
	print(f"F1: {data['F1']}")
	print(f"F1 options: {data['F1Options']}")
	print(f"Geo: {data['Geo']}")
	print(f"Guard: {data['Guard']}")
	print(f"Guests {data['Guest5']}")
	print(f"Manage call divert: {data['ManageCallDivert']}")
	print(f"Open door: {data['OpenDoor']}")
	print(f"Photocaller: {data['Photocaller']}")
	print(f"Ringtone: {data['Ringtone']}")
	print(f"Sessions unlimited: {data['SessionsUnlimited']}")
	print(f"TZ: {data['TZ']}")

# Function - Get mydevice history json

def get_mydevice_history_json():
	"""Gets the user's intercom history in json format"""
	
	# Perform the GET request
	url = "https://blue.fermax.com/services2/api/v1/services/{}".format(deviceId)
	response = requests.get(url, headers=get_json_headers(bearer_token))

	# Check the status of the response
	if response.status_code != 200:
		print(f"\nError when obtaining information from the Intercom: Error {response.status_code}")
		return
			
	# Decode the content of the response
	data = response.json()

	# Show the user's intercom history in .json format
	print(f"\n------------")
	print(f"INTERCOM HISTORY (JSON)")
	print(f"------------")
	print(f"{data}")

# Function - Open door

def open_door():
	"""Open door"""
	
	if not provided_doors:
		logging.info('Success, getting devices...')

		tag, deviceId, accessIds = pairings(bearer_token)

		logging.info(
			f'Found {tag} with deviceId {deviceId} ({len(accessIds)} doors), calling directed opendoor...')

	else:
		logging.info(
			f'Success, using provided deviceId {deviceId}, calling directed opendoor...')

	if not reauth:
		# If user provided doors we open them all
		if provided_doors:
			for accessId in accessIds:
				result = directed_opendoor(bearer_token, deviceId, accessId)
				logging.info(f'Result: {result}')
				time.sleep(7)

		# Otherwise we just open the first one (ZERO?)
		else:
			result = directed_opendoor(bearer_token, deviceId, accessIds[0])
			logging.info(f'Result: {result}')

	# Show message if door is opened or failed to open
  	if result == "la puerta abierta" or result == "the door is open":
		print("\The door has been opened")
	else:
		print("\nError opening the door")

# Función - Get version script

def get_version_script():
	"""Gets the current version of the script"""
	
	# Show the message with the current version of the script
	print(f"\n")
	print(f"Version: {version_script}")

# Program

# Get the access token.
bearer_token = get_token()

# Execute a pairings
pairings(bearer_token)

# Get the device ID and access ID.
deviceId = pairings(bearer_token)[1]
accessId = pairings(bearer_token)[2]

# If the user enters the argument "--user-info"
if args.user_info:
	get_user_info()

# If the user enters the argument "--user-info-json"
if args.user_info_json:
	get_user_info_json()

# If the user enters the argument "--pairings-info"
if args.pairings_info:
	get_pairings_info()

# If the user enters the argument "--pairings-info-json"
if args.pairings_info_json:
	get_pairings_info_json()

# If the user enters the argument "--mydevice-info"	
if args.mydevice_info:
	get_mydevice_info()

# If the user enters the argument "--mydevice-info-json"	
if args.mydevice_info_json:
	get_mydevice_info_json()

# If the user enters the argument "--mydevice-history"
if args.mydevice_history:
	get_mydevice_history()

# If the user enters the argument "--mydevice-history-json"	
if args.mydevice_history_json:
	get_mydevice_history_json()

# If the user enters the argument "--open-door"
if args.open_door:
	open_door()

# If the user enters the argument "--version"
if args.version:
	get_version_script()	
