import logging
import time

logger = logging.getLogger("bookstore.requests")


class RequestTimingMiddleware:
    """
    Measure request processing time and write it to the log.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()

        response = self.get_response(request)

        duration_ms = (time.perf_counter() - start_time) * 1000

        response["X-Response-Time-ms"] = f"{duration_ms:.2f}"

        # Avoid logging static files and Debug Toolbar requests.
        if not request.path.startswith(("/static/", "/__debug__/")):
            logger.info(
                "%s %s | status=%s | duration=%.2f ms",
                request.method,
                request.path,
                response.status_code,
                duration_ms,
            )

        return response
