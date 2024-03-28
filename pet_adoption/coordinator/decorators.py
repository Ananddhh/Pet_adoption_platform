from django.contrib.auth.decorators import user_passes_test
from .models import Coordinator

def coordinator_required(function=None):
    """
    Decorator for views that checks whether the user is a coordinator.
    """
    def check_coordinator(user):
        if user.is_authenticated and hasattr(user, 'coordinator'):
            return True
        return False

    actual_decorator = user_passes_test(
        check_coordinator,
        login_url='/coordinator-login/'  # URL to redirect to if the user is not authenticated
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
