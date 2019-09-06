from bs4 import BeautifulSoup
import requests
 
session = requests.Session()
portal_url = 'https://selfserve.publicmobile.ca/'
loginpage = session.get(portal_url,verify=False)
soup = BeautifulSoup(loginpage.text,"html.parser")

#Self Serve portal details
username = ""
password = ""

#initilaze viewstate objects
viewstate = soup.select("#__VIEWSTATE")[0]['value']
viewstategenerator = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
viewstateencrypted = soup.select("#__VIEWSTATEENCRYPTED")[0]['value']
eventvalidation = soup.select("#__EVENTVALIDATION")[0]['value']

item_request_body = {
"__EVENTTARGET":"",
"__EVENTARGUMENT":"",
"__VIEWSTATE":viewstate,
"__VIEWSTATEGENERATOR":viewstategenerator,
"__VIEWSTATEENCRYPTED":viewstateencrypted,
"__EVENTVALIDATION":eventvalidation,
"ctl00$FullContent$ContentBottom$LoginControl$UserName":username,
"ctl00$FullContent$ContentBottom$LoginControl$Password":password,
"ctl00$FullContent$ContentBottom$LoginControl$chkRememberUsername":"on",
"ctl00$FullContent$ContentBottom$LoginControl$LoginButton":"Log In"
}
 
response = session.post(url=portal_url, data=item_request_body, headers={"Referer": portal_url}, verify=False)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.find(id="PrePaidCurrentBalanceLabelPnP"))