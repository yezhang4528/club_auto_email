from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of the spreadsheet

def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    CLASS_SPREADSHEET_ID = '1ym_LSUI-4YPesJ9JJdv-JETfJBYQdmxpTlestlI1U58'
    CLASS_RANGE_NAME = 'PythonClassContacts!D2:E'
    result = service.spreadsheets().values().get(spreadsheetId=CLASS_SPREADSHEET_ID,
                                                range=CLASS_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('Error: No data found.')
    else:
        print('Parent Name, Email:')
        for row in values:
            # Print columns D and E, which correspond to 3 and 4.
            print('%s, %s' % (row[0], row[1]))


if __name__ == '__main__':
    main()
