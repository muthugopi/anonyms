from django.shortcuts import redirect

class VerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:

            allowed_paths = [
                '/auth/pending/',
                '/auth/logout/',
                '/admin/'
            ]

            if (
                request.user.is_verified != 'verified'
                and request.path not in allowed_paths
            ):
                return redirect('/auth/pending/')

        response = self.get_response(request)
        return response