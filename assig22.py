import json,ssl
import urllib.request,urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# #Stroring the given parameters
# api_key = 42
# serviceurl = "http://py4e-data.dr-chuck.net/json?"
# # sample_address = "South Federal University"
# data_address = "Rochester Institute of Technology"
# address_wanted = data_address
########################################################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
api_key = 42
location = input("Enter location: ")
#test: South Federal University
#assignment: Rochester Institute of Technology
base_url = "http://py4e-data.dr-chuck.net/json?"
address_param = urllib.parse.urlencode({'address': location})
target = base_url + address_param
#############################################################################
#Setting the GET parameters on the URL
parameters = {"address": address_wanted, "key":api_key}
paramsurl = urllib.parse.urlencode(parameters)

#Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl.strip() + paramsurl.strip()
print("DATA URL: ", queryurl)

#Obtaining and reading the data
try :
    data_read = urllib.request.urlopen(queryurl , context=ctx).read()
    data = data_read.decode()
    # Parsing the data and looking for the field we want.
    jsondata = json.loads(data)
    print(jsondata)
    place_id = jsondata["results"][0]["place_id"]
    print("PLACE ID: ", place_id)
except:
    print("Error.....")
    print("-"*50)
    print(data)
################################################################################################    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print ("Retrieving {0}".format(target))
connection = urllib.request.urlopen(target)
raw_data = connection.read().decode()
print ("Retrieved {0} characters".format(len(raw_data)))
parsed_data = json.loads(raw_data)
#print(parsed_data)

print ("Place id", parsed_data["results"][0]["place_id"])
##################################################################################################