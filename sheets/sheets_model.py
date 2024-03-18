import gspread
from google.oauth2.service_account import Credentials

class SheetsModel():
    def __init__(self):
        try:
            scopes = ["https://www.googleapis.com/auth/spreadsheets"]
            creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
            self.client = gspread.authorize(creds)
            self.sheet_id = "1b_WuKh0xKlkv8CGN89jBWpQkTDEDOAOEeteiewMkNZ0"
            self.workbook=self.client.open_by_key(self.sheet_id)
            self.sheet = self.workbook.worksheet("Sheet1")
        except Exception as e:
            print("Error:", e)

    def update_sheet(self, column_values):
        try:
            self.sheet.clear()
            print()
            self.sheet.update(f"A1:L{len(column_values)}", column_values)
            self.sheet.format(f"A1:L1", {"textFormat": {"bold": True}})
            print("Sheet updated successfully")
        except Exception as e:
            print("Error updating sheet:", e)
    
    def find_repo_row(self, repo_name):
        cell_list = self.sheet.findall(repo_name)
        for cell in cell_list:
            if cell.col == 1:
                return cell.row
        return None
            
    def update_sheet_with_repo_data(self, combined_data):
        repo_name = combined_data['repo_details']['repo_name']
        repo_row = self.find_repo_row(repo_name)
        
        branch_names = ', '.join(combined_data['branch_info']['branch_names'])
        collaborators = ', '.join(combined_data['collaborator_info']['collaborators'])

        
        data_to_insert = [
            combined_data['repo_details']['repo_name'],
            combined_data['branch_info']['branch_number'],
            branch_names,
            combined_data['collaborator_info']['collaborator_number'],
            collaborators,
            combined_data['repo_details']['repo_created_at'],
            combined_data['repo_details']['repo_default_branch'],
            combined_data['repo_details']['repo_description'],
            combined_data['repo_details']['repo_forks_count'],
            combined_data['repo_details']['repo_full_name'],
            combined_data['repo_details']['repo_owner_details'],
            combined_data['repo_details']['is_private']
        ]
        
        if repo_row:
            self.sheet.update(f"A{repo_row}:L{repo_row}", [data_to_insert])
            return {"message": "Sheet updated successfully"}
        
        else:
            self.sheet.append_row(data_to_insert)
            return {"message": "New row added successfully"}
