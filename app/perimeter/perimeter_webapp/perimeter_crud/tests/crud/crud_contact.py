from django.test import TestCase
# Create your tests here.
from perimeter.perimeter_core.models.contacts import Contact
from perimeter.perimeter_core.controllers import contacts

class ContactCRUDTestCase(TestCase):

    contact = None

    def setUp(self):
        global contact

        try:
            parameters = {
                'title': 'Mr.',
                'alias': 'neet_lord',
                'first_name': 'Lusayo',
                'last_name': 'Nyondo',
                'middle_name': 'Henderson',
                'job_post': 'I.T Technician',
            }
            
            contact = contacts.create(parameters)
        except:
            pass

        self.assertIsNotNone(contact)

    def test_modify_contact(self):
        global contact
        response = None
        
        try:
            parameters = {
                'id': contact.id,
                'title': 'Mr.',
                'alias': 'neet_lord',
                'first_name': 'Lusayo',
                'last_name': 'NeetLord',
                'middle_name': 'Henderson',
                'job_post': 'I.T Technician',
            }

            response = contacts.modify(parameters)

        except:
            pass

        self.assertIsNotNone(response)

    def test_add_contact_phone_numbers(self):
        global contact
        response = None

        try:
            parameters = {
                'contact': contact,
                'phone_number': '+265997578523',
            }

            response = contacts.add_contact_phone_number(parameters)

        except:
            pass

        self.assertIsNotNone(response)

    def test_edit_contact_phone_numbers(self):
        pass

    def test_remove_contact_phone_numbers(self):
        pass

    def test_add_contact_emails(self):
        global contact
        response = None

        try:
            parameters = {
                'contact': contact,
                'email_address': '+265997578523',
            }

            response = contacts.add_contact_email_address(parameters)

        except:
            pass

        self.assertIsNotNone(response)

    def test_edit_contact_emails(self):
        pass

    def test_remove_contact_emails(self):
        pass

    def test_get_contact(self):
        global contact
        response = None

        try:
            parameters = {
                'id': contact.id,
            }

            response = contacts.get(parameters)

        except:
            pass

        self.assertIsNotNone(response)

    def test_remove_contact(self):
        global contact
        response = None
        deleted_contact = None

        try:
            parameters = {
                'id': contact.id,
            }
            
            deleted_contact, response = contacts.delete(parameters)
        except:
            pass

        self.assertIsNotNone(response)
        self.assertIsNotNone(deleted_contact)