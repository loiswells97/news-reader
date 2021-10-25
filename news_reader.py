import pyttsx3
import requests
from bs4 import BeautifulSoup

def getHeadlines(url):

    request=requests.get(url)
    soup=BeautifulSoup(request.content, "html.parser")

    titles=soup.find_all("h3")

    headlines=set()
    headline_string=""

    i=0
    while len(headlines)<5:
        headline=titles[i].string
        if headline not in headlines:
            headlines.add(headline)
            headline_string+=headline+".\n"
        i+=1

    return headline_string

def getWeather(url):
    request=requests.get(url)
    soup=BeautifulSoup(request.content, "html.parser")
    today=soup.find(class_="wr-date")
    dates=soup.find_all(class_="wr-date__long")
    dates.insert(0, today)

    forcasts=soup.find_all(class_="wr-day__details__weather-type-description")

    forcast_string=""
    for i in range(5):
        forcast_string+=dates[i].contents[0]+": "+forcasts[i].string+".\n"

    return forcast_string

engine=pyttsx3.init()
engine.setProperty('rate', 150)
engine.say(
            "The latest BBC News headlines are: \n"+getHeadlines("https://www.bbc.co.uk/news")+
            "The latest sport headlines are: \n"+getHeadlines("https://www.bbc.co.uk/sport")+
            "The latest South East Wales headlines are: \n"+getHeadlines("https://www.bbc.co.uk/news/wales/south_east_wales")+
            "The weather forcast for Newport is: \n"+getWeather("http://www.bbc.co.uk/weather/2641598"))
engine.runAndWait()
