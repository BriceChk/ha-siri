"""SIRI API"""
import logging
import requests

_LOGGER = logging.getLogger(__name__)

class SIRIApi:
    def __init__(self, url, token, stop):
        self._token = token
        self._url = url
        self._stop = stop
        
    def get_stops(self):
        headers = {
            "Cache-Control": "no-cache"
        }
        response = requests.get(self._url + "?AccountKey=" + self._token +"&MonitoringRef=" + str(self._stop), headers=headers)
        
        data = {}
        if response.status_code == requests.codes.ok:
            response = response.json()
            _LOGGER.debug(response)
            
            if response['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]:
                if response['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']:
                    if response['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]:
                        data = response['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']
            return data
        else:
            _LOGGER.error('Failed to fetch SIRI data')
            return data
