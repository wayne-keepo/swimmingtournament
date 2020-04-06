from classes import *
from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from constants import *


def spreadsheet_processing(data: list):
    try:
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
            req = service.spreadsheets().values().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()

        send_to_sheet()
    except Exception as err:
        print('err from google..')
        print(err)
        pass
