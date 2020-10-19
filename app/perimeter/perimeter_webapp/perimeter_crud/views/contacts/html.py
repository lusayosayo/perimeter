from django.shortcuts import loader, redirect
from django.http import HttpResponse

from perimeter.perimeter_core.models.contacts import Contact, ContactPhoneNumber, ContactEmail

from perimeter.perimeter_core.controllers import contacts

def index(request):
    template = loader.get_template('perimeter_crud/module_blocks/contacts/index.dtl.html')

    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }

    return HttpResponse(template.render(context, request))

def create(request):
    if request.POST.get('first_name'):
        alias = request.POST.get('alias')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        title = request.POST.get('title')
        job_post = request.POST.get('job_post')
        middle_name = request.POST.get('middle_name')

        parameters = {
            'alias': alias,
            'first_name': first_name,
            'last_name': last_name,
            'title': title,
            'middle_name': middle_name,
            'job_post': job_post,
        }

        contact = contacts.create(**parameters)

        redirect_url = '/perimeter/contacts/{}/show'.format(
            contact.id,
        )

        return redirect(redirect_url)

    else:
        template = loader.get_template('perimeter_crud/module_blocks/contacts/create.dtl.html')
        
        context = {}

        return HttpResponse(template.render(context, request))

def edit(request, contact_id):
    if request.POST.get('first_name'):
        title = request.POST.get('title')
        alias = request.POST.get('alias')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        job_post = request.POST.get('job_post')

        parameters = {
            'id': contact_id,
            'title': title,
            'alias': alias,
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'job_post': job_post,
        }

        contact = contacts.modify(**parameters)

        return redirect('/perimeter/contacts/{0}/show'.format(contact_id))
    else:
        template = loader.get_template('perimeter_crud/module_blocks/contacts/edit.dtl.html')

        contact = Contact.objects.get(
            id=contact_id,
        )

        phone_numbers = ContactPhoneNumber.objects.filter(
            contact=contact,
        )

        emails = ContactEmail.objects.filter(
            contact=contact,
        )

        context = {
            'contact': contact,
            'phone_numbers': phone_numbers,
            'emails': emails,
        }

        return HttpResponse(template.render(context, request))

def show(request, contact_id):
    template = loader.get_template('perimeter_crud/module_blocks/contacts/show.dtl.html')

    contact = Contact.objects.get(
        id=contact_id,
    )

    phone_numbers = ContactPhoneNumber.objects.filter(
        contact=contact,
    )

    emails = ContactEmail.objects.filter(
        contact=contact,
    )

    context = {
        'contact': contact,
        'phone_numbers': phone_numbers,
        'emails': emails,
    }

    return HttpResponse(template.render(context, request))

def delete(request, contact_id):
    contact = contacts.delete(id=contact_id)
    return redirect('/perimeter/contacts/index')

def add_email(request, contact_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    if request.POST.get('email_address'):
        email_address = request.POST.get('email_address')

        parameters = {
            'contact': contact,
            'email_address': email_address,
        }

        email = contacts.add_contact_email_address(**parameters)
        
        return redirect('/perimeter/contacts/{0}/show'.format(contact_id))
    else:
        template = loader.get_template('perimeter_crud/module_blocks/contacts/emails/add.dtl.html')
        
        context = {
            'contact': contact,
        }

        return HttpResponse(template.render(context, request))

def edit_email(request, contact_id, email_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    email = ContactEmail.objects.get(
        id=email_id,
    )

    if request.POST.get('email_address'):
        email_address = request.POST.get('email_address')

        parameters = {
            'id': email_id,
            'contact': contact,
            'email_address': email_address,
        }

        email = contacts.modify_contact_email_address(**parameters)
        
        return redirect('/perimeter/contacts/{0}/show'.format(contact_id))
    else:
        template = loader.get_template('perimeter_crud/module_blocks/contacts/emails/edit.dtl.html')
        
        context = {
            'contact': contact,
            'email': email,
        }

        return HttpResponse(template.render(context, request))

def remove_email(request, contact_id, email_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    email_address = ContactEmail.objects.get(
        id=email_id,
    )

    contact_email = contacts.remove_contact_email_address(
        id=email_id,
    )

    return redirect('/perimeter/contacts/{0}/show'.format(contact_id))

def show_email(request, contact_id, email_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    email_address = ContactEmail.objects.get(
        id=email_id,
    )

    template = loader.get_template('/perimeter_crud/module_blocks/contacts/emails/show.dtl.html')

    context = {
        'contact': contact,
        'email': email_address,
    }

    return HttpResponse(template.render(context, request))
    
def add_phone_number(request, contact_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    if request.POST.get('phone_number'):
        phone_number = request.POST.get('phone_number')

        parameters = {
            'contact': contact,
            'phone_number': phone_number,
        }

        phone_number = contacts.add_contact_phone_number(**parameters)
        
        return redirect('/perimeter/contacts/{0}/show'.format(contact_id))
    else:
        template = loader.get_template('perimeter_crud/module_blocks/contacts/phone_numbers/add.dtl.html')
        
        context = {
            'contact': contact,
        }

        return HttpResponse(template.render(context, request))

def edit_phone_number(request, contact_id, phone_number_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    phone_number = ContactPhoneNumber.objects.get(
        id=phone_number_id,
    )

    if request.POST.get('phone_number'):
        phone_number = request.POST.get('phone_number')

        parameters = {
            'id': phone_number_id,
            'contact': contact,
            'phone_number': phone_number,
        }

        phone_number = contacts.modify_contact_phone_number(**parameters)
        
        return redirect('/perimeter/contacts/{0}/show'.format(contact_id))
    else:
        template = loader.get_template('perimeter_crud/module_blocks/contacts/phone_numbers/edit.dtl.html')
        
        context = {
            'contact': contact,
            'phone_number': phone_number,
        }

        return HttpResponse(template.render(context, request))

def remove_phone_number(request, contact_id, phone_number_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    phone_number = ContactPhoneNumber.objects.get(
        id=phone_number_id,
    )

    contact_phone_number = contacts.remove_contact_phone_number(
        id=phone_number_id,
    )

    return redirect('/perimeter/contacts/{0}/show'.format(contact_id))

def show_phone_number(request, contact_id, phone_number_id):
    contact = Contact.objects.get(
        id=contact_id,
    )

    phone_number = ContactPhoneNumber.objects.get(
        id=phone_number_id,
    )

    template = loader.get_template('/perimeter_crud/module_blocks/contacts/phone_numbers/show.dtl.html')

    context = {
        'contact': contact,
        'phone_number': phone_number,
    }

    return HttpResponse(template.render(context, request))