from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
	"""docstring for FlaskTestCase"""
	
	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		#self.assertEqual(response.status_code, 200)

    
        def test_login_page_loads(self):
    	    tester = app.test_client(self)
    	    response = tester.get('/login', content_type='html/text')
    	    self.assertFalse(b'Please login' in response.data)

     ## test login page
    	def test_correct_login(self):
    		tester = app.test_client(self)
    		response = tester.post(
    			'/api/v1/auth/login',
    			data=dict(username="admin", password="admin"),)
    		self.assertIn(b'You were just logged in!', response.data)


    	def test_correct_login(self):
    		tester = app.test_client(self)
    		response = tester.post(
    			'/login',
    			data=dict(username="wrong",  password="wrong"),
    			)
    		#self.assertIn(b'Invalid credentials. Please try again.', response.data)

        def test_register(self):
            tester =app.test_client(self)
            response = tester.get('/api/v1/auth/register', content_type='html/text')
            self.assertFalse(b'Please register' in response.data)
        
        def test_edit(self):
            tester =app.test_client(self)
            response = tester.get('/api/v1/edit', content_type='html/text')
            self.assertFalse(b'Please edit' in response.data)
        
        def test_add(self):
            tester =app.test_client(self)
            response = tester.get('/api/v1/add', content_type='html/text')
            self.assertFalse(b'Please add' in response.data)
        
        def test_order(self):
            tester =app.test_client(self)
            response = tester.get('/api/v1/order', content_type='html/text')
            self.assertFalse(b'Please order' in response.data)

        def test_welcome(self):
            tester =app.test_client(self)
            response = tester.get('/welcome', content_type='html/text')
            self.assertFalse(b'Please welcome' in response.data)

if __name__ == '__main__':
	unittest.main()
