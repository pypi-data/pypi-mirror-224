import httpx as requests
from rich import print
import re
from functools import cache
class consult:
    def __init__(self, api_key_nvd, cvss_score=0.2, epss_score=6.0, semaphore=5) -> None:
        self.nvd_key = api_key_nvd
        self.cvss_score = cvss_score
        self.epss_score = epss_score
        self.semaphore = semaphore
        self.PRIORITIES_LIST = []
        self.NIST_BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        self.EPSS_URL = "https://api.first.org/data/v1/epss"

    def __check_cve_string(self, cve):
        return re.search('CVE-\d{4}-\d{4,7}', cve)
    
    def __model_append(self, cve_id, priority, epss, cvss_num, cvss_version, cvss_severity, cisa_key):
        model = {
            "cve": cve_id,
            "priority": priority,
            "epss": epss,
            "cvss_baseScore": cvss_num,
            "cvss_version": cvss_version,
            "severity": cvss_severity,
            "cisa_key": cisa_key
        }
        self.PRIORITIES_LIST.append(model)

    @cache
    def __nist_check(self, cve_id):
        try:
            params = {
                "cveId": cve_id
            }

            header = {'apiKey': f'{self.nvd_key}'}

            # Check if API has been provided
            if self.nvd_key:
                nvd_response = requests.get(self.NIST_BASE_URL, headers=header, params=params)
            else:
                nvd_response = requests.get(self.NIST_BASE_URL, params=params)

            nvd_status_code = nvd_response.status_code

            if nvd_status_code == 200:
                cisa_kev = False
                if nvd_response.json().get("totalResults") > 0:
                    for unique_cve in nvd_response.json().get("vulnerabilities"):

                        # Check if present in CISA's KEV
                        if unique_cve.get("cve").get("cisaExploitAdd"):
                            cisa_kev = True

                        # Collect CVSS Data
                        if unique_cve.get("cve").get("metrics").get("cvssMetricV31"):
                            for metric in unique_cve.get("cve").get("metrics").get("cvssMetricV31"):
                                results = {"cvss_version": "CVSS 3.1",
                                        "cvss_baseScore": float(metric.get("cvssData").get("baseScore")),
                                        "cvss_severity": metric.get("cvssData").get("baseSeverity"),
                                        "cisa_kev": cisa_kev}
                                return results
                        elif unique_cve.get("cve").get("metrics").get("cvssMetricV30"):
                            for metric in unique_cve.get("cve").get("metrics").get("cvssMetricV30"):
                                results = {"cvss_version": "CVSS 3.0",
                                        "cvss_baseScore": float(metric.get("cvssData").get("baseScore")),
                                        "cvss_severity": metric.get("cvssData").get("baseSeverity"),
                                        "cisa_kev": cisa_kev}
                                return results
                        elif unique_cve.get("cve").get("metrics").get("cvssMetricV2"):
                            for metric in unique_cve.get("cve").get("metrics").get("cvssMetricV2"):
                                results = {"cvss_version": "CVSS 2.0",
                                        "cvss_baseScore": float(metric.get("cvssData").get("baseScore")),
                                        "cvss_severity": metric.get("cvssData").get("baseSeverity"),
                                        "cisa_kev": cisa_kev}
                                return results
                        elif unique_cve.get("cve").get("vulnStatus") == "Awaiting Analysis":
                            print(f"{cve_id:<18}NIST Status: {unique_cve.get('cve').get('vulnStatus')}")
                else:
                    print(f"{cve_id:<18}Not Found in NIST NVD.")
            else:
                print(f"{cve_id:<18}Error code {nvd_status_code}")
        except requests.exceptions.ConnectionError:
            print(f"Unable to connect to NIST NVD, Check your Internet connection or try again")
            return None
        
    @cache
    def __epss_check(self, cve_id):
        try:
            params = {
                "cve": cve_id
            }

            epss_response = requests.get(self.EPSS_URL, params=params)
            epss_status_code = epss_response.status_code

            if epss_status_code == 200:
                if epss_response.json().get("total") > 0:
                    for cve in epss_response.json().get("data"):
                        results = {"epss": float(cve.get("epss")),
                                "percentile": int(float(cve.get("percentile"))*100)}
                        return results
                else:
                    return False
            else:
                print("Error connecting to EPSS")
        except requests.exceptions.ConnectionError:
            print(f"Unable to connect to EPSS, Check your Internet connection or try again")
            return None
        
    @cache
    def calc_priority_cve(self, cve_id):
        nist_result = self.__nist_check(cve_id)
        epss_result = self.__epss_check(cve_id)

        try:
            if nist_result.get("cisa_kev"):
                self.__model_append(cve_id, 'Priority 1+', epss_result.get('epss'),
                                nist_result.get('cvss_baseScore'), nist_result.get('cvss_version'),
                                nist_result.get('cvss_severity'), 'TRUE')
            elif nist_result.get("cvss_baseScore") >= self.cvss_score:
                if epss_result.get("epss") >= self.epss_score:
                    self.__model_append(cve_id, 'Priority 1', epss_result.get('epss'),
                                    nist_result.get('cvss_baseScore'), nist_result.get('cvss_version'),
                                    nist_result.get('cvss_severity'), 'FALSE')
                else:
                    self.__model_append(cve_id, 'Priority 2', epss_result.get('epss'),
                                    nist_result.get('cvss_baseScore'), nist_result.get('cvss_version'),
                                    nist_result.get('cvss_severity'), 'FALSE')
            else:
                if epss_result.get("epss") >= self.epss_score:
                    self.__model_append(cve_id, 'Priority 3', epss_result.get('epss'),
                                    nist_result.get('cvss_baseScore'), nist_result.get('cvss_version'),
                                    nist_result.get('cvss_severity'), 'FALSE')
                else:
                    self.__model_append(cve_id, 'Priority 4', epss_result.get('epss'),
                                    nist_result.get('cvss_baseScore'), nist_result.get('cvss_version'),
                                    nist_result.get('cvss_severity'), 'FALSE')
        except (TypeError, AttributeError):
            pass
    
    def process_list(self, cves_list):
        if type(cves_list) == list:
            for cve in cves_list:
                if self.__check_cve_string(cve=cve):
                    self.calc_priority_cve(cve_id=cve)
        else:
            return {'error': 'no list type'}
        
        return self.PRIORITIES_LIST
        
if __name__ == "__main__":
    c = consult(api_key_nvd='API_KEY_NVD')
    print(c.process_list(['CVE-2022-22965', 'CVE-2021-3749', 'CVE-2023-0842']))