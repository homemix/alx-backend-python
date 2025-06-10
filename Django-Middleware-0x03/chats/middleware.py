import logging
from datetime import datetime, time

from django.http import HttpResponseForbidden


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()

        # Define allowed access window: between 6PM and 9PM
        start_time = time(18, 0)  # 6:00 PM
        end_time = time(21, 0)  # 9:00 PM

        # Restrict access if outside the window
        if not (start_time <= current_time <= end_time):
            if request.path.startswith("/api/messages/") or request.path.startswith("/api/conversations/"):
                return HttpResponseForbidden("Access to chat is only allowed between 6PM and 9PM.")

        return self.get_response(request)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logger
        self.logger = logging.getLogger("request_logger")
        handler = logging.FileHandler("requests.log")
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        self.logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        response = self.get_response(request)
        return response
