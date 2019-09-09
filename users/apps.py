from django.apps import AppConfig
from __future__ import unicode_literals


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
