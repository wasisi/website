from django.apps import AppConfig


class AccountappConfig(AppConfig):
    name = 'accountApp'
    index_page_name = 'Login Wasisi'
    account_page_name = 'Test Account'

    #the templates used
    login_view_tmpl   = 'account/login.html'
    profile_view_tmpl = 'account/profile_view.html'
