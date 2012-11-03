#-*- coding:utf-8 -*-

class Match:
    def setDate(self, date):
        self.date = date
    
    def getDate(self):
        return self.date

    def setHomeTeam(self, homeTeam):
        self.homeTeam = homeTeam

    def getHomeTeam(self):
        return self.homeTeam

    def setAwayTeam(self, awayTeam):
        self.awayTeam = awayTeam

    def getAwayTeam(self):
        return self.awayTeam
        
    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def display(self):
        print self.date + "  " + self.homeTeam + " - " + self.awayTeam + "  " + self.score
