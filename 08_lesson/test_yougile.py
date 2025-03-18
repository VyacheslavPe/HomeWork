import requests


base_url = 'https://ru.yougile.com'
creds = {
    'login' : '',
    'password' : ''
}
company_id = requests.post(base_url + '/api-v2/auth/companies', json=creds).json()['content'][0]['id']
creds['companyId'] = company_id
auth_key = requests.post(base_url + '/api-v2/auth/keys', json=creds).json()['key']
project = {
    'title' : 'test_project'
}
renamed_project = {
        'title': 'test_project'
}


def test_create_positive():
    resp = requests.post(base_url + '/api-v2/projects', json=project, headers={'Authorization' : 'bearer ' + auth_key})
    assert resp.status_code == 201

def test_create_negative():
    resp = requests.post(base_url + '/api-v2/projects', json=project)
    assert resp.status_code == 401

def test_rename_positive():
    id = requests.post(base_url + '/api-v2/projects', json=project, headers={'Authorization' : 'bearer ' + auth_key}).json()['id']
    resp = requests.put(base_url + '/api-v2/projects/' + id, json=renamed_project, headers={'Authorization' : 'bearer ' + auth_key})
    assert resp.status_code == 200

def test_rename_negative():
    resp = requests.put(base_url + '/api-v2/projects/', json=renamed_project, headers={'Authorization' : 'bearer ' + auth_key})
    assert resp.status_code == 404

def test_get_positive():
    id = requests.post(base_url + '/api-v2/projects', json=project, headers={'Authorization' : 'bearer ' + auth_key}).json()['id']
    resp = requests.get(base_url + '/api-v2/projects/' + id, headers={'Authorization' : 'bearer ' + auth_key})
    assert resp.status_code == 200

def test_get_negative():
    id = requests.post(base_url + '/api-v2/projects', json=project, headers={'Authorization' : 'bearer ' + auth_key}).json()['id']
    resp = requests.get(base_url + '/api-v2/projects/' + id)
    assert resp.status_code == 401