# -*- coding: utf-8 -*-
# @Author: Z.BOUDAOUD
# @Email: zinedddine97@gmail.com

import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from constants.constants import SCOPES, SAMPLE_SPREADSHEET_ID


class GoogleSheet:
    """
    Class used to access and write in the Google Sheet
    """
    def __init__(self):
        """
        Init function found on https://developers.google.com/sheets/api/quickstart/python
        """
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('doc/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)
        self.sheet = self.service.spreadsheets()

    def add_company(self, company, range):
        """
        Add a line to the google sheet
        :param company: Company
            Company to add to the sheet, with its name and website
        :param range: str
            Range where to write datas
        :return:
        """
        values = [[company.name, company.url]]
        body = {'values': values}
        self.service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range,
                                                    valueInputOption='RAW', body=body).execute()
