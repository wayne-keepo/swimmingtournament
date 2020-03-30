from classes import *
from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from constants import *


def spreadsheet_processing(data: list):
    if len(data) > 0:
        try:
            print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                           [
                                                                               'https://www.googleapis.com/auth/spreadsheets',
                                                                               'https://www.googleapis.com/auth/drive'])
            httpAuth = credentials.authorize(httplib2.Http())
            service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

            def send_to_sheet():
                body = {
                    "valueInputOption": VALUE_INPUT_OPTION,
                    "data": [
                        {
                            "range": SHEET_RANGE_FINAL_RESULT,
                            "majorDimension": MAJOR_DIMENSION,
                            "values": data
                        }
                    ]
                }
                print("request to google sheets:")
                pprint(body)
                req = service.spreadsheets().values().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
                pprint(req)

            send_to_sheet()

            print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        except Exception as err:
            print('err from google..')
            print(err)
            pass


# rang track fullname time
"""
[
	{
		'index': 4, 
		'info': {
			"track": "4", 
			"first_name": "Анастасия", 
			"last_name": "Ордина", 
			"rank": "1", 
			"lap": "2", 
			"lane_time": "1:6.84", 
			"raw_time": "668408", 
			"spreadsheet_data": "['1', '4', 'Анастасия Ордина', '1:6.84']"
		},
		'rank': 1, 
		'isfull': True, 
		'spreadsheet_data': ['1', '4', 'Анастасия Ордина', '1:6.84']
	}
]
"""
