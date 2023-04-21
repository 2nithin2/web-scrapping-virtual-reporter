import requests
from bs4 import BeautifulSoup
import pyttsx3
def speak(txt):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 150)     # setting up new voice rate
    voices = engine.getProperty('voices')
    engine.setProperty('voice', "US_DAVID_11.0")
    engine.say(txt)
    engine.runAndWait()

def get_news(url,no_of_headlines):
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the news headlines
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")

    # Print the headlines
    i=0
    txt="hi, todays top"+ str(3)+"headlines for you."
    speak(txt)
    for headline in headlines:   
        if i<no_of_headlines:
            print(i+1,headline.text.strip()+".")
            txt=headline.text.strip()+"."
            speak(txt)
        elif i==no_of_headlines:
            txt="These are the headlines of today. meet you soon, byee!"
            speak(txt)
            break
        i+=1
   # Make a request to the website

def main():
    url = "https://www.bbc.com/news/world/asia/india"
    msg="enter number of  head lines you want to listen"
    speak(msg)
    no_of_headlines=int(input(msg+"\n"))
    get_news(url,no_of_headlines)
main()