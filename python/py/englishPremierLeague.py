#-*- coding:utf-8 -*-ee
import urllib
import urllib2
import os
import match

from BeautifulSoup import BeautifulSoup

def analyze(data):
    soup = BeautifulSoup(data)
    tagList = soup.find("table", {"class":"results"})
    
    #get tr tags
    trTag = tagList.contents
    
    #ingored the first tr tag
    trTag = trTag[1:]

    tr = trTag[0]

    for tr in trTag:
        tds = tr.contents
        date = tds[0].contents[0]
        teams = tds[1].contents
        teamArr = teams[0].split("-")
        homeTeam = teamArr[0].strip()
        awayTeam = teamArr[1].strip()
        score = tds[2].contents[0]

        print date + "  " + homeTeam + " - " + awayTeam + " " + score 

    
    
    

def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)

    result = response.read()
    return result
    #f = open("d:/index.html", "w")
    #f.write(result)
    #f.close()


def main():
    posturl = "http://www.resultdb.com/english-premier-league/2011/"
    data = {"gamelimit":"10"}

    result = post(posturl, data)

    analyze(result)
    #ma = match.Match()
    #ma.setDate("xyz")
    #ma.setHomeTeam("China")
    #ma.setAwayTeam("Japan")
    #ma.setScore("10-1")

    #ma.display()


if __name__ == '__main__':
    main()

