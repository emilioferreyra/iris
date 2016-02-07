Iris Project.
=======

This project was designed to assist the correct identification of needs for the proper channeling of resources to the members of the Association of  Blind of Cibao of Dominican Republic.

Iris is a web application developed in Python via Django web framework, which allows recording information of the members and their environment and medical history:

- Basic information (name, age, phone, address, marital status, occupation, photography).
- The one or more types of disability.
- Registers family member living with and their relationship.
- Automatically identify mothers.
- Identifies the number of children of members.

***

##List of requirements:
- [Django==1.8.9](https://www.djangoproject.com/download/) 
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


##List of top Apps:

**Employees:** This app allows the registration of employees and the department to which it belongs, position and supervisor.

**Members:** This app lets you save the member information as well as their type of disability and information related to family and home.

**Doctors:** This app lets you record clinics and doctors who provide consultation service to members and the appointments of the members.

**Suppliers:** This app allows you to register suppliers and contacts related companies.

***


##List of auxiliary apps:

**Common:** Contains common models used in the main apps.

**Location:** Contains the models necessary for the correct location of entities (people, members, suppliers, etc.).

**People:** This app contains reusable models entities employees, members, doctor, family member and family employee contact supplier.

**Housing: **This app contains the models that identify the characteristics of housing for members.

***


##Screen shots:
