import requests
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# sheet_endpoint = os.environ.get("SHEET_ENDPOINT")
# sheet_key = os.environ.get("SHEET_KEY")
#
# sheet_headers = {
#     "Authorization": f"Bearer {sheet_key}"
# }



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        # use creds to create a client to interact with the Google Drive API
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
        self.client = gspread.authorize(self.creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        self.sheet = self.client.open("Flight Deals").worksheets()


        # Extract and print all of the values
        # self.list_of_hashes = self.sheet.get_all_records()
        # print(self.list_of_hashes)

    def get_destination_data(self):
        self.destination_data = self.sheet[0].get_all_records()
        return self.destination_data

    def update_destination_codes(self):
        row = 2
        col = 2
        for city in range(len(self.destination_data)):
            self.sheet[0].update_cell(row, col, self.destination_data[city]["IATA Code"])
            row += 1

    def add_customer(self,name,surname,email):
        row_data = [name,surname,email]
        self.sheet[1].insert_row(values = row_data, index=2)

    def get_emails(self):
        customer_data = self.sheet[1].get_all_records()
        emails = [row['Email'] for row in customer_data]
        return emails



