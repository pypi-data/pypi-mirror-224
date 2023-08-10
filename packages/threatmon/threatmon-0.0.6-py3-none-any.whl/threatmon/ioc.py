import json
from pprint import pprint
import requests
import time
import re
import socket
from OTXv2 import OTXv2, IndicatorTypes
from stix2 import Indicator
import json
from pandas.io.json import json_normalize
import requests
import urllib3
from base64 import b64encode

# Disable insecure https warnings (for self-signed SSL certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ioc():
    def __init__(self, api_token = "", limit = 10):
        self.api_token = api_token
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        self.limit = limit
        self.json_data = {
            'api_token': self.api_token,
            'limit': self.limit,
        }

    def daily_ioc(self,):
        if self.api_token == "":
            return print("Please Use Your API Token")
        if self.limit > 100:
            return print("Limit can not exceed 100")

        return requests.post(
            'https://ioc.threatmonit.io/api/daily-ioc/',
            headers=self.headers,
            json=self.json_data,
        ).json()

    def QRadarIntegration(self, 
                        import_data,
                        qradar_auth_key,
                        qradar_server,
                        qradar_ref_set
                        ):
        
        # self.qradar_auth_key = "811aacf9-jh68-444h-98f4-5d25b7a94844"
        self.qradar_ref_set = "THREATMON_Event_IOC"

        QRadar_POST_url = f"https://{qradar_server}/api/reference_data/sets/bulk_load/{qradar_ref_set}"

        self.QRadar_headers = {
            'sec': qradar_auth_key,
            'content-type': "application/json",
        }

        print(time.strftime("%H:%M:%S") + " -- " + "Initiating, IOC POST to QRadar ")
        files = []

        for key in import_data["entities"]:
            files.extend(ioc["hash"] for ioc in key["hashes"])
            
        qradar_response = requests.request("POST", QRadar_POST_url, data=files, headers=self.QRadar_headers, verify=False)
        if qradar_response.status_code == 200:
            print(time.strftime("%H:%M:%S") + " -- " + " (Finished) Imported IOCs to QRadar (Success)" )
        else:
            print(time.strftime("%H:%M:%S") + " -- " + "Could not POST IOCs to QRadar (Failure)")
            
    def SentinelIntegration(self,
                            import_data,
                            bearerToken,
                            workspaceId,
                            systemName,
                            ):  # sourcery skip: avoid-builtin-shadow
        
        ioc_list = []
        api_url = f"https://sentinelus.azure-api.net/{workspaceId}/threatintelligence:upload-indicators?api-version=2022-07-01"
                        
        for iocs in import_data["entities"]:
            for ioc in iocs["hashes"]:
                if ioc["algorithm"] == "MD5":
                    hash = ioc["hash"]
                    indicator = Indicator(name="indicator",
                        pattern= f"[file:hashes.md5 = '{hash}']",
                        pattern_type="stix")
                    
                if ioc["algorithm"] == "SHA-1":
                    hash = ioc["hash"]
                    indicator = Indicator(name="indicator",
                        pattern= f"[file:hashes.sha1 = '{hash}']",
                        pattern_type="stix")
                    
                if ioc["algorithm"] == "SHA-256":
                    hash = ioc["hash"]
                    indicator = Indicator(name="indicator",
                        pattern= f"[file:hashes.sha256 = '{hash}']",
                        pattern_type="stix")
                    
                indicator = indicator.serialize(sort_keys=True)
                indicator = json.loads(indicator)
                ioc_list.append(indicator)

        request_body = {
            "sourcesystem": systemName,
            "value": ioc_list
        }
        
        headers = {
            'Authorization': bearerToken,
            'Content-Type': 'application/json',
        }
        
        try:
            microsof_api = requests.post(
                url=api_url,
                headers=headers,
                json=request_body,
            )
            if microsof_api.status_code == 200:
                print(time.strftime("%H:%M:%S") + " -- " + " (Finished) Imported IOCs to Sentinel (Success)" )
            else:
                print(time.strftime("%H:%M:%S") + " -- " + "Could not POST IOCs to Sentinel (Failure)")
        except Exception as e:
            print(e)
            
    def CrowdStrikeIntegration(self,
                               bearerToken,
                               import_data):
        # sourcery skip: avoid-builtin-shadow
        
        api_url = "https://api.crowdstrike.com/iocs/entities/indicators/v1"
        
        ioc_list = []
        
        headers = {
            'Authorization': bearerToken,
            'Content-Type': 'application/json',
        }
        
        for iocs in import_data["entities"]:
            for ioc in iocs["hashes"]:
                if ioc["algorithm"] == "MD5":
                    value = ioc["hash"]
                    type = "md5"
                    
                if ioc["algorithm"] == "SHA-256":
                    value = ioc["hash"]
                    type = "sha256"
                    
                if ioc["algorithm"] == "Domain":
                    type = "domain"
                    value = ioc["hash"]
                    
                if ioc["algorithm"] == "IPV4":
                    type = "ipv4"
                    value = ioc["hash"]
                    
                if ioc["algorithm"] == "IPV6":
                    type = "ipv6"
                    value = ioc["hash"]
                    
                ioc_dict = {
                    "type": type,
                    "value": value,
                    "policy": "none",
                    "apply_globally": False,
                }
                
                ioc_list.append(ioc_dict)
            
        response_data = {
            "indicators" : ioc_list,
        }
            
        try:
            crowdstrike = requests.post(
                url=api_url,
                headers=headers,
                json=response_data,
            )
            
            if crowdstrike.status_code == 200:
                print(time.strftime("%H:%M:%S") + " -- " + " (Finished) Imported IOCs to CrowdStrike (Success)" )
            else:
                print(time.strftime("%H:%M:%S") + " -- " + "Could not POST IOCs to CrowdStrike (Failure)")
                
        except Exception as e:
            print(e)

    def SplunkIntegration(self, token, import_data):
        # sourcery skip: avoid-builtin-shadow
        api_url = "https://api.trustar.co/api/2.0/submissions/indicators/upsert"
        
        ioc_list = []
        
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
        }
        
        for iocs in import_data["entities"]:
            for ioc in iocs["hashes"]:
                if ioc["algorithm"] == "MD5":
                    value = ioc["hash"]
                    type = "MD5"
                    
                if ioc["algorithm"] == "SHA-256":
                    value = ioc["hash"]
                    type = "SHA256"
                    
                if ioc["algorithm"] == "Domain":
                    type = "DOMAIN"
                    value = ioc["hash"]
                    
                if ioc["algorithm"] == "IPV4":
                    type = "IP4"
                    value = ioc["hash"]
                    
                if ioc["algorithm"] == "IPV6":
                    type = "IP6"
                    value = ioc["hash"]
                    
                ioc_dict = {
                    "id": "",
                    "title": "Indicator from ThreatMon API",
                    "enclaveGuid": "ThreatMon",
                    "tags":["ioc","threatmon"],
                    "observable": {
                            "type": type,
                            "value": value
                        }
                }
                
                ioc_list.append(ioc_dict)
            
        response_data = ioc_list
            
        try:
            splunk = requests.post(
                url=api_url,
                headers=headers,
                json=response_data,
            )
            
            if splunk.status_code == 200:
                print(time.strftime("%H:%M:%S") + " -- " + " (Finished) Imported IOCs to Splunk (Success)" )
            else:
                print(time.strftime("%H:%M:%S") + " -- " + "Could not POST IOCs to Splunk (Failure)")
                
        except Exception as e:
            print(e)


    def AlienVaultIntegration(self, token, import_data):
        # sourcery skip: avoid-builtin-shadow        
        ioc_list = []
        otx = OTXv2(token)
        
        for iocs in import_data["entities"]:
            for ioc in iocs["hashes"]:
                if ioc["algorithm"] == "MD5":
                    value = ioc["hash"]
                    type = "FileHash-MD5"
                    
                if ioc["algorithm"] == "SHA-256":
                    value = ioc["hash"]
                    type = "FileHash-SHA256"
                    
                if ioc["algorithm"] == "Domain":
                    type = "domain"
                    value = ioc["hash"]
                    
                if ioc["algorithm"] == "IPV4":
                    type = "IPv4"
                    value = ioc["hash"]
                    
                if ioc["algorithm"] == "IPV6":
                    type = "IPv6"
                    value = ioc["hash"]
                    
                ioc_dict = {
                    "indicator": value,
                    "description": "",
                    "type": type,
                }
                
                ioc_list.append(ioc_dict)
                
        try:
            new_pulse = otx.create_pulse(name="Threatmon IOCs", indicators=ioc_list, public=False)
            pprint(json_normalize(new_pulse))
            
        except Exception as e:
            print(e)
