from django.contrib.auth.decorators import user_passes_test
from .models import Coordinator

def coordinator_required(function=None):
    """
    Decorator for views that checks whether the user is a coordinator.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and hasattr(u, 'coordinator'),
        login_url='/login/'  # URL to redirect to if the user is not authenticated
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
