from django.contrib import admin
from .models import SimulatedUserSession, SimulatedUserAction


class SimulatedUserSessionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SimulatedUserSession model.

    Provides:
        - List display with specific fields.
        - Search capability across specific fields.
        - Filtering based on creation and closure dates.
        - Ordering by creation date in descending order.
        - Restriction of permissions to superusers only.
    """

    # Configuration
    list_display: list[str] = [
        'id', 'real_user', 'simulated_user', 'real_session_key', 'simulated_session_key', 'created_at', 'closed_at'
    ]
    search_fields: list[str] = [
        'id', 'real_user', 'simulated_user', 'real_session_key', 'simulated_session_key', 'created_at', 'closed_at'
    ]

    list_filter: list[str] = ['created_at', 'closed_at']

    ordering: list[str] = ['-created_at']

    def has_view_permission(self, request, obj=None) -> bool:
        """Ensure only superusers can view the records."""
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None) -> bool:
        """Ensure only superusers can change the records."""
        return request.user.is_superuser

    def has_add_permission(self, request) -> bool:
        """Ensure only superusers can add new records."""
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None) -> bool:
        """Ensure only superusers can delete the records."""
        return request.user.is_superuser


class SimulatedUserActionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SimulatedUserAction model.

    Provides:
        - List display with specific fields.
        - Search capability across specific fields.
        - Filtering based on the timestamp.
        - Ordering by timestamp in descending order.
        - Restriction of permissions to superusers only.
    """

    # Configuration
    list_display: list[str] = ['simulated_user_session', 'action', 'timestamp']
    search_fields: list[str] = ['simulated_user_session', 'action']
    list_filter: list[str] = ['timestamp']
    ordering: list[str] = ['-timestamp']

    def has_view_permission(self, request, obj=None) -> bool:
        """Ensure only superusers can view the records."""
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None) -> bool:
        """Ensure only superusers can change the records."""
        return request.user.is_superuser

    def has_add_permission(self, request) -> bool:
        """Ensure only superusers can add new records."""
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None) -> bool:
        """Ensure only superusers can delete the records."""
        return request.user.is_superuser


# Registering the models with their respective admin configurations
admin.site.register(SimulatedUserSession, SimulatedUserSessionAdmin)
admin.site.register(SimulatedUserAction, SimulatedUserActionAdmin)
