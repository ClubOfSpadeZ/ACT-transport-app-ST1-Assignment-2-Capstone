import requests
import datetime
import dicttoxml

# Make an XML request to the URL
API_Key = "EA1DEB"
timeStamp = datetime.datetime.now().isoformat()


def smRequest(busStopID):
    url = f"http://siri.nxtbus.act.gov.au:11000/{API_Key}/sm/service.xml"

    xmlDict = \
        {"ServiceRequest": {"RequestTimestamp": timeStamp, "RequestorRef": API_Key,
                            "StopMonitoringRequest": {"-version": "2.0", "RequestTimestamp": timeStamp,
                                                      "PreviewInterval": "PT1H", "MonitoringRef": busStopID,
                                                      "MaximumStopVisits": "4", "MaximumTextLength": "160"}}}

    siriVersionTag = '<Siri xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="2.0" xmlns="http://www.siri.org.uk/siri">'
    rawXML = dicttoxml.dicttoxml(xmlDict, attr_type=False, custom_root='Siri').decode()
    return rawXML.replace("<Siri>", siriVersionTag), url

def ptRequest(start, end, line, direction):
    url = f"http://siri.nxtbus.act.gov.au:11000/{API_Key}/pt/service.xml"

    xmlDict = \
        {"ServiceRequest": {"RequestTimestamp": timeStamp, "RequestorRef": API_Key,
                            "ProductionTimetableRequest": {"-version": "2.0", "RequestTimestamp": timeStamp,
                                                      "ValidityPeriod": {"StartTime": start, "EndTime": end}, "Lines": {"LineDirection": {"LineRef": line, "DirectionRef": }}}}}

    siriVersionTag = '<Siri xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="2.0" xmlns="http://www.siri.org.uk/siri">'
    rawXML = dicttoxml.dicttoxml(xmlDict, attr_type=False, custom_root='Siri').decode()
    return rawXML.replace("<Siri>", siriVersionTag), url

def request(type, ):
    sm = smRequest(timeStamp, API_Key, busStopID=1231)

    headers = {'Content-Type': 'application/xml'}  # set what your server accepts
    print(requests.post(sm[1], data=sm[0], headers=headers).text)
