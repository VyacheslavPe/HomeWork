from sqlalchemy import text
from sql_requests import requests

db_connection_link = 'postgresql://postgres:SkyPro@localhost:5432/QA'

request = requests(db_connection_link)

sql_insert = text("INSERT INTO users (user_id, user_email, subject_id) VALUES(12345, \'test@mail.com\', 12345);")
sql_select = text('SELECT * FROM users WHERE user_email = \'test@mail.com\'')
sql_select2 = text('SELECT * FROM users WHERE user_email = \'test2@mail.com\'')
sql_delete = text('DELETE FROM users WHERE user_email = \'test@mail.com\'')
sql_delete2 = text('DELETE FROM users WHERE user_email = \'test2@mail.com\'')
sql_update = text('UPDATE users SET user_email = \'test2@mail.com\' WHERE user_email=\'test@mail.com\'')

def test_insert():
    request.edit(sql_insert)
    rows = request.select(sql_select).mappings().all()
    assert rows[0]['user_id'] == 12345
    assert rows[0]['user_email'] == 'test@mail.com'
    assert rows[0]['subject_id'] == 12345
    request.edit(sql_delete)

def test_update():
    request.edit(sql_insert)
    request.edit(sql_update)
    rows = request.select(sql_select2).mappings().all()
    assert rows[0]['user_id'] == 12345
    assert rows[0]['user_email'] == 'test2@mail.com'
    assert rows[0]['subject_id'] == 12345
    request.edit(sql_delete2)

def test_delete():
    request.edit(sql_insert)
    request.edit(sql_delete)
    rows = request.select(sql_select).mappings().all()
    assert len(rows) == 0

