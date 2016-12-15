=====
Accounts
=====

Accounts is a django app that creates a basic layout for user accounts and logins

Quick start
-----------

1. Add "accounts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'accounts',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^accounts/', include('accounts.urls')),

3. Run `python manage.py migrate` to create the accounts models.

4. Visit http://127.0.0.1:8000/accounts/login
