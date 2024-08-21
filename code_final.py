import requests
import csv
import time


token = ''
Cookie = ''
captcha= ''
print("Developer's tools > Network tab > Payload tab -----Token looks like: \nR1WrScxq24AMC6zM4h6Xs1J7mNm2oRJlBp24b1XW")
token = input("Enter the token from :")
print("Developer's tools > Network tab > request header section > request header -----Cookie looks like: \n\nBIGipServerIRD_Website=689116170.47873.0000; XSRF-TOKEN=eyJpdiI6IlpzWE5RcitQYnUxTnhsR0lFeHlXeEE9PSIsInZhbHVlIjoiYWpYbFhYRDU2OEhKZ0h0cDd5aDJHUms5V1g3Qm9mYVprYk14blFFdEZSak8ycHJUR2cwTkJRZ1AwL2thdTkrdSIsIm1hYyI6IjUwZjBiODFhN2I4OTVhYzZlNjhlZGU5ZDA2NTI2NGQ2MDQzNWNiNTZlYTFlOTRiNjRlMzMxZjQwOGZlNDRmMGYifQ%3D%3D; ird_session=eyJpdiI6InF6aDgzN3J3RWRaQUxWZHFUaVNhSHc9PSIsInZhbHVlIjoiYUF4ZzN3ZVUxSjZTb0xQZkxHVXJLNG1oWWs4L2RCSS9KMGNEMEZ6YitEVFIzVUlWb0RXbmdQRk40VzlQenhsOSIsIm1hYyI6ImJlNTBhOTcyNzliODE3YmU1NWQzZDMxYWUzYjc2YTBkNWJhODg2NmU4MDBkM2NlZjJlNmYwYzBhOGJkM2ZhMzYifQ%3D%3D; TS0144b6e1=01066ef3095a8d911eb8352877352374ef71fa8172aae1684d4dec64570a03659ccfb68766dbdd1e3cea441aac3344d1e8d11345c4453edd3eaeffdac90b769b59bfbb8563cdfd710276e4448026364f6b2d8d8a5f841b3ed8eea6a4aafa536b13810dc8b2; TS8de900db029=08ee972670ab28002179bf339d0aabfb09c29154d2eed9c61cef29fbe1751e1b28c920f32064ce6bd03c4223d09878de\n")
Cookie = input("Enter the Cookie from request headers :")
print("Developer's tools > Network tab > Payload tab -----Captcha looks like: '5'\n")
captcha = input("Enter the captcha value from the site :")

url = 'https://ird.gov.np/statstics/getPanSearch'
with open("source.txt","r")as f:
    data_txt = f.readlines()
data_txt = [d.strip().split(',') for d in data_txt]
# print(data_txt)
pan_names = []

start = time.time()
with open("PAN_DETAILS_SEARCHED.csv",'w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    for original_name,pan_no in data_txt:
        try:
            data = {
                '_token': token,
                'pan': pan_no,
                'captcha': captcha
            }
            headers = {
                "Cookie": Cookie,
            }
            response = requests.post(url, headers=headers, data=data, timeout=30)
            dicts = response.json()
            nep_name = dicts['panDetails'][0]['trade_Name_Nep']
            eng_name = dicts['panDetails'][0]['trade_Name_Eng']
        except:
            nep_name = "none"
            eng_name = "none"
        if eng_name:    
            if str(original_name).lower().replace(' ','') == eng_name.lower().replace(' ',''):
                flag = 'match'
        
            else:
                flag = 'not match'
        else:
            flag = 'No english name in ird'
        pan_name = [pan_no,original_name,nep_name,eng_name,flag]
        # pan_names.append([pan_no,original_name,nep_name,eng_name,flag])
        print(f"{pan_no},{original_name},{eng_name}")
        writer.writerow(pan_name)
    
end = time.time()

elapsed = end-start
print(f"elapsed time = {elapsed}")