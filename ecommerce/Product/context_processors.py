def user_profile(request):
    return {'user_profile': request.user.profile if request.user.is_authenticated else None}
