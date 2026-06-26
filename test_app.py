from app import app,users
import pytest
@pytest.fixture
def c():
 app.config['TESTING']=True
 return app.test_client()
def test_signup_login(c):
 users.clear()
 c.post('/signup',data={'username':'a','password':'1','confirm':'1'})
 r=c.post('/login',data={'username':'a','password':'1'},follow_redirects=True)
 assert b'Welcome' in r.data
def test_404(c):
 assert c.get('/missing').status_code==404
