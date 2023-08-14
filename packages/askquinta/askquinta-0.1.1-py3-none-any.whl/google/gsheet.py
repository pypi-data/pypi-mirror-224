import os
from dotenv import load_dotenv

import pandas as pd
import pygsheets

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the current directory of the script (package directory)
package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Navigate to the credentials directory inside the package
credentials_dir = os.path.join(package_dir, 'credentials')

# Load environment variables from the login_credentials.env file
env_file_path = os.path.join(credentials_dir, 'login_credentials.env')
load_dotenv(dotenv_path=env_file_path)

# ============================================================
# Config Do not Touch
# ============================================================
gsheet_credential_location = os.getenv("gsheet_config_cred_location")

# ============================================================
# Functions
# ============================================================

class GsheetConnector:
    """
    A class to connect and interact with Google Sheets using pygsheets.

    Attributes:
        credential_location (str): The file path to the Google Sheets API credential file.

    Methods:
        __init__(self, credential_location):
            Initializes the GsheetConnector object with the provided credential file location.

        push_gsheets(self, sheet_name, tab_sheet, cell, df, copy_head=True):
            Pushes a DataFrame to a specified Google Sheets tab.

        pull_gsheets(self, sheet_name, tab_sheet, index):
            Pulls data from a specified Google Sheets tab and returns it as a DataFrame.
    """

    def __init__(self):
        """
        Initializes the GsheetConnector object with the provided credential file location.

        Args:
            credential_location (str): The file path to the Google Sheets API credential file.
        """
        self.credential_location = gsheet_credential_location
        self.client = pygsheets.authorize(service_file=self.credential_location)

    def push_gsheets(self, sheet_name, tab_sheet, cell, df, copy_head=True):
        """
        Pushes a DataFrame to a specified Google Sheets tab.

        Args:
            sheet_name (str): The name of the Google Sheets file.
            tab_sheet (str): The title of the Google Sheets tab.
            cell (str): The cell in the Google Sheets where the DataFrame should be placed.
            df (pd.DataFrame): The DataFrame to be pushed to the Google Sheets.
            copy_head (bool, optional): Whether to copy the column headers from the DataFrame to the Google Sheets.
                                        Default is True.

        Raises:
            pygsheets.SpreadsheetNotFound: If the specified Google Sheets file is not found.
        """
        try:
            sheet = self.client.open(sheet_name)
        except:
            print("Sheet is not found, creating a new sheet")
            self.create_gsheet(sheet_name)
            sheet = self.client.open(sheet_name)
        
        worksheet = sheet.worksheet_by_title(tab_sheet)  
        worksheet.set_dataframe(df, start = cell, copy_index=False, copy_head=copy_head, extend=True, fit=False, escape_formulae=False)
        print('Store to Google Sheet Done!')

    def pull_gsheets(self, sheet_name, tab_sheet, index):
        """
        Pulls data from a specified Google Sheets tab and returns it as a DataFrame.

        Args:
            sheet_name (str): The name of the Google Sheets file.
            tab_sheet (str): The title of the Google Sheets tab.
            index (int): The row index where the column headers are located.

        Returns:
            pd.DataFrame: The DataFrame containing the data from the specified Google Sheets tab.

        Raises:
            pygsheets.SpreadsheetNotFound: If the specified Google Sheets file is not found.
        """
        sheet = self.client.open(sheet_name)
        worksheet = sheet.worksheet_by_title(tab_sheet)  

        data = worksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False)
        df = pd.DataFrame(data)
        df.columns = df.iloc[index - 1]
        df.drop([index - 1], inplace=True, axis=0)
        df.reset_index(inplace=True, drop=True)
        return df
    
    def create_gsheet(self, sheet_name):
        """
        Creates a new Google Sheets file with the given name.

        Args:
            sheet_name (str): The name of the new Google Sheets file.

        Returns:
            pygsheets.Spreadsheet: The newly created Google Sheets file object.

        Raises:
            pygsheets.SpreadsheetExists: If a Google Sheets file with the given name already exists.
        """
        
        try:
            sheet = self.client.open(sheet_name)
            url_name = self.get_gsheet_url(sheet_name)
            print(f"A Google Sheets file with the name '{sheet_name}' already exists here {url_name}")
        except:
            # Create a new Google Sheets file
            spreadsheet = self.client.create(sheet_name)
            # Show the result
            self.get_gsheet_url(sheet_name)
            # Set default email share
            default_email_share = ['data-drive@paper.id']
            self.share_gsheet_with_emails(sheet_name=sheet_name, emails=default_email_share)
            
            print(f"New Google Sheets file '{sheet_name}' created.")
            return spreadsheet
    
    def get_gsheet_url(self, sheet_name):
        """
        Retrieves the URL of the given Google Sheets file.

        Args:
            sheet_name (str): The name of the Google Sheets file.

        Returns:
            str: The URL of the Google Sheets file.

        Raises:
            pygsheets.SpreadsheetNotFound: If the specified Google Sheets file is not found.
        """
        try:
            # Open the existing Google Sheets file
            sheet = self.client.open(sheet_name)
            return sheet.url
        except pygsheets.exceptions.SpreadsheetNotFound:
            raise ValueError(f"Google Sheets file with name '{sheet_name}' not found.")
    
    def share_gsheet_with_emails(self, sheet_name, emails):
        """
        Shares the specified Google Sheets file with edit access to multiple email addresses.

        Args:
            sheet_name (str): The name of the Google Sheets file to be shared.
            emails (list): A list of email addresses to share the Google Sheets file with.

        Raises:
            pygsheets.SpreadsheetNotFound: If the specified Google Sheets file is not found.
        """
        try:
            # Open the existing Google Sheets file
            sheet = self.client.open(sheet_name)

            # Share the Google Sheets file with edit access to each email address
            for email in emails:
                sheet.share(email, role='writer')

            print(f"Shared Google Sheets file '{sheet_name}' with {len(emails)} email addresses.")
        except pygsheets.exceptions.SpreadsheetNotFound:
            raise ValueError(f"Google Sheets file with name '{sheet_name}' not found.")