"""Arquivo de instancia para http_error402"""


class HttpUnprocessableEntity(Exception):
    """HttpError 402 - Unprocessable Entity!"""

    def __init__(self, message: str = " Unprocessable Entity!") -> None:
        super().__init__(message)
        self.message = message
        self.name = " UnprocessableEntity!Error"
        self.status_code = 402
