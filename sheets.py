import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from constants import *
import time


def spreadsheet_processing(data: list):
    try:
        print('Sending spreadsheet data...')
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                       [
                                                                           'https://www.googleapis.com/auth/spreadsheets',
                                                                           'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

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
        print('Spreadsheet data send succesfull...')
    except Exception as err:
        print('err from google..')
        print(err)
        pass


def cleaning(dummy=None):
    try:
        print('Cleaning spreadsheet data...')
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                       [
                                                                           'https://www.googleapis.com/auth/spreadsheets',
                                                                           'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
        service.spreadsheets().values().clear(spreadsheetId=SPREADSHEET_ID,
                                              range=SHEET_RANGE_FINAL_RESULT).execute()
        print('Spreadsheet data is clean ...')
    except Exception as err:
        print('err from google..')
        print(err)
        pass
