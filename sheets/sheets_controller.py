from app import app
from flask import request, jsonify
from sheets.sheets_model import SheetsModel
from repo.repo_controller import combined_repo_data_controller

sheets_model = SheetsModel()

@app.route("/sheets/update", methods=["POST"])
def update_sheet():
    try:
        data = request.json
        sheets_model.update_sheet(data["column_values"])
        return jsonify({"message": "Sheet updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/update-sheet-with-repo-data', methods=["POST"])
def update_sheet_with_repo_data():
    repo_info = combined_repo_data_controller()
    
    
    response = sheets_model.update_sheet_with_repo_data(repo_info)
    return response

