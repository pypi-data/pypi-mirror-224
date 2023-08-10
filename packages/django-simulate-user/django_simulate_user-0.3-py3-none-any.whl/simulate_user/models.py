from datetime import timedelta, datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.utils import timezone
from .app_settings import app_settings


UserModel = get_user_model()


class SimulatedUserSession(models.Model):
    """
    Model representing a simulated user session.

    Attributes:
        - real_user: The actual user initiating the simulation.
        - simulated_user: The user being simulated. Can be None, representing an anonymous user.
        - real_session_key: Session key of the real user.
        - simulated_session_key: Session key of the simulated user.
        - created_at: Timestamp when the simulation session was created.
        - closed_at: Timestamp when the simulation session was closed or expired.
        - hide_bar: Flag to determine if the control bar should be hidden during the simulation.
    """

    # Fields
    real_user: UserModel = models.ForeignKey(UserModel, related_name="real_user_sessions", on_delete=models.CASCADE)
    simulated_user: UserModel | None = models.ForeignKey(
        UserModel, related_name="simulated_user_sessions", null=True, blank=True, on_delete=models.SET_NULL
    )
    real_session_key: str = models.CharField(max_length=40)
    simulated_session_key: str = models.CharField(max_length=40, unique=True)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    closed_at: datetime | None = models.DateTimeField(null=True, blank=True)
    hide_bar: bool = models.BooleanField(default=False)

    def get_simulated_user(self) -> models.ForeignKey | AnonymousUser:
        """
        Returns the simulated user. If no user is being simulated, returns an AnonymousUser instance.

        Returns:
            (models.ForeignKey | AnonymousUser): The user being simulated or an anonymous user.
        """
        if self.simulated_user:
            return self.simulated_user
        return AnonymousUser()

    @property
    def simulated_user_or_anonymous(self) -> models.ForeignKey | AnonymousUser:
        """
        Property returning the simulated user or an anonymous user.

        Returns:
            (models.ForeignKey | AnonymousUser): The user being simulated or an anonymous user.
        """
        return self.get_simulated_user()

    def save(self, *args, **kwargs) -> None:
        """
        Override the save method to:
            - Close any open simulation sessions of the same user.
            - Expire sessions that exceed the simulated session expiry time.
            - Delete sessions that exceed the simulated session retention period.

        Args:
            *args, **kwargs: Arguments passed to the base save method.
        """
        SimulatedUserSession.objects.filter(
            real_user=self.real_user, closed_at__isnull=True
        ).update(closed_at=timezone.now())

        cutoff_expiration: datetime = timezone.now() - timedelta(seconds=app_settings.SIMULATED_SESSION_EXPIRY)
        SimulatedUserSession.objects.filter(
            created_at__lt=cutoff_expiration, closed_at__isnull=True
        ).update(closed_at=timezone.now())

        cutoff_date: datetime = timezone.now() - timedelta(days=app_settings.SIMULATED_SESSION_RETENTION)
        SimulatedUserSession.objects.filter(created_at__lt=cutoff_date).delete()

        super(SimulatedUserSession, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        String representation of the model.

        Returns:
            (str): A string representation showing who is simulating as whom and when it was created.
        """
        return f"Session by {self.real_user} as {self.simulated_user} created at {self.created_at}"


class SimulatedUserAction(models.Model):
    """
    Model representing an action performed during a simulated user session.

    Attributes:
        - simulated_user_session: The SimulatedUserSession in which the action was performed.
        - action: Text description of the action performed.
        - timestamp: Timestamp when the action was performed.
    """

    # Fields
    simulated_user_session: SimulatedUserSession = models.ForeignKey(
        SimulatedUserSession, related_name='simulated_session_actions', on_delete=models.CASCADE
    )
    action: str = models.TextField()
    timestamp: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        String representation of the model.

        Returns:
            (str): A string representation showing who performed what action and when.
        """
        return f"Action by {self.simulated_user_session.real_user} as {self.simulated_user_session.simulated_user} on" \
               f" {self.timestamp}"
