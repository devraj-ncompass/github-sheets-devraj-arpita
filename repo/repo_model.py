from flask import Flask
from flask import make_response
import pip._vendor.requests
from app import token

class repo_overview():
    def get_github_repo_info(self, data):
       
        owner = data['owner']
        repo = data['repo']


        base_url = f'https://api.github.com/repos/{owner}/{repo}'


        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }


        response1 = pip._vendor.requests.get(base_url, headers=headers)


        if response1.status_code == 200:
            details1 = response1.json()
           


            repo_all_details = {
                'repo_name': details1['name'],
                'repo_full_name' : details1['full_name'],
                'repo_created_at': details1['created_at'],
                'repo_default_branch': details1['default_branch'],
                'repo_description' : details1['description'],
                'repo_forks_count': details1['forks_count'],
                'repo_owner_details' : details1['owner']['login'],
                'is_private': details1['private'],
            }
           
            return repo_all_details
        else:
            return {'error': 'Unable to fetch repository information'}
       


    def get_github_branch_info(self, data):
       
        owner = data['owner']
        repo = data['repo']


        url = f'https://api.github.com/repos/{owner}/{repo}/branches?per_page=100&page=3'
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }


        response = pip._vendor.requests.get(url, headers=headers)
        if response.status_code == 200 :
            details = response.json()
            branch_names = [branch['name'] for branch in details]
            branch_number = len(branch_names)
            repo_branch_details = {
                'branch_names': branch_names,
                'branch_number': branch_number
            }
            return repo_branch_details
        else:
            return {'error': 'Unable to fetch repository information'}
       


    def get_github_collaborator_info(self, data):
       
        owner = data['owner']
        repo = data['repo']


        url = f'https://api.github.com/repos/{owner}/{repo}/collaborators'
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }


        response = pip._vendor.requests.get(url, headers=headers)
        if response.status_code == 200 :
            details = response.json()
            collaborator_names = [collaborator['login'] for collaborator in details]
            collaborator_number = len(collaborator_names)
            collaborator_details = {
                'collaborators': collaborator_names,
                'collaborator_number': collaborator_number
            }


            return collaborator_details
        else:
            return {'error': 'Unable to fetch repository information'}