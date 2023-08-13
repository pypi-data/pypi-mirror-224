from aiohttp import ClientResponse, ClientSession
from utils import encode_base64


class Awakatime:
    """Wakatime API client.

    Attributes:
        base_url (str): Base URL for the API.
        api_key (str): Encoded API key.
        session (aiohttp.ClientSession): HTTP session.
    """

    base_url = "https://wakatime.com"

    def __init__(self, api_key: str):
        """Initialize a new Wakatime client.

        Transform the API key into a base64 encoded string.

        Args:
            api_key (str): API key to use.
        """
        self.api_key = encode_base64(api_key)
        self.session = ClientSession(self.base_url)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        await self.close()

    async def request(self, method: str, endpoint: str, **kwargs) -> ClientResponse:
        """Make a request to the WakaTime API.

        This method is a coroutine.

        Args:
            method (str): HTTP method to use.
            endpoint (str): API endpoint to use.
            **kwargs: Additional arguments to pass to the request.

        Returns:
            aiohttp.ClientResponse: Response from the API.

        Raises:
            aiohttp.ClientResponseError: If the response status code is not 2xx.
        """
        headers = {
            "Authorization": f"Basic {self.api_key}",
            "Content-Type": "application/json",
        }
        return await self.session.request(
            method,
            endpoint,
            headers=headers,
            raise_for_status=True,
            **kwargs,
        )

    async def get_all_time(self, project_name: str | None = None) -> dict:
        """Get all time logged for the user.

        This method is a coroutine.

        Args:
            project_name (str, optional): Project name to filter by.

        Returns:
            dict: All time logged for the user.

        Raises:
            KeyError: If the response data is missing the "data" key.
            aiohttp.ClientResponseError: If the response status code is not 2xx.
        """
        endpoint = "/api/v1/users/current/all_time_since_today"
        params = {"project": project_name} if project_name else {}

        response = await self.request("GET", endpoint, params=params)
        response_data = await response.json()
        return response_data["data"]

    async def get_projects(self) -> list[dict]:
        """Get all projects for the current user.

        This method is a coroutine.

        Returns:
            list[dict]: List of projects.

        Raises:
            KeyError: If the response data is missing the "data" key.
            aiohttp.ClientResponseError: If the response status code is not 2xx.
        """
        endpoint = "/api/v1/users/current/projects"

        response = await self.request("GET", endpoint)
        response_data = await response.json()
        return response_data["data"]

    async def close(self):
        await self.session.close()
