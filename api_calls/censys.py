import requests

from lib.settings import start_animation
from lib.errors import AutoSploitAPIConnectionError
from lib.settings import HOST_FILE, write_to_file
import lib.output


class CensysAPIHook(object):

    """
    Censys API hook
    """

    def __init__(self, identity=None, secret=None, query=None, proxy=None, agent=None, save_mode=None, **kwargs):
        self.id = identity
        self.secret = secret
        self.query = query
        self.proxy = proxy
        self.user_agent = agent
        self.host_file = HOST_FILE
        self.save_mode = save_mode

    def search(self):
        """
        connect to the Censys API and pull all IP addresses from the provided query
        """
        discovered_censys_hosts = set()
        try:
            start_animation(
                "searching Censys with given query '{}'".format(self.query))
            req = requests.get(
                "https://search.censys.io/api/v2/hosts/search",
                params={"q": self.query},
                auth=(self.id, self.secret),
                headers=self.user_agent,
                proxies=self.proxy
            )
            lib.output.info(req)
            json_data = req.json()
            lib.output.info(json_data)
            for item in json_data["result"]["hits"]:
                discovered_censys_hosts.add(str(item["ip"]))
            write_to_file(discovered_censys_hosts,
                          self.host_file, mode=self.save_mode)
            return True
        except Exception as e:
            raise AutoSploitAPIConnectionError(str(e))
