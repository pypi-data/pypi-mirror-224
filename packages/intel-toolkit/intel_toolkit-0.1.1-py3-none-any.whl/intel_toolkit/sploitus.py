import re
import httpx
from rich import print
from functools import cache

class consult:
    def __init__(self):
        self.requests = httpx.Client(follow_redirects=True, http2=True, default_encoding='utf-8')
        self.url_api_sploitus = 'https://sploitus.com/search'
        self.body_search = {
                "type": "exploits", 
                "sort": "default",
                "query": "",
                "title": True,
                "offset": 0
            }
        self.headers = {
            "authority": "sploitus.com",
            "accept": "application/json",
            "Accept-Encoding": "deflate, gzip, br, zstd",
            "content-type": "application/json",
            "referer": "https://sploitus.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        
    def __check_cve_string(self, cve):
        check = re.search('CVE-\d{4}-\d{4,7}', cve)
        if check == None:
            return False
        else:
            return True
    
    @cache
    def get_vuln_id_info(self, vulnid, type):
        model_body = self.body_search
        model_headers = self.headers
        vulnid = vulnid.upper()
        if self.__check_cve_string(vulnid):
            model_body['query'] = vulnid
            model_body['type'] = type
            model_headers['referer'] = f"{model_headers['referer']}/?query={vulnid}"
        else:
            msg = {
                "error": 'CVE Model Error',
                "received": vulnid,
                "model_example": 'CVE-2000-0000000',
                "match_regex": 'CVE-\d{4}-\d{4,7}'
            }
            print(msg)
            exit(1)
        try:
            r = self.requests.post(url=self.url_api_sploitus, json=model_body, headers=model_headers)
            return r.json()
        except:
            return {'error': 'Error API Sploitus'}
        
    def check_vuln_has_exploit(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid, 'exploits')
        if vulnid_data.get('exploits_total') > 0:
            return True
        else:
            return False
    
    def get_vuln_exploits(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid, 'exploits')
        return vulnid_data.get('exploits')
    
    def get_vuln_total_exploits(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid, 'exploits')
        return vulnid_data.get('exploits_total')
    
    def check_vuln_has_tool(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid, 'tools')
        if vulnid_data.get('exploits_total') > 0:
            return True
        else:
            return False
    
    def get_vuln_tools(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid, 'tools')
        return vulnid_data.get('exploits')
    
    def get_vuln_total_tools(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid, 'tools')
        return vulnid_data.get('exploits_total')

if __name__ == "__main__":
    c = consult()
    vuln = 'CVE-2022-22965'
    d_vuln = c.get_vuln_total_tools(vuln)
    print(d_vuln)
    # console = Console()
    # for ex in d_vuln:
    #     md = Markdown(ex.get('source'))
    #     console.print(md)
    # if c.check_vuln_has_exploit(vulnid=vuln):
    #     print(c.get_vuln_total_exploits(vulnid=vuln))