def get_authenticated_user(request):
    try:
        authenticated_user = request.user
        return authenticated_user
    except Exception as exception:
        raise exception