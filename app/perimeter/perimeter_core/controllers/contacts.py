from perimeter.perimeter_core.models.contacts import Contact, ContactPhoneNumber, ContactEmail

def create(
    title=None,
    alias=None,
    first_name=None,
    last_name=None,
    middle_name=None,
    job_post=None
):
    contact = Contact.objects.get_or_create(
        title=title,
        alias=alias,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        job_post=job_post,
    )[0]

    return contact

def modify(
    id,
    title=None,
    alias=None,
    first_name=None,
    last_name=None,
    middle_name=None,
    job_post=None
):
    contact = Contact.objects.get(
        id=id,
    )

    changes_count = 0    
    
    contact.title = title if title is not None else contact.title
    contact.alias = alias if alias is not None else contact.alias
    contact.first_name = first_name if first_name is not None else contact.first_name
    contact.last_name = last_name if last_name is not None else contact.last_name
    contact.middle_name = middle_name if middle_name is not None else contact.middle_name
    contact.job_post = job_post if job_post is not None else contact.job_post

    contact.save()

    return contact

def delete(id):
    contact = Contact.objects.get(
        id=id,
    )

    response = contact.delete()

    return contact, response

def get(id):
    contact = Contact.objects.get(
        id=id,
    )

    return contact

def add_contact_phone_number(contact, phone_number):
    assert isinstance(contact, Contact)

    contact_phone_number = ContactPhoneNumber.objects.create(
        contact=contact,
        phone_number=phone_number,
    )

    return contact_phone_number

def remove_contact_phone_number(id):
    contact_phone_number = ContactPhoneNumber.objects.get(
        id=id,
    )

    contact_phone_number.delete()

    return contact_phone_number

def modify_contact_phone_number(
    id,
    contact=None,
    phone_number=None,
):
    assert isinstance(contact, Contact)

    phone_number_model = ContactPhoneNumber.objects.get(
        id=id,
    )

    phone_number_model.contact = contact if contact is not None else phone_number_model.contact
    phone_number_model.phone_number = phone_number if phone_number is not None else phone_number_model.phone_number

    phone_number_model.save()

    return phone_number_model


def get_contact_phone_numbers(contact):
    assert isinstance(contact, Contact)

    contact_phone_numbers = ContactPhoneNumber.objects.filter(
        contact=contact,
    )

    return contact_phone_numbers

def add_contact_email_address(contact, email_address):
    assert isinstance(contact, Contact)
    contact_email = ContactEmail.objects.create(
        contact=contact,
        email_address=email_address,
    )

    return contact_email

def remove_contact_email_address(id):
    contact_email = ContactEmail.objects.get(
        id=id,
    )

    contact_email.delete()

    return contact_email

def modify_contact_email_address(
    id,
    contact=None,
    email_address=None,
):
    assert isinstance(contact, Contact)

    email = ContactEmail.objects.get(
        id=id,
    )

    email.contact = contact if contact is not None else email.contact
    email.email_address = email_address if email_address is not None else email.email_address

    email.save()

    return email

def get_contact_email_addresses(contact):
    assert isinstance(contact, Contact)

    contact_email_addresses = ContactEmail.objects.filter(
        contact=contact,
    )

    return contact_email_addresses
