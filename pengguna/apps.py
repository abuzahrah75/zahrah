from django.apps import AppConfig


class PenggunaConfig(AppConfig):
    name = 'pengguna'

    def ready(self):
        import pengguna.signals