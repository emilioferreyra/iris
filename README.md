Iris Project.
=======

This project was designed to assist in the right identification of needs for the proper channeling of resources to the members of the Asociación de Ciegos del Cibao (Dominican Republic).

Iris is a web application developed in Python and powered by Django web framework, which allows recording members information, their environment and medical history:

- Basic information (name, age, phone, address, marital status, occupation, photography).
- One or more disabilities types.
- Registers member's families living with and their relationship.
- Automatically identify mothers.
- Identify member's children quantity.

***

##List of requirements:
- [Django==1.8.13](https://www.djangoproject.com/download/)
- blessings==1.6
- bootstrap-admin==0.3.6
- [MySQL-python==1.2.5](https://pypi.python.org/pypi/MySQL-python/1.2.5) 
- [Pillow==3.0.0](https://pillow.readthedocs.org/en/3.1.x/) 
- [Pygments==2.0.2](https://github.com/odeoncg/django-pygments) 
- argparse==1.2.1
- blessings==1.6
- curtsies==0.1.23
- [django-audit-log==0.7.0](https://github.com/Atomidata/django-audit-log) 
- [django-localflavor==1.2](https://github.com/django/django-localflavor) 
- [django-model-utils==2.4](https://pypi.python.org/pypi/django-model-utils/) 
- django-smart-selects==1.2.0
- [django-suit==0.2.16](https://github.com/digi604/django-smart-selects) 
- [greenlet==0.4.9](https://greenlet.readthedocs.org/en/latest/) 
- [requests==2.9.1](https://github.com/kylef/django-request) 
- [six==1.10.0](https://github.com/django/django/blob/master/django/utils/six.py) 
- [sorl-thumbnail==12.3](https://github.com/mariocesar/sorl-thumbnail) 
- [wsgiref==0.1.2](https://pypi.python.org/pypi/wsgiref?) 


##Mains Modules:

**Employees:** This app allows employees control and department which they belongs, also their position and supervisor.

**Members:** This app allows to save member information as well as their disabilities types, family information related to and home status.

**Doctors:** This app allows record clinics history, doctors who provide medicals consultations services and the member's appointments.

**Suppliers:** This app allows to record suppliers information such as contact, address and so on.

***


##Others Modules:

**Common:** Provides commons models used in the mains apps.

**Location:** Provides models needed for entities right location (people, members, suppliers, etc.).

**People:** This app provides reusable models entities like employees, members, doctors, member's family, employee's family and supplier's contact information.

**Housing:** This app provides models that identify member's housing features, like floor type and ceiling materials.

***


##Screen shots:

**Member form:**


![Member form](https://github.com/emilioferreyra/iris/blob/dev/ScreenShots/member_form.png?raw=true)


**Member list:**


![Member list](https://github.com/emilioferreyra/iris/blob/dev/ScreenShots/member_list.png?raw=true)


**Member menu:**


![Member menu](https://github.com/emilioferreyra/iris/blob/dev/ScreenShots/member_menu.png?raw=true)
 
