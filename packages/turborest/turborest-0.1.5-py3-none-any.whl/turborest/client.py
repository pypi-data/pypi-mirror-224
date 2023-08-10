import urllib.parse
import urllib.request
import json
import base64

from .__main__ import Application
from .logger import HTTPLogger

class Client:
    def __init__(self, format: str = None, auth: tuple = None, proxy: str = None, logger: HTTPLogger = None) -> None:
        """
        Create a pyResty client
        """
        self.headers = {}
        self.format = self.__format(format)
        self.set_content_type(format)
        self.set_accept(format)
        self.set_agent(f"{Application.name}/{Application.version}")
        self.logger = None
        if logger:
            self.logger = logger

    def __format(self, value: str) -> str:
        """
        Format the value to the set format
        """
        if value is None:
            return None
        match value:
            case "json":
                return "application/json"
            case "xml":
                return "application/xml"
            case "yaml":
                return "application/yaml"
            case "text":
                return "text/plain"
            case "html":
                return "text/html"
            case _:
                raise Exception("Invalid format!")

    def set_content_type(self, format: str) -> None:
        """
        Set the content type of the request ["Content-Type"]
        """
        if format is not None:
            self.content_type = self.__format(format)
            self.headers["Content-Type"] = self.content_type
        else:
            self.content_type = "application/json"
            self.headers["Content-Type"] = self.content_type
    
    def set_accept(self, format: str) -> None:
        """
        Set the accept type of the request ["Accept"]
        """
        if format is not None:
            self.accept = self.__format(format)
            self.headers["Accept"] = self.accept

    def set_agent(self, agent: str) -> None:
        """
        Set the user agent of the request ["User-Agent"]
        """
        self.agent = agent
        self.headers["User-Agent"] = agent

    def set_auth(self, auth: tuple, type: str = "basic") -> None:
        """
        Set the authentication of the request
        """
        match type:
            case "basic":
                __auth = base64.b64encode(f"{auth[0]}:{auth[1]}".encode("utf-8"))
                self.auth = f"Basic {__auth.decode('utf-8')}"
                self.headers["Authorization"] = self.auth
            case "bearer":
                self.auth = f"Bearer {auth}"
                self.headers["Authorization"] = self.auth
            case "api-key":
                self.auth = auth[0]
                self.headers["X-API-Key"] = self.auth
            case _:
                self.auth = f"{type} {auth[0]}"
                self.headers["Authorization"] = self.auth

    def __send(self, method: str, url: str, data: dict = None, query: dict = None) -> urllib.request.Request:
        """
        Send the request
        """
        if query:
            url = f"{url}?{urllib.parse.urlencode(query)}"
        request = urllib.request.Request(url, method=method, headers=self.headers)
        if data:
            request.data = json.dumps(data).encode("utf-8")
        # If self.accept is html or text, then return the response as a string
        # Else, return the response as a dict
        res = urllib.request.urlopen(request)
        response_code = res.getcode()
        if self.logger:
            self.logger.handler.info(f"[{response_code}] {method} {url}")
        return res
    
    def html(self, response: urllib.request.Request) -> str:
        """
        Get the html response
        """
        return response.read().decode("utf-8")

    def text(self, response: urllib.request.Request) -> str:
        """
        Get the text response
        """
        return response.read().decode("utf-8")

    def json(self, response: urllib.request.Request) -> dict:
        """
        Get the json response
        """
        return json.loads(response.read().decode("utf-8"))
    
    def get(self, url: str, query: dict = None) -> dict:
        """
        Send a get request
        """
        res = self.__send("GET", url, query=query)
        return res
    
    def post(self, url: str, data: dict = None, query: dict = None) -> dict:
        """
        Send a post request
        """
        res = self.__send("POST", url, data=data, query=query)
        return res
    
    def put(self, url: str, data: dict = None, query: dict = None) -> dict:
        """
        Send a put request
        """
        res = self.__send("PUT", url, data=data, query=query)
        return res
    
    def delete(self, url: str, query: dict = None) -> dict:
        """
        Send a delete request
        """
        res = self.__send("DELETE", url, query=query)
        return res
    
    def head(self, url: str, query: dict = None) -> dict:
        """
        Send a head request
        """
        res = self.__send("HEAD", url, query=query)
        return res
    
    def options(self, url: str, query: dict = None) -> dict:
        """
        Send a options request
        """
        res = self.__send("OPTIONS", url, query=query)
        return res
    
    def patch(self, url: str, data: dict = None, query: dict = None) -> dict:
        """
        Send a patch request
        """
        res = self.__send("PATCH", url, data=data, query=query)
        return res