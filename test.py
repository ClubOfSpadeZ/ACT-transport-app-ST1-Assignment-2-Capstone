import googlemaps
from datetime import datetime

APIkey = 'AIzaSyAzmIkaPnXXghoAImiCqL1wlYW5shytqKE'
client = googlemaps.Client(APIkey)

timenow = datetime.now()

hour = 10
minute = 30
midday = 'am'

time_str = f'{hour}:{minute}{midday}'
time = datetime.combine(timenow, datetime.strptime(time_str, '%I:%M%p').time())

response = client.directions({"lat": -35.418312, "lng": 149.11557}, {"lat": -35.416279, "lng": 149.095901}, mode='transit', departure_time=time)
print(response)