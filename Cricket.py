from pycricbuzz import Cricbuzz
import json
import time

cricket = Cricbuzz()
    
# Matches 
    #* Match result
    #* Match Number
    #* Match description
    #* Source
    #* Match Status
    #* Id

class Matches:
    __data = cricket.matches()
    global __Id
    def __init__(self):
        i = 0
        for match in self.__data:
            print i+1, " => ", match['mchdesc']
            i += 1
        ask = input('Choose match number: ')
        if ask < len(self.__data) :
            self.__Id = (ask-1)
            self.display()
        else:
            print "You have selected wrong choice "

    def display(self):
        print "####################################"
        match_selected = self.__data[self.__Id]
        for item in match_selected.keys():
            print item, " => ", match_selected[item]

    def getId(self):
        return (self.__Id)

    
    def Commentary(self):
        comm = cricket.commentary(self.__data[self.__Id]['id'])['commentary']
        for line in comm[:5]:
            print line.replace('<br//>','\\n')
            
        more = raw_input('Want to see more (y/n): ')
        if more == 'y' or more == 'Y':
            for line in comm[5:]:
                print line

    def Score_card(self):
        card = cricket.scorecard(self.__data[self.__Id]['id'])
        self.display()
        team_data = card['squad']
        for team in team_data:
            print "----------------------------------"
            print "Team : ", team['team']
            for player in team['members']:
                print player
            print "----------------------------------"
        for inning in card['scorecard']:
            print "Bowling : ",inning['bowlteam']
            print "Batting : ",inning['batteam']
            print "Total Rans : ",inning['runs']
            print "Total Wickets : ",inning['wickets']
            print "Total Overs : ", inning['overs']
            time.sleep(5)
            print "Bowling Performance : "
            print '|{:15}|{:^5}|{:^5}|{:^5}|'.format("Name","Runs","Overs","Wickets")
            for bowler in inning['bowlcard']:
                print '|{:15}|{:^5}|{:^5}|{:^5}|'.format(bowler['name'],bowler['runs'],bowler['overs'],bowler['wickets']) 
            print "Batting Performance : "
            print '|{:15}|{:^5}|{:^5}|{:^5}|{:^5}|'.format("Name","Runs","Balls","Fours","Sixs")
            for batman in inning['batcard']:
                print '|{:15}|{:^5}|{:^5}|{:^5}|{:^5}|'.format(batman['name'],batman['runs'],batman['balls'],batman['fours'],batman['six'])
                print "Result : {}".format(batman['dismissal'])
                print
            print


def main():
    c = Matches()
    print 'Options:\n'
    print '1. Score Card\n'
    print '2. Commentary\n'
    ask = input()
    if ask == 1 or ask == '1':
        c.Score_card()
    elif ask==2 or ask=='2' :
        c.Commentary()
    else :
        print 'Invalid input '


if __name__ == "__main__":
    cmd = raw_input('Press any key to start :')
    if len(cmd):  main()
    
