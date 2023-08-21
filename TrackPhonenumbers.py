import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
number=input("Entry  phone number with country code:")
phone=phonenumbers.parse(number)
timeZone=timezone.time_zones_for_number(phone)
print("Timezone"+str(timeZone))
location=geocoder.description_for_number(phone,"en")
print("Location:"+location)
service=carrier.name_for_number(phone,"en")
print("Service provider:"+service)