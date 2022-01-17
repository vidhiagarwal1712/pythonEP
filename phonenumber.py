from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier
import os
os.system('cls')


service_provider = phonenumbers.parse("+61470485100" )
print(carrier.name_for_number(service_provider,
                              'en')) 

ch_number = phonenumbers.parse("+61470485100","CH")
print(geocoder.description_for_number(ch_number,"en"))