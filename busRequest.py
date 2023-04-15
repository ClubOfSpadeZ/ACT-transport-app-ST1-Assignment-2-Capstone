import requests
import datetime
import dicttoxml
from typing_extensions import Literal


def build(xmlDict):
    siriVersionTag = '<Siri xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="2.0" xmlns="http://www.siri.org.uk/siri">'
    rawXML = dicttoxml.dicttoxml(xmlDict, attr_type=False, custom_root='Siri').decode()
    XML = rawXML.replace("<Siri>", siriVersionTag)
    return XML


def URL(ServiceType, ServiceName):
    url = f"http://siri.nxtbus.act.gov.au:11000/{API_Key}/{ServiceType}/{ServiceName}.xml"
    return url


def timeCONVERT(time_str: str, date_str: str = None):
    time_obj = datetime.datetime.strptime(time_str, '%I:%M%p').time()

    if date_str is None:
        today = datetime.datetime.today().date()
        datetime_obj = datetime.datetime.combine(today, time_obj)

        time_iso = datetime_obj.isoformat()
        return time_iso
    else:
        date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        datetime_obj = datetime.datetime.combine(date, time_obj)

        time_iso = datetime_obj.isoformat()
        return time_iso


def smRequest(busStopID: int, previewTime: str = '30M', start: str = ..., direction: Literal['A', 'B'] = ...,
              stopType: Literal["all", "arrivals", "departures"] = ..., maxTrips: int = ..., debug: bool = False):
    f"""
    stop monitoring Request will give you the passing Buses at a given stop from a starting time and interval\n
    argument formats\n
    busStopID: XXXX\n
    previewTime: M for minutes H for hours, 30M\n
    maxTrips: int , Maximum number of trips to return\n
    sample: smRequest(busStopID=2032, previewTime='', direction='A', debug=False)
    """
    start = timeCONVERT(start)

    xmlDict = \
        {"ServiceRequest": {"RequestTimestamp": timeStamp, "RequestorRef": API_Key,
                            "StopMonitoringRequest": {"-version": "2.0", "RequestTimestamp": timeStamp,
                                                      "StartTime": start, "PreviewInterval": f"PT{previewTime}",
                                                      "MonitoringRef": busStopID, "DirectionRef": direction,
                                                      "StopVisitTypes": stopType, "MaximumStopVisits": maxTrips,
                                                      "MaximumTextLength": "1024"}}}

    if start is ...:
        xmlDict["ServiceRequest"]["StopMonitoringRequest"].pop("StartTime")
    if direction is ...:
        xmlDict["ServiceRequest"]["StopMonitoringRequest"].pop("DirectionRef")
    if stopType is ...:
        xmlDict["ServiceRequest"]["StopMonitoringRequest"].pop("StopVisitTypes")
    if maxTrips is ...:
        xmlDict["ServiceRequest"]["StopMonitoringRequest"].pop("MaximumStopVisits")

    if debug is True:
        print(xmlDict)
        print(build(xmlDict))
        return

    return requests.post(url=URL(ServiceType="sm", ServiceName="service"), data=build(xmlDict), headers=headers).text


def ptRequest(start="2:30pm", end="3:30pm", date: Literal['today', '15/4/2023'] = 'today', line: int = 0,
              direction: Literal['A', 'B'] = ..., debug: bool = False):
    f"""
    This will give you a timetable for a giving time and route for only the day the Request is sent\n
    argument formats\n
    start / end: %I:%M%p or HH:MMpm/am I.E 2:30pm\n
    date: %d/%m/%Y or dd/mm/yyyy I.E 15/4/2023\n
    direction: 'A' or 'B'\n
    line: int or '81' or '4'\n
    sample: ptRequest(start="6:00am", end="6:15am", line=4, direction='B', debug=False)
    """
    if date == 'today':
        start = timeCONVERT(start)
        end = timeCONVERT(end)
    else:
        start = timeCONVERT(start, date)
        end = timeCONVERT(end, date)

    xmlDict = \
        {"ServiceRequest": {"RequestTimestamp": timeStamp, "RequestorRef": API_Key,
                            "ProductionTimetableRequest": {"-version": "2.0", "RequestTimestamp": timeStamp,
                                                           "ValidityPeriod": {"StartTime": start, "EndTime": end},
                                                           "Lines": {"LineDirection": {"LineRef": f"ACT_{line}",
                                                                                       "DirectionRef": direction}}}}}

    if direction is ...:
        xmlDict["ServiceRequest"]["ProductionTimetableRequest"]["Lines"]["LineDirection"].pop("DirectionRef")

    if debug is True:
        print(xmlDict)
        print(build(xmlDict))
        return

    return requests.post(url=URL(ServiceType="pt", ServiceName="service"), data=build(xmlDict), headers=headers).text


def vmRequest(busID: int = 000, line: int = ..., direction: Literal['A', 'B'] = ..., debug: bool = False):
    f"""
    vehicle monitoring Request does not work\n
    argument formats\n
    BusID: int XXX\n
    line: int or '81' or '4'\n
    sample: vmRequest(busID=637, direction='A', debug=False)
    """
    xmlDict = \
        {"ServiceRequest": {"RequestTimestamp": timeStamp, "RequestorRef": API_Key,
                            "VehicleMonitoringRequest": {"-version": "2.0", "RequestTimestamp": timeStamp,
                                                         "VehicleMonitoringRef": f"VM_ACT_{busID}",
                                                         "LineRef": line, "DirectionRef": direction}}}
    if line is ...:
        xmlDict["ServiceRequest"]["VehicleMonitoringRequest"].pop("LineRef")
    if direction is ...:
        xmlDict["ServiceRequest"]["VehicleMonitoringRequest"].pop("DirectionRef")

    if debug is True:
        print(xmlDict)
        print(build(xmlDict))
        return

    return requests.post(url=URL(ServiceType="vm", ServiceName="service"), data=build(xmlDict), headers=headers).text


if __name__ == '__main__':
    API_Key = "EA1DEB"
    timeStamp = datetime.datetime.now().isoformat()
    headers = {'Content-Type': 'application/xml'}
