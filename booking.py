import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup as bs

#Enter the url here
urlMovie="https://in.bookmyshow.com/chennai/movies/star-wars-the-rise-of-skywalker/ET00115302"

def scrape():
    page=requests.get(urlMovie)
    soup=bs(page.content,'html.parser')
    temp=soup.select("#user-wts-true .__text")

    if temp!=[]:
        print("Nope, not yet.")
    else:
        print("Bookings are open!")
        
scheduler = BlockingScheduler()
scheduler.add_job(scrape, 'interval', hours=1)
scheduler.start()
        