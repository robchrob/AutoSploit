import json
import requests

from lib.settings import start_animation
from lib.errors import AutoSploitAPIConnectionError
from lib.settings import (
    API_URLS,
    HOST_FILE,
    write_to_file
)
import lib.output


class ShodanAPIHook(object):

    """
    Shodan API hook, saves us from having to install another dependency
    """

    def __init__(self, token=None, query=None, proxy=None, agent=None, save_mode=None, **kwargs):
        self.token = token
        self.query = query
        self.proxy = proxy
        self.user_agent = agent
        self.host_file = HOST_FILE
        self.save_mode = save_mode

    def search(self):
        """
        connect to the API and grab all IP addresses associated with the provided query
        """
        start_animation(
            "searching Shodan with given query '{}'".format(self.query))
        discovered_shodan_hosts = set()
        try:
            req = requests.get(
                "https://api.shodan.io/shodan/host/search",
                params={"query": self.query, "key": self.token},
                proxies=self.proxy, headers=self.user_agent
            )
            lib.output.info(req)
            lib.output.info(self.token)
            json_data = json.loads(req.content)
            lib.output.info(json_data)
            for match in json_data["matches"]:
                discovered_shodan_hosts.add(match["ip_str"])
            write_to_file(discovered_shodan_hosts,
                          self.host_file, mode=self.save_mode)
            return True
        except Exception as e:
            raise AutoSploitAPIConnectionError(str(e))
