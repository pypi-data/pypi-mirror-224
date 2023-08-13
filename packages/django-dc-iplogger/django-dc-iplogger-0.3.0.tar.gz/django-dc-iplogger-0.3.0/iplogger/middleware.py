from iplogger.models import UserIP

class IPLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        
        if ip_address:
            UserIP.objects.create(user=request.user, ip_address=ip_address)
        
        return response
