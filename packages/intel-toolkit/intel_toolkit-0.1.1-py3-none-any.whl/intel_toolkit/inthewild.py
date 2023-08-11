import httpx as requests
from rich import print
from functools import cache

class consult:
    def __init__(self):
        self.url_exploitations_feed = 'https://inthewild.io/_next/data/UMG9URuOvdt1CxoJXmUax/feed.json'
        self.url_exploits_feed = 'https://inthewild.io/api/exploits?limit=1000'
        self.url_exploitation_get_vuln_id = 'https://inthewild.io/api/exploitations' # ?query=CVE-2022-22965
        self.url_exploit_get_vuln_id = 'https://inthewild.io/api/exploits' # ?query=CVE-2022-22965

    @cache
    def exploitations_feed(self):
        try:
            r = requests.get(url=self.url_exploitations_feed)
            return r.json()
        except:
            return {'error': 'Error API InTheWild'}
    
    @cache
    def exploits_feed(self):
        try:
            r = requests.get(url=self.url_exploits_feed)
            return r.json()
        except:
            return {'error': 'Error API InTheWild'}
    
    @cache
    def get_exploitation_vuln_id(self, vulnid):

        params = {
            "query": vulnid
        }

        try:
            r = requests.get(url=self.url_exploitation_get_vuln_id, params=params)
            return r.json()
        except:
            return {'error': 'Error API InTheWild'}
    
    @cache
    def get_exploit_vuln_id(self, vulnid):

        params = {
            "query": vulnid
        }

        try:
            r = requests.get(url=self.url_exploit_get_vuln_id, params=params)
            return r.json()
        except:
            return {'error': 'Error API InTheWild'}
        
if __name__ == "__main__":
    c = consult()
    print(c.get_exploit_vuln_id('CVE-2022-22965'))