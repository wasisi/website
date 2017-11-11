from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = 'mainApp'
    index_page_name = 'Wasisi Home'

    #templates used by the application
    index_page_view_tmpl="wasisi/index.html"
