#!/usr/bin/env python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .cyberark import Cyberark
from gspread.exceptions import WorksheetNotFound

class UMGoogleSheet(object):
    def __init__(self, ss):
        cyberark = Cyberark("UMNET")
        self.scope_app = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.service_account_email = str(cyberark.query_cyberark("gsheet_api_service_account_email"))
        self.project_id = str(cyberark.query_cyberark("gsheet_api_project_id"))
        self.client_id = str(cyberark.query_cyberark("gsheet_api_client_id"))
        self.private_key_id = str(cyberark.query_cyberark("gsheet_api_key_id"))
        self.private_key = str(cyberark.query_cyberark("gsheet_api_private_key")).replace("\\n", "\n")

        self.open_spreadsheet(ss)

    def _col_to_a1(col_num:int)->str:
        """
        Converts a column number to A1 notation.
        """

    def _gsheet_auth(self):
        json_creds = {
            "type": "service_account",
            "project_id": self.project_id,
            "private_key_id": self.private_key_id,
            "private_key": self.private_key,
            "client_email": self.service_account_email,
            "client_id": self.client_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/" + self.service_account_email.replace("@", "%40"),
        }
        cred = ServiceAccountCredentials.from_json_keyfile_dict(json_creds, self.scope_app)

        # authorize the clientsheet
        return gspread.authorize(cred)


    def open_spreadsheet(self, url_or_key):
        '''
        Opens a spreadsheet by url or by key. Detects a url by looking for 'https'
        '''
        self._client = self._gsheet_auth()
        if url_or_key.startswith('http'):
            self._ss = self._client.open_by_url(url_or_key)
        else:
            self._ss = self._client.open_by_key(url_or_key)

    def get_worksheet(self, ws_name):
        '''
        Gets a worksheet by name. If return as dict is set to true (default is yet),
        will return the results of "get all records". Otherwise will return a worksheet object.
        '''
        return self._ss.worksheet(ws_name)

    def get_worksheet_values(self, ws_name):
        ws = self.get_worksheet(ws_name)
        return ws.get_all_records()

    def open_and_get_worksheet(self, url_or_key, ws_name):
        """
        Opens a spreadsheet and gets a worksheet by name from that spreadsheet.
        """
        self.open_spreadsheet(url_or_key)
        return self.get_worksheet(ws_name, return_as_dict=True)

    def open_and_get_worksheet_values(self, url_or_key, ws_name):
        ws = self.open_and_get_worksheet(url_or_key, ws_name)
        return ws.get_all_records()

    def find_row_in_worksheet(self, ws_name, search_term, as_dict=True):
        """
        Finds the first row on a specific worksheet where the search term
        matches a cell in that row. If it is found, will either
        return as a dict with header (row 1) as the keys, or as a simple list
        """
        ws = self._ss.worksheet(ws_name)
        cell = ws.find(search_term)
        if cell:
            row = ws.row_values(cell.row)
            if as_dict:
                headers = ws.row_values(1)
                return {headers[i]:row[i] for i in range(0,len(row)-1)}
            else:
                return row
        else:
            return None


    def find_rows_in_worksheet(self, ws_name, search_term, as_dict=True):
        """
        Finds ALL rows on a specific worksheet where the search term
        matches a cell in that row. If it is found, will either
        return as a list of dicts with header (row 1) as the keys, or as a list of lists
        """
        ws = self._ss.worksheet(ws_name)
        cells = ws.findall(search_term)
        results = []
        for cell in cells:
            row = ws.row_values(cell.row)
            if as_dict:
                headers = ws.row_values(1)
                [row.append("") for x in range(0,len(headers)-len(row))]
                results.append({headers[i]:row[i] for i in range(0,len(headers))})
            else:
                results.append(row)
       
        return results
    
    def create_or_overwrite_worksheet(self, ws_name, data:list):
        """
        Creates a new worksheet or overwrites an existing one
        with the data provided.

        If the data is a dictionary, the keys become a header for row 1
        Otherwise data is assumed to be a list of lists of all the same
        length (letting gspreads api validate that)
        """

        if isinstance(data[0], dict):
            ws_data = []
            ws_data.append(list(data[0].keys()))
            [ ws_data.append(list(row.values())) for row in data ]
        elif isinstance(data[0], list):
            ws_data = data
        else:
            raise TypeError(f'Data must be a list of dicts or list of lists')
        
        try:
            ws = self._ss.worksheet(ws_name)
            ws.clear()
        except WorksheetNotFound:
            ws = self._ss.add_worksheet(ws_name, len(ws_data), len(ws_data[0]))
                
        last_cell = gspread.utils.rowcol_to_a1(len(ws_data), len(ws_data[0]))
        ws.update(f'A1:{last_cell}', ws_data)


    def diff_worksheets(self, ws1_name, ws2_name):
        """
        Compares the data on two worksheets. Rows that don't match are
        highlighted on both sheets
        """
        ws1 = self._ss.worksheet(ws1_name)
        ws2 = self._ss.worksheet(ws2_name)

        ws1_vals = ws1.get_values()
        ws2_vals = ws2.get_values()

        diff_cells = []
        for row1, row2, row_num in zip(ws1_vals, ws2_vals, range(1,len(ws1_vals))):
            for col1, col2, col_num in zip(row1, row2, range(1,len(row1))):
                if col1 != col2:
                    diff_cells.append((row_num, col_num))

        if diff_cells:
            formats = [
                { 
                    "range": gspread.utils.rowcol_to_a1(c[0], c[1]),
                    "format": {
                        "backgroundColor": {
                            "red": 1.0,
                            "green": 0.0,
                            "blue": 0.0,
                        }
                    }
                }

                for c in diff_cells
            ]
            ws1.batch_format(formats)
            ws2.batch_format(formats)
    
