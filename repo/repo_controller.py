from app import app
from repo.repo_model import repo_overview
from flask import jsonify, request

obj = repo_overview()

@app.route('/repo-details', methods=['POST'])
def repo_details_controller():
    return obj.get_github_repo_info(request.get_json())

@app.route('/repo-branches', methods=['POST'])
def repo_branches_controller():
    return obj.get_github_branch_info(request.get_json())

@app.route('/repo-collaborators', methods=['POST'])
def repo_collaborators_controller():
    return obj.get_github_collaborator_info(request.get_json())

@app.route('/combined-repo-data', methods=['POST'])
def combined_repo_data_controller():
    data = request.get_json()
    repo_info = obj.get_github_repo_info(data)
    branch_info = obj.get_github_branch_info(data)
    collaborator_info = obj.get_github_collaborator_info(data)

    combined_data = {
        'repo_details': repo_info,
        'branch_info': branch_info,
        'collaborator_info': collaborator_info
    }

    return combined_data
