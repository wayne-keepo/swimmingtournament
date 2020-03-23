from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_ID = '1uvjMM6L-f7WQlc1haP_z1hGV1axgBgbVUDj2z1OecA4'

CREDENTIALS_FILE = 'resources/creds.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range='A1:C6').execute()

pprint(result['values'])
print(type(result['values']))
# SwimmingTournament
