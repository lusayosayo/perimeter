from xml.etree import ElementTree as ET

from perimeter.perimeter_core.models.contacts import Contact, ContactEmail, ContactPhoneNumber

class EmailXMLFormatter():
    def __init__(
        self,
        email=None,
    ):
        self.email = email

    def load_model(self, model):
        self.email = model.email_address

    def to_model(self, contact):
        model = ContactEmail.objects.get_or_create(
            email_address=self.email,
            contact=contact,
        )[0]

        return model

    def load_xml(self, xml):
        self.email = xml.text

    def to_xml(self):
        xml = ET.Element('email')
        xml.text = self.email

        return xml

    def save_model(self, contact):
        model = self.to_model(contact=contact)
        model.save()

class PhoneNumberXMLFormatter():
    def __init__(
        self,
        phone_number=None,
    ):
        self.phone_number = phone_number

    def load_model(self, model):
        self.phone_number = model.phone_number_address

    def to_model(self, contact):
        model = ContactPhoneNumber.objects.get_or_create(
            phone_number=self.phone_number,
            contact=contact,
        )[0]

        return model

    def load_xml(self, xml):
        self.phone_number = xml.text

    def to_xml(self):
        xml = ET.Element('phone_number')
        xml.text = self.phone_number

        return xml

    def save_model(self, contact):
        model = self.to_model(contact=contact)
        model.contact = contact
        model.save()

class ContactXMLFormatter():
    def __init__(
        self,
        title=None,
        alias=None,
        first_name=None,
        last_name=None,
        middle_name=None,
        job_post=None,
    ):
        """ Accepts:
                'name': The name of the contact.
                'description': The description of the contact.
        """
        self.title = title
        self.alias = alias
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.job_post = job_post
        
        self.emails = None
        self.phone_numbers = None

    def to_model(self):
        """ Converts the NetworkXMLFormatter object to an instance of the Network model.
        """
        contact = Contact.objects.get_or_create(
            title=self.title,
            alias=self.alias,
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name,
            job_post=self.job_post
        )[0]
        
        return contact

    def load_model(self, contact):
        """ Reads from the contact model object specified and creates a corresponding object.
        """
        self.title = contact.title
        self.alias = contact.alias
        self.first_name = contact.first_name
        self.last_name = contact.last_name
        self.middle_name = contact.middle_name
        self.job_post = contact.job_post

        emails_models = contact.get_emails()

        self.emails = list()

        for email_model in self.email_models:
            email = EmailXMLFormatter(email_model)
            self.emails.append(email)

        phone_numbers_models = contact.get_phone_numbers()

        self.phone_numbers = list()

        for phone_number in phone_numbers_models:
            phone_number_xml = PhoneNumberXMLFormatter(phone_number)
            self.phone_numbers.append(phone_number_xml)

    def save_model(self, network_provider):
        model = self.to_model()
        model.save()

        from perimeter.perimeter_core.models.network_providers import NetworkProviderContactMapping

        mapping = NetworkProviderContactMapping.objects.get_or_create(
            contact=model,
            network_provider=network_provider,
        )[0]

        mapping.save()

        emails = self.emails

        for email in emails:
            email.save_model(contact=model)

        phone_numbers = self.phone_numbers
        
        for phone_number in phone_numbers:
            phone_number.save_model(contact=model)

    def to_xml(self):
        """ Converts an instance of this class to an Element object.
        """
        xml = ET.Element("contact")

        xml.attrib['title'] = self.title
        xml.attrib['alias'] = self.alias
        xml.attrib['first_name'] = self.first_name
        xml.attrib['last_name'] = self.last_name
        xml.attrib['middle_name'] = self.middle_name
        xml.attrib['job_post'] = self.job_post

        for email in self.emails:
            email_xml = email.to_xml()
            xml.append(email_xml)

        for phone_number in self.phone_numbers:
            phone_number_xml = phone_number.to_xml()
            xml.append(phone_number_xml)

        return xml

    def load_xml(self, xml):
        """ Reads from an instance of an Element object.
        """
        self.title = xml.attrib['title']
        self.alias = xml.attrib['alias']
        self.first_name = xml.attrib['first_name']
        self.last_name = xml.attrib['last_name']
        self.middle_name = xml.attrib['middle_name']
        self.job_post = xml.attrib['job_post']
        
        self.emails = list()
        emails_xmls = xml.findall('email')
        
        for email_xml in emails_xmls:
            email = EmailXMLFormatter()
            email.load_xml(email_xml)

            self.emails.append(email)

        self.phone_numbers = list()
        phone_numbers_xmls = xml.findall('phone_number')

        for phone_number_xml in phone_numbers_xmls:
            phone_number = PhoneNumberXMLFormatter()
            phone_number.load_xml(phone_number_xml)

            self.phone_numbers.append(phone_number)
