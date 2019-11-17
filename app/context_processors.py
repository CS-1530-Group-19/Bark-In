from .models import UserProfile

def add_variable_to_context(request):
    if (request.user is not None):
        authUser = UserProfile.objects.get(pk=request.user.id)
    return {
        'authUserDogs': authUser.dogs.all()
    }