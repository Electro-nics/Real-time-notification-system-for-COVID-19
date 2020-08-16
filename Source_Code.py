from plyer import notification
#pip install player
import requests
from bs4 import BeautifulSoup
import time
def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\VS_Tutorial\icon.ico",
        timeout=10
    )
def getdata(url):
    r=requests.get(url)
    return r.text



if __name__ == "__main__":
    
    myHTMLdata=getdata('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myHTMLdata, 'html.parser')

    # print(soup.prettify())
    myDatastr=""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
       myDatastr+=tr.get_text()
    myDatastr=myDatastr[1:]
    Item_List = myDatastr.split("\n\n")


    States=["Maharashtra","Assam","Odisha","West Bengal"]
    for item in Item_List[0:33]:
        Data_List = item.split("\n")
        if Data_List[1] in States:

            
            nTitle="Cases of COVID-19"
            nText=f"States: {Data_List[1]}\nTotal Confirmed cases: {Data_List[2]}\nCured: {Data_List[3]}\nDeath: {Data_List[4]}"
            notifyme(nTitle, nText)
            time.sleep(2)
