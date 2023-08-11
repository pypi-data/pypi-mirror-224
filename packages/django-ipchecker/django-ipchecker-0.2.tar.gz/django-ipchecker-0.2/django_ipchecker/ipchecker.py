# myapp/middleware.py
from django.http import HttpResponseForbidden

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = ['192.168.1.1', '10.0.0.2']  # List of IP addresses to block

    def __call__(self, request):
        # Get the client's IP address
        client_ip = request.META.get('REMOTE_ADDR')

        # Check if the IP address is in the blocked_ips list
        if client_ip in self.blocked_ips:
            return HttpResponseForbidden("Access denied")

        response = self.get_response(request)
        return response
