from fibertrace import Logger

class HTTPLogger:
    def __init__(self, path: str, app: str, json: bool = False) -> None:
        """
        Create a HTTP logger
        """
        logger = Logger(path, app, json, "turborest")
        self.handler = logger
