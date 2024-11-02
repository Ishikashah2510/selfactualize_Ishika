import unittest
from app import app, db, MessageLog
from flask import json


class MessageAPITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the application for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB for testing
        # with app.app_context():
        #     db.create_all()  # Create tables

    # @classmethod
    # def tearDownClass(cls):
    #     # Teardown database after tests
    #     with app.app_context():
    #         db.drop_all()

    def setUp(self):
        # Set up the test client
        self.client = app.test_client()

    def test_unsupported_message_type(self):
        # Test sending a message with an unsupported type
        payload = {
            "type": "unsupported_type",
            "recipient": "user@example.com",
            "content": "This should fail due to unsupported type."
        }
        response = self.client.post('/sendMessage',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        # Check if the response indicates failure
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'failure')
        self.assertEqual(data['message'], 'Unsupported message type: unsupported_type')

    def test_email_failure(self):
        # Test sending a message with an invalid email
        payload = {
            "type": "email",
            "recipient": "not a email",
            "content": "This email should fail to send."
        }
        response = self.client.post('/sendMessage',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        # Check if the response indicates failure
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'failure')
        self.assertIn("Recipient is not a", data['message'])

    def test_sms_failure(self):
        # Test sending a message with an invalid phone number
        payload = {
            "type": "sms",
            "recipient": "not a number",
            "content": "This SMS should fail to send."
        }
        response = self.client.post('/sendMessage',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        # Check if the response indicates failure
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'failure')
        self.assertIn("Recipient is not a", data['message'])

    def test_whatsapp_failure(self):
        # Test sending a whatsapp message with an invalid phone number
        payload = {
            "type": "whatsapp",
            "recipient": "not a number",
            "content": "This WhatsApp message should fail to send."
        }
        response = self.client.post('/sendMessage',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        # Check if the response indicates failure
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'failure')
        self.assertIn("Recipient is not a", data['message'])

    def test_missing_recipient(self):
        # Test with missing recipient field
        payload = {
            "type": "email",
            "content": "This message is missing the recipient field."
        }
        response = self.client.post('/sendMessage',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        # Check if the response indicates failure due to missing recipient
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'failure')
        self.assertIn("Missing fields", data['message'])

    def test_missing_content(self):
        # Test with missing content field
        payload = {
            "type": "sms",
            "recipient": "+1234567890"
        }
        response = self.client.post('/sendMessage',
                                    data=json.dumps(payload),
                                    content_type='application/json')

        # Check if the response indicates failure due to missing content
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'failure')
        self.assertIn("Missing fields", data['message'])


if __name__ == '__main__':
    unittest.main()
