from django.apps import AppConfig


class SimulateUserConfig(AppConfig):
    """
    Configuration class for the SimulateUser application.

    Attributes:
    - default_auto_field: Specifies the type of auto-created primary key.
    - name: The full Python path of the application.
    - verbose_name: Human-readable name for the application.

    Methods:
    - ready: This method is called when the application is ready. It's used here to import signals.
    """
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'simulate_user'
    verbose_name: str = "Simulate Users"

    # noinspection PyUnresolvedReferences
    def ready(self) -> None:
        """
        Import signals when the application is ready.
        This ensures that the signal handlers are connected when the app is loaded.
        """
        from . import signals
        from . import checks
