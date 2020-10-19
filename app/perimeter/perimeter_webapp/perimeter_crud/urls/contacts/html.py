from django.urls import path, include
from perimeter.perimeter_webapp.perimeter_crud.views.contacts import html as contacts

urlpatterns = [
    path('contacts/', contacts.index),
    path('contacts/create', contacts.create),
    path('contacts/<int:contact_id>/edit', contacts.edit),
    path('contacts/index', contacts.index),
    path('contacts/<int:contact_id>/show', contacts.show),
    path('contacts/<int:contact_id>/delete', contacts.delete),

    path('contacts/<int:contact_id>/emails/add', contacts.add_email),
    path('contacts/<int:contact_id>/emails/<int:email_id>/edit', contacts.edit_email),
    path('contacts/<int:contact_id>/emails/<int:email_id>/remove', contacts.remove_email),
    path('contacts/<int:contact_id>/emails/<int:email_id>/show', contacts.show_email),

    path('contacts/<int:contact_id>/phone_numbers/add', contacts.add_phone_number),
    path('contacts/<int:contact_id>/phone_numbers/<int:phone_number_id>/edit', contacts.edit_phone_number),
    path('contacts/<int:contact_id>/phone_numbers/<int:phone_number_id>/remove', contacts.remove_phone_number),
    path('contacts/<int:contact_id>/phone_numbers/<int:phone_number_id>/show', contacts.show_phone_number),
]