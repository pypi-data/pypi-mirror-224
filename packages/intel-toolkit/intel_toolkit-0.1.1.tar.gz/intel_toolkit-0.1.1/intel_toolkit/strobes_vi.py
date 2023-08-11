import re
import httpx as requests
from rich import print
from functools import cache

class consult:
    def __init__(self):
        self.url_api_strobes = 'https://intel.strobes.co/api/vulnerabilities'

    def check_cve_string(self, cve):
        check = re.search('CVE-\d{4}-\d{4,7}', cve)
        if check == None:
            return False
        else:
            return True
    
    @cache
    def get_vuln_id_info(self, vulnid):
        vulnid = vulnid.upper()
        if self.check_cve_string(vulnid):
            url = f'{self.url_api_strobes}/{vulnid}'
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
            r = requests.get(url=url)
            return r.json()
        except:
            return {'error': 'Error API StribesVI'}
        
    @cache
    def check_vuln_has_patch(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid)
        return vulnid_data.get('patches').get('patch_available')

    @cache
    def get_refs_vuln_patch(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid)
        return vulnid_data.get('patches').get('references')

    @cache
    def check_vuln_is_zeroday(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid)
        return vulnid_data.get('zeroday').get('is_zeroday')
    
    @cache
    def get_refs_vuln_zeroday(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid)
        return vulnid_data.get('zeroday').get('references')

    @cache
    def check_vuln_has_exploit(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid)
        return vulnid_data.get('exploits').get('exploit_available')
    
    @cache
    def get_refs_vuln_exploits(self, vulnid):
        vulnid_data = self.get_vuln_id_info(vulnid)
        return vulnid_data.get('exploits').get('references')
        
if __name__ == "__main__":
    c = consult()
    # print(c.check_vuln_has_patch('CVE-2022-4955'))
    # print(c.get_refs_vuln_patch('CVE-2022-4955'))
    # print(c.check_cve_string('cve-2022-22965'))
    print(c.check_vuln_has_exploit('cve-2022-22965'))
    print(c.get_refs_vuln_exploits('cve-2022-22965'))