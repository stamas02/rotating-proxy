import requests
import logging
from bs4 import BeautifulSoup


class RotatingProxy:
    """ A generator class which acquires a list of proxy servers and
        iterates through.

        Attributes:
        -----------
        https: bool
            When true proxies only with https support will be returned. When false
            proxies only without https support will be returned.
        _proxy_list: []
            List of proxy servers where each item is in the form of: [ip, port, country, is_https]

        Methods:
        --------
        update_list:
            Update the proxy list

        Example:
        --------
        The following example infinitelly requests the given url either if it is a http or an https
        >>> import requests
        >>> from rotating_proxy.rotating_proxy import RotatingProxy
        >>>
        >>> url = "http(s)://YOURURL.COM"
        >>> rp_http = RotatingProxy(https = False)
        >>> rp_https = RotatingProxy(https = True)
        >>> while True:
        >>>     rp_http.update()
        >>>     rp_https.update()
        >>>     for proxy_http , proxy_https  in zip(rp_http, rp_https):
        >>>         proxyDict = {"http"  : "{0}:{1}".format(*proxy_http[0:2]),
        >>>                      "https"  : "{0}:{1}".format(*proxy_https[0:2])}
        >>>         r = requests.get(url, proxies=proxyDict)
        >>>         print(r.text)
    """

    __source = "https://free-proxy-list.net/"

    def __init__(self, https=True):
        self.https = https
        self._proxy_list = []
        self.update_list()
        pass

    def update_list(self):
        """ Update the proxy list

        Returns
        -------
            None
        """
        logging.info("Loading proxy list")
        html = requests.get(self.__source).text
        soup = BeautifulSoup(html)
        table = soup.find('table', id="proxylisttable")
        table_content = table.find('tbody')
        for row in table_content.findAll('tr'):
            cols = row.findAll('td')
            ip, port, _, country, _, _, https, _ = [c.contents[0] if len(c.contents) > 0 else "" for c in cols]
            is_https = https == "yes"
            if self.https != is_https:
                continue
            self._proxy_list.append([ip, port, country, is_https])

    def __iter__(self):
        """ Generate a proxy at a time

        Returns
        -------
        A list like: [ip, port, country, is_https]

        """
        for proxy in self._proxy_list:
            yield proxy
