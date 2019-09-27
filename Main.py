# Work with Python 3.6
import discord
import requests
from bs4 import BeautifulSoup
import os



client = discord.Client()


#returns word specified in argument
def define(word):
    r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(word)) #goes to link for word
    soup = BeautifulSoup(r.content, features="html.parser")                            #sets up soup
    def_header = soup.find("div", attrs={"class": "def-header"}).text                  #header is the word we are defining
    def_header = def_header[0:len(def_header)-8]                                       #header always ends in "unknown" this removes it
    meaning = soup.find("div", attrs={"class": "meaning"}).text                        #gets the definition
    example = soup.find("div", attrs={"class": "example"}).text                        #gets the example
    output = def_header + ": " + meaning + "\nEx: " + example                          #output string
    output = output.replace("'", "&apos")                                              #replaces weird formatting of ' from original
    return output                                                                      #returns the word, defintion, and example


#returns the word of the day from the homepage
def word_of_the_day():
    r = requests.get("http://www.urbandictionary.com")                                 #link is always homepage
    soup = BeautifulSoup(r.content, features="html.parser")                            #sets up soup
    def_header = soup.find("div", attrs={"class": "def-header"}).text                  #header is the word we are defining
    def_header = def_header[0:len(def_header)-8]                                       #header always ends in "unknown" this removes it
    meaning = soup.find("div", attrs={"class": "meaning"}).text                        #gets the definition
    example = soup.find("div", attrs={"class": "example"}).text                        #gets the example
    output = def_header + ": " + meaning + "\nEx: " + example                          #output string
    output = output.replace("'", "&apos")                                              #replaces weird formatting of ' from original
    return output                                                                      #returns the word, defintion, and example


#listeners for different commands
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #help command
    if message.content.startswith('/help'):
        msg = 'To use type !define followed by the word you wish to define.\nYou may also type !wotd for the word of the day'.format(message)
        await channel.send( msg)

    #define command
    if message.content.startswith('/define'):
        word = message.content[7:]
        msg = define(word).format(message)
        await channel.send( msg)

    #word of the day command
    if message.content.startswith('/wotd'):
        msg = word_of_the_day().format(message)
        await channel.send( msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv('TOKEN'))



