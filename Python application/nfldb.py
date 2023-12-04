#import psycopg2
#import psycopg2.extras
#import datetime

#conn = None
#cur = None

#conn = psycopg2.connect(database = "nfldata", user= "postgres", host = 'localhost', port= 5433, password = 'SQLfall23')

#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
import psycopg2
import datetime
import os

conn = psycopg2.connect(database = "nfldata", user= "maddiemortensen", host = 'localhost')

class Player:

    def getAllPlayers(self):
        
        cursor = conn.cursor()
        print('------ All Players ------\n')
        cursor.execute("SELECT * FROM Player Order by spid")
        userList = cursor.fetchall()
        i = 0
        for user in userList:
            i += 1
            print(" ----- spID ",user[0],"-----")
            print(" Position : ", user[2])
            print(" Weight : ", user[3])
            print("\n")
        print('------ SUCCESS ------\n')

    def addPlayer(self):

        mycursor = conn.cursor()

        print('------ Add a Player ------\n')

        spID = int(input ('Enter sports person ID: '))
        position =  input('Enter player position : ')
        weight = input('Enter player weight : ')

        sql = 'INSERT INTO Player ("spid","picture","position","weight") VALUES (%s,%s,%s,%s)'
        val = (spID,None,position,weight)
        mycursor.execute(sql,val)
        conn.commit()

        #sql = 'SELECT * FROM SportsPerson WHERE spID=' +  str(spID)               
        #mycursor.execute(sql)
        #user = mycursor.fetchall()
        #print(" ----- User -----")
        #print(" Name : ", user[0][1])
        #print(" Birthday : ", user[0][2])
        #print(" College : ", user[0][3])
        #print("\n")

        print('------ SUCCESS ------\n')

    def getAllPlayersbyPosition(self):
        mycursor = conn.cursor()
        print('------ Get All Players by Position ------\n')
        n = input("Enter Position : ")
        sql = "Select sportsperson.name, sportsperson.college, player.position, player.weight From sportsPerson, Player where sportsperson.spId = player.spid and player.position='%s'" % n            
        mycursor.execute(sql)
        userList = mycursor.fetchall()

        if len(userList) == 0:
            print(" This position doesn't exist")
        else:
            i = 0
            for user in userList:
                i += 1
                print(" ----- Player -----")
                print(" Name : ", user[0])
                print(" College : ", user[1])
                print(" Position : ", user[2])
                print(" Weight : ", user[3])
                print("\n")

            print('------ SUCCESS ------\n')


    def getAllPlayerInformation(self):
        mycursor = conn.cursor()
        print('------ Get All Player Information ------\n')
        query = "SELECT sportsPerson.name, player.weight, sportsPerson.college, player.position, playedFor.salary FROM sportsPerson, Player, playedFor, team WHERE sportsPerson.spid = player.spid AND player.spid = playedFor.spid AND playedFor.teamid = team.teamid"
        mycursor.execute(query)
        userList = mycursor.fetchall()

        if len(userList) == 0:
                print("No player information available")
        else:
            i = 0
            for user in userList:
                i += 1
                print(f" ----- Player {i} -----")
                print("Name:", user[0])
                print("Weight:", user[1])
                print("College:", user[2])
                print("Position:", user[3])
                print("Salary:", user[4])
                print()

            print('------ SUCCESS ------\n')
    
    def deletePlayer(self):
        mycursor = conn.cursor()
        print('------ Delete Player by Name ------\n')
        n = input("Enter Player Name : ") 
        sql = "SELECT spid, name FROM sportsPerson WHERE name ='%s'" %n
        mycursor.execute(sql)
        userList = mycursor.fetchone()
  
        spId = userList[0]

        sql = "SELECT * FROM player WHERE spid='%s'" %spId
        mycursor.execute(sql)
        playerStats = mycursor.fetchall()
        
        sql = "DELETE FROM player WHERE spid ='%s'" %spId
        mycursor.execute(sql)

        if len(playerStats) == 0:
            print(" This player is not in the Database")
        else:
            i = 0
            for player in playerStats:
                i += 1
                print(" ----- Player Deleted-----")
                print(" spid : ", player[0])
                print(" Position : ", player[2])
                print(" Weight : ", player[3])
                print("\n")
            print('------ SUCCESS ------\n')

        


    def updatePlayer(self):
        mycursor = conn.cursor()
        print('------ Update Player Weight ------\n')
        spId = input("Enter Player spid : ") 
        weight = input("Enter Player's new weight : ") 
        sql = " UPDATE player SET weight = %s WHERE spid = %s" 
        mycursor.execute(sql, (weight, spId))

        sql = "SELECT * FROM player WHERE spid='%s'" %spId
        mycursor.execute(sql)
        playerStats = mycursor.fetchall()

        if len(playerStats) == 0:
            print(" This player is not in the Database")
        else:
            i = 0
            for player in playerStats:
                i += 1
                print(" ----- Player Updated Stats -----")
                print(" spid : ", player[0])
                print(" Position : ", player[2])
                print(" Weight : ", player[3])
                print("\n")
            print('------ SUCCESS ------\n')

        

class Coach:

    def getAllCoaches(self):
        
        cursor = conn.cursor()
        print('------ All Coaches ------\n')
        cursor.execute("SELECT * FROM Coach Order by spid")
        userList = cursor.fetchall()
        i = 0
        for user in userList:
            i += 1
            print(" ----- spID ",user[0],"-----")
            print(" Duration Coaching : ", user[1])
            print("\n")
        print('------ SUCCESS ------\n')

    def addCoach(self):

        mycursor = conn.cursor()

        print('------ Add a Coach ------\n')

        spID = int(input ('Enter the coach sportsPerson ID: '))
        duration =  input('Enter the number of years that the coach has coached that team : ')

        sql = 'INSERT INTO coach ("spid","duration") VALUES (%s,%s)'
        val = (spID,duration)
        mycursor.execute(sql,val)
        conn.commit()

        print('------ SUCCESS ------\n')
    
    def deleteCoach(self):
        mycursor = conn.cursor()
        print('------ Delete Coach by Name ------\n')
        n = input("Enter Coach Name : ") 
        sql = "SELECT spid, name FROM sportsPerson WHERE name ='%s'" %n
        mycursor.execute(sql)
        userList = mycursor.fetchone()
  
        spId = userList[0]

        sql = "SELECT * FROM coach WHERE spid='%s'" %spId
        mycursor.execute(sql)
        playerStats = mycursor.fetchall()
        
        sql = "DELETE FROM coach WHERE spid ='%s'" %spId
        mycursor.execute(sql)

        if len(playerStats) == 0:
            print(" This Coach is not in the Database")
        else:
            i = 0
            for player in playerStats:
                i += 1
                print(" ----- Coach Deleted-----")
                print(" spid : ", player[0])
                print(" Duration : ", player[1])
                print("\n")

            print('------ SUCCESS ------\n')

class Owner:
    def getAllOwners(self):
        
        cursor = conn.cursor()
        print('------ All Owners ------\n')
        cursor.execute("SELECT * FROM Owner Order by spid")
        userList = cursor.fetchall()
        i = 0
        for user in userList:
            i += 1
            print(" ----- spID ",user[0],"-----")
            print(" NetWorth : ", user[1])
            print(" Year they bought the Team : ", user[2])
            print("\n")
        print('------ SUCCESS ------\n')

    def addOwner(self):

        mycursor = conn.cursor()

        print('------ Add a Owner ------\n')

        spID = int(input ('Enter the coach sportsPerson ID: '))
        networth = int(input ('Enter their Networth: '))
        boughtYear = int(input ('Enter the Year that they bought the team: '))
        

        sql = 'INSERT INTO owner ("spid","networth", "boughtyear") VALUES (%s,%s, %s)'
        val = (spID,networth, boughtYear)
        mycursor.execute(sql,val)
        conn.commit()

        print('------ SUCCESS ------\n')
    
    def deleteOwner(self):
        mycursor = conn.cursor()
        print('------ Delete Owner by Name ------\n')
        n = input("Enter Coach Name : ") 
        sql = "SELECT spid, name FROM sportsPerson WHERE name ='%s'" %n
        mycursor.execute(sql)
        userList = mycursor.fetchone()

        spId = userList[0]

        sql = "SELECT * FROM owner WHERE spid='%s'" %spId
        mycursor.execute(sql)
        playerStats = mycursor.fetchall()
        
        sql = "DELETE FROM owner WHERE spid ='%s'" %spId
        mycursor.execute(sql)

        if len(playerStats) == 0:
            print(" This Owner is not in the Database")
        else:
            i = 0
            for player in playerStats:
                i += 1
                print(" ----- Coach Deleted-----")
                print(" spid : ", player[0])
                print(" Networth : ", player[1])
                print(" Year they Bought the Team : ", player[2])
                print("\n")

            print('------ SUCCESS ------\n')

    def updateOwner(self):
        mycursor = conn.cursor()
        print('------ Update Owner Networth ------\n')
        spId = input("Enter Owner spid : ") 
        worth = input("Enter Owner's new NetWorth : ") 
        sql = " UPDATE owner SET networth = %s WHERE spid = %s" 
        mycursor.execute(sql, (worth, spId))

        sql = "SELECT * FROM owner WHERE spid='%s'" %spId
        mycursor.execute(sql)
        playerStats = mycursor.fetchall()

        if len(playerStats) == 0:
            print(" This Owner is not in the Database")
        else:
            i = 0
            for player in playerStats:
                i += 1
                print(" ----- Owner Update Info -----")
                print(" spid : ", player[0])
                print(" NetWorth : ", player[1])
                print(" Year they Bought the Team : ", player[2])
                print("\n")
            print('------ SUCCESS ------\n')

class Organization:
    def addOrganization(self):
    
        mycursor = conn.cursor()

        print('------ Add Data to Organization Table ------\n')

        orgID = int(input('Enter organization ID: '))
        name = input('Enter organization name: ')

        sql = 'INSERT INTO organization ("orgid", "name") VALUES (%s, %s)'
        val = (orgID, name)
        mycursor.execute(sql, val)
        conn.commit()
        print('------ SUCCESS------\n')
        
    def selectOrganization(self):

        mycursor = conn.cursor()

        print('------ Select Data from Organization Table ------\n')

        try:
            sql = 'SELECT * FROM organization'
            mycursor.execute(sql)

            rows = mycursor.fetchall()

            if rows:
                print("orgID\tname")
                for row in rows:
                    print(f"{row[0]}\t{row[1]}")
            else:
                print("Not found in organization table")

        except psycopg2.Error as e:
            print(f'Error: {e}')

class SportsPerson:
    def getAllSportsPersons(self):
        
        cursor = conn.cursor()
        print('------ All NFL Coaches, Players, and Owners ------\n')
        try:
            cursor.execute("SELECT * FROM sportsPerson")
            userList = cursor.fetchall()
            i = 0
            for user in userList:
                i += 1
                print(" ----- Sports Person ",i,"-----")
                print(" Name : ", user[1])
                print(" Birthday : ", user[2])
                print(" College : ", user[3])
                print("\n")
            print('------ SUCCESS ------\n')
        except psycopg2.Error as e:
            print(f'Error: {e}')


    def addSportsPerson(self):

        mycursor = conn.cursor()

        print('------ Add a Sports Person ------\n')
        try:
            spID = int(input ('Enter sports person ID: '))
            name =  input('Enter name : ')
            date_entry = input('Enter a date in YYYY-MM-DD format: ')
            year, month, day = map(int, date_entry.split('-'))
            date1 = datetime.date(year, month, day)
            college = input('Enter college : ')

            sql = 'INSERT INTO sportsPerson ("spid","name","birthday","college") VALUES (%s,%s,%s,%s)'
            val = (spID,name,date1,college)
            mycursor.execute(sql,val)
            conn.commit()
            print('------ SUCCESS ------\n')

        except psycopg2.Error as e:
            print(f'Error: {e}')


        #sql = 'SELECT * FROM SportsPerson WHERE spID=' +  str(spID)               
        #mycursor.execute(sql)
        #user = mycursor.fetchall()
        #print(" ----- User -----")
        #print(" Name : ", user[0][1])
        #print(" Birthday : ", user[0][2])
        #print(" College : ", user[0][3])
        #print("\n")

        

class Team:

    def getAllTeams(self):
        
        cursor = conn.cursor()
        print('------ All Teams ------\n')
        try:
            cursor.execute("SELECT * FROM Team Order by teamid")
            userList = cursor.fetchall()
            i = 0
            for user in userList:
                i += 1
                print(" ----- teamID ",user[0],"-----")
                print(" Colors : ", user[1])
                print(" Home City : ", user[2])
                print(" Name : ", user[3])
                print("\n")
            print('------ SUCCESS ------\n')

        except psycopg2.Error as e:
            print(f'Error: {e}')


    def addTeam(self):

        mycursor = conn.cursor()

        print('------ Add a Owner ------\n')

        try:
            teamID = int(input ('Enter the TeamID: '))
            colors = (input ('List the team colors: '))
            city = (input ('Enter the home city of the Team: '))
            teamName = (input ('Enter the team name: '))
            

            sql = 'INSERT INTO team ("teamid","colors", "city", "name") VALUES (%s,%s, %s, %s)'
            val = (teamID,colors,city, teamName)
            mycursor.execute(sql,val)   
            conn.commit()

            #sql = 'SELECT * FROM SportsPerson WHERE spID=' +  str(spID)               
            #mycursor.execute(sql)
            #user = mycursor.fetchall()
            #print(" ----- User -----")
            #print(" Name : ", user[0][1])
            #print(" Birthday : ", user[0][2])
            #print(" College : ", user[0][3])
            #print("\n")

            print('------ SUCCESS ------\n')
        except psycopg2.Error as e:
            print(f'Error: {e}')
        
    def getAllPlayersonTeam(self):
    
        mycursor = conn.cursor()
        print('------ Get All Players on a Team ------\n')
    
        try:
            n = input("Enter Team Name : ")
            sql = "Select sportsPerson.name, sportsPerson.birthday, player.position, player.weight, playedFor.salary, team.name from sportsPerson, Player, playedFor, team  Where sportsPerson.spid = player.spid and sportsPerson.spid = playedFor.spid and team.teamid = playedFor.teamid and team.name='%s'" % n            
            mycursor.execute(sql)
            userList = mycursor.fetchall()

            if len(userList) == 0:
                print(" This team doesn't exist")
            else:
                i = 0
                for user in userList:
                    i += 1
                    print(" ----- Player -----")
                    print(" Player Name : ", user[0])
                    print(" Birthday : ", user[1])
                    print(" Position : ", user[2])
                    print(" Weight : ", user[3])
                    print(" Salary : ", user[4])
                    print(" Team Name : ", user[5])
                    print("\n")

            print('------ SUCCESS ------\n')
        except psycopg2.Error as e:
            print(f'Error: {e}')
    
class Award:

    def addAward(self):
        mycursor = conn.cursor()

        print('------ Add Data to award Table ------\n')

        organizationName = input('Enter organization name: ')
        spID = int(input('Enter sports person ID: '))

        sql = 'INSERT INTO award ("organizationname", "spid") VALUES (%s, %s)'
        val = (organizationName, spID)
        mycursor.execute(sql, val)
        conn.commit()
        print('------ SUCCESS: Data added to award Table ------\n')

    def selectAward(self):

        mycursor = conn.cursor()

        print('------ Select Data from award Table ------\n')

        try:
            sql = 'SELECT * FROM award'
            mycursor.execute(sql)

            rows = mycursor.fetchall()

            if rows:
                print("OrganizationName\tspID")
                for row in rows:
                    print(f"{row[0]}\t\t{row[1]}")
            else:
                print("Not found in award table")

        except psycopg2.Error as e:
            print(f'Error: {e}')

class PlayedFor:
    
    def addplayedFor(self):

        mycursor = conn.cursor()

        print('------ Add Data to playedFor Table ------\n')

        teamID = int(input('Enter Team ID: '))
        spID = int(input('Enter sports person ID: '))
        weight = float(input('Enter player weight: '))
        salary = float(input('Enter player salary: '))

        sql = 'INSERT INTO playedFor ("teamid", "spid", "weight", "salary") VALUES (%s, %s, %s, %s)'
        val = (teamID, spID, weight, salary)
        mycursor.execute(sql,val)
        conn.commit()
        print('------ SUCCESS ------\n')
        
        
    def selectPlayedfor(self):

        mycursor = conn.cursor()

        print('------ Select Data from playedfor Table ------\n')

        try:
            sql = 'SELECT * FROM playedfor'
            mycursor.execute(sql)

            rows = mycursor.fetchall()

            if rows:
                print("teamID\tspID\tWeight\tSalary")
                for row in rows:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
            else:
                print("Not found in playedFor table")

        except psycopg2.Error as e:
            print(f'Error: {e}')
        

class MainClass:

    def player(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1. Select")
        print("2. Insert")
        print("3. Update")
        print("4. Delete")
        print("5. Get All Players By Position")
        print("6. Get All Players By College")
        print("7. Get All Player Information")
        print("8. Exit")

        action_choice = int(input("Which Action You want to Perform?(1-8)\n"))

        if action_choice == 1:
            choice.getAllPlayers()
        elif action_choice == 2:
            choice.addPlayer()
        elif action_choice == 3:
            choice.updatePlayer()
        elif action_choice == 4:
            choice.deletePlayer()
        elif action_choice == 5:
            choice.getAllPlayersbyPosition()
        elif action_choice == 6:
            choice.getAllPlayersbyCollege()
        elif action_choice == 7:
            choice.getAllPlayerInformation()  # Method to retrieve all player information
        elif action_choice == 8:
            pass
        else:
            print("Wrong Choice")


    def coach(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1. Select")
        print("2. Insert")
        print("3. Delete")
        print("4. Exit")

        action_choice = int(input("Which Action You want to Perform?(1-4)\n"))

        if action_choice == 1:
            choice.getAllCoaches()
        elif action_choice == 2:
            choice.addCoach()
        elif action_choice == 3:
            choice.deleteCoach()
        elif action_choice == 4:
            pass
        else:
            print("Wrong Choice")

    def owner(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1. Select")
        print("2. Insert")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        action_choice = int(input("Which Action You want to Perform?(1-5)\n"))

        if action_choice == 1:
            choice.getAllOwners()
        elif action_choice == 2:
            choice.addOwner()
        elif action_choice == 3:
            choice.updateOwner()
        elif action_choice == 4:
            choice.deleteOwner()
        elif action_choice == 5:
            pass
        else:
            print("Wrong Choice")

    def organization(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1. Select")
        print("2. Insert")
        print("3. Exit")

        action_choice = int(input("Which Action You want to Perform?(1-3)\n"))

        if action_choice == 1:
            choice.selectOrganization()
        elif action_choice == 2:
            choice.addOrganization()
        elif action_choice == 3:
            pass
        else:
            print("Wrong Choice")

    def sportsPerson(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1. Select")
        print("2. Insert")
        print("3. Exit")

        action_choice = int(input("Which Action You want to Perform?(1-3)\n"))

        if action_choice == 1:
            choice.getAllSportsPersons()
        elif action_choice == 2:
            choice.addSportsPerson()
        elif action_choice == 3:
            pass
        else:
            print("Wrong Choice")

    def team(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1. Select")
        print("2. Insert")
        print("3. Exit")
        print("4. Get All Players By Team")

        action_choice = int(input("Which Action You want to Perform?(1-4)\n"))

        if action_choice == 1:
            choice.getAllTeams()
        elif action_choice == 2:
            choice.addTeam()
        elif action_choice == 4:
            choice.getAllPlayersonTeam()
        elif action_choice == 3:
            pass
        else:
            print("Wrong Choice")

    def award(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1.Select")
        print("2.Insert")
        print("3.Exit")

        action_choice = int(input("Which Action You want to Perform?(1-3)\n"))

        if action_choice == 1:
            choice.selectAward()
        elif action_choice == 2:
            choice.addAward()
        elif action_choice == 3:
            pass
        else:
            print("Wrong Choice")

    def playedFor(self, choice):
        print("----------------------------------------------------------------------------------------------")
        print("1. Select")
        print("2. Insert")
        print("3. Exit")

        action_choice = int(input("Which Action You want to Perform?(1-3)\n"))

        if action_choice == 1:
            choice.selectPlayedfor()
        elif action_choice == 2:
            choice.addplayedFor()
        elif action_choice == 3:
            pass
        else:
            print("Wrong Choice")

class MainDriver:

    def main():
        print("----------------------------------------------------------------------------------------------")
        print("                           Welcome To The NFL Players Database                                ")
        print("----------------------------------------------------------------------------------------------")

        mc = MainClass()

        while True:
            print("\nSelect the table you want to interact with :-")
            print("1.Player")
            print("2.Coach")
            print("3.Owner")
            print("4.Organization")
            print("5.SportsPerson")
            print("6.Team")
            print("7.Award")
            print("8.PlayedFor")
            print("9.Exit")

            table_choice = int(input("Enter your Choice(1-9)\n"))
            if table_choice == 1:
                p = Player()
                mc.player(p)
            elif table_choice == 2:
                c = Coach()
                mc.coach(c)
            elif table_choice == 3:
                o = Owner()
                mc.owner(o)
            elif table_choice == 4:
                org = Organization()
                mc.organization(org)
            elif table_choice == 5:
                sp = SportsPerson()
                mc.sportsPerson(sp)
            elif table_choice == 6:
                t = Team()
                mc.team(t)
            elif table_choice == 7:
                a = Award()
                mc.award(a)
            elif table_choice == 8:
                pf = PlayedFor()
                mc.playedFor(pf)
            elif table_choice == 9:
                break
            else:
                print("Wrong Choice!!")

if __name__ == "__main__":
    MainDriver.main()
