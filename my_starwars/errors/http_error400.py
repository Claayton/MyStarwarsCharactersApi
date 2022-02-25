"""Arquivo de instancia para http_error400"""


class HttpBadRequestError(Exception):
    """HttpError 400 - Bad Request!"""

    def __init__(self, message: str = "Bad Request!") -> None:
        super().__init__(message)
        self.message = message
        self.name = "BadRequestError"
        self.status_code = 400