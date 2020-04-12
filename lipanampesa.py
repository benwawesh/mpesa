import requests
import base64
import important
from access_token import generate_access_token
from datetime import datetime
from requests.auth import HTTPBasicAuth
print(datetime.now())
unformatted_time =datetime.now()
formatted_time= unformatted_time.strftime("%Y%m%d%H%M%S")
# print(formatted_time, "this is formatted time")
data_to_encode = important.business_shortCode + important.lipa_na_mpesa_passkey + formatted_time
encoded_string= base64.b64encode(data_to_encode.encode())
decoded_password= encoded_string.decode('utf-8')
print (encoded_string)
print(decoded_password)


  

def lipa_na_mpesa():
  
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": important.business_shortCode ,
    "Password": decoded_password,
    "Timestamp": formatted_time ,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "5",
    "PartyA":  important.partyA,
    "PartyB": important.business_shortCode  ,
    "PhoneNumber": important.partyA ,
    "CallBackURL": "https://ben.com/callback",
    "AccountReference": "12345678",
    "TransactionDesc": "school fees "
    }
    
    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)
# lipa_na_mpesa()
