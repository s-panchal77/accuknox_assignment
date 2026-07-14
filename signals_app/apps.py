from django.apps import AppConfig


class SignalsAppConfig(AppConfig):
    name = 'signals_app'

    def ready(self):
        # Import signals here so the receiver gets registered when Django starts.
        # If we skip this, the signal never fires — no error, just silence.
        import signals_app.signals  # noqa: F401
