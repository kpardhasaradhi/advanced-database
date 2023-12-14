import sqlite3
import traceback

connection = sqlite3.connect("Ipl.db")

def get_teams(player_name):
    cursor = connection.cursor()
    if player_name == None:
        rows = cursor.execute("""select team_id from player where player_name='{player_name}'""")
    else:
        query = f"SELECT team_id FROM player WHERE player_name ='{player_name}'"
        ids = cursor.execute(query).fetchall()
        team_ids = [team[0] for team in ids]
            
        # Use a comma-separated string of team_id values for the SQL query
        team_ids_str = ', '.join(map(str, team_ids))
        print(team_ids_str)
        # Construct and execute the SQL query with the IN operator
        query = f"SELECT team_name FROM team WHERE team_id IN ({team_ids_str})"
        rows = cursor.execute(query).fetchall()

        #rows = cursor.execute(f"select team_name from team where team_id='{1}'")

    rows = list(rows)
    #print(rows)
    rows = [ {'team_name':row[0]} for row in rows ]
    return rows

def search_player(name):
    cursor = connection.cursor()
    rows = cursor.execute(f"select player_name from player where player_name='{name}'").fetchone()
    if rows is not None:
        rows = list(rows)
        print ("search_player: ",rows)
        rows = [ {'player_name':row} for row in rows ]
    else:
        rows = "None"
    return rows

def get_players(team_name=None):
    
    cursor = connection.cursor()
    if team_name == None:
        rows = cursor.execute("""select distinct player_name from player""").fetchall()
    else:
        query = f"SELECT team_id FROM team WHERE team_name ='{team_name}'"
        result = cursor.execute(query).fetchone()
        id=int(result[0])
        query = f"SELECT distinct player_name FROM player WHERE team_id = ({id})"
        rows = cursor.execute(query).fetchall()
    

    rows = list(rows)
    print (rows)
    rows = [ {'player_name':row[0]} for row in rows ]
    return rows

def add_player(player_name,team_name):
    cursor = connection.cursor()
    print(player_name,team_name)
    try:
        team_name=team_name.upper()
        print("team_name",team_name)
        query = f"SELECT COUNT(*) FROM team WHERE UPPER(team_name) = UPPER('{team_name}')"
        result = cursor.execute(query).fetchone()
        #cursor.execute("Delete from player where player_name in ('Srinu','Pardhu','Jaddu')")
        count=0
        if result is not None:
            count = int(result[0])
        print("count",count)
        #Insert a new record only in the Player table if the team exists
        if count > 0:
            print("inside if")
            query = f"SELECT team_id FROM team WHERE UPPER(team_name) = UPPER('{team_name}')"
            result = cursor.execute(query).fetchone()
            print("after execution")
            team_id=int(result[0])    
            print("team_id ",team_id," Player",player_name)   
            #cursor.execute("INSERT INTO team (team_id, team_name) VALUES (?, ?)", (max_team_id, team_name))
            cursor.execute("INSERT INTO player (player_name, team_id) VALUES (?, ?)", (player_name, team_id))
            connection.commit()
        #Else insert a record into both Player and team table if the team doesn't exist. 
        else:
            query = f"SELECT max(team_id) FROM team"
            result = cursor.execute(query).fetchone()
            team_id=int(result[0])       
            print("id",id)
            max_team_id=team_id+1
            print("max team id",max_team_id)
            cursor.execute("INSERT INTO team (team_id, team_name) VALUES (?, ?)", (max_team_id, team_name))
            cursor.execute("INSERT INTO player (player_name, team_id) VALUES (?, ?)", (player_name, max_team_id))
            connection.commit()
       
    except Exception as e:
         print(f"Exception: {e}")
         traceback.print_exc()
         
def setup_database():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table team")
        cursor.execute("drop table player")
    except:
        pass
  
    cursor.execute("""CREATE TABLE player (player_id INTEGER PRIMARY KEY,player_name TEXT NOT NULL
                   ,team_id INTEGER, FOREIGN KEY (team_id) references team(team_id))""")
    cursor.execute(""" CREATE TABLE team (team_id INTEGER PRIMARY KEY,team_name TEXT NOT NULL)""")
    
    cursor.execute(f"insert into player (player_name,team_id) values ('Virat Kohli','1')")
    cursor.execute(f"insert into player (player_name,team_id) values ('Virat Kohli','2')")
    cursor.execute(f"insert into player (player_name,team_id) values ('MS Dhoni','1')")
    cursor.execute(f"insert into player (player_name,team_id) values ('MS Dhoni','3')")
    cursor.execute(f"insert into player (player_name,team_id) values ('Rahul','1')")
    cursor.execute(f"insert into player (player_name,team_id) values ('Rahul','2')")

    connection.commit()

    cursor.execute("INSERT INTO team (team_id, team_name) VALUES (1, 'INDIA')")
    cursor.execute("INSERT INTO team (team_id, team_name) VALUES (2, 'RCB')")
    cursor.execute("INSERT INTO team (team_id, team_name) VALUES (3, 'CSK')")
    connection.commit()

    rows = cursor.execute("""select player_id, player_name,team_name from player p join team t on 
                          p.team_id=t.team_id """)


    rows = cursor.execute("select player_name,team_name from team t join player p on t.team_id=p.team_id")

    connection.commit()

def update_player(old_name,new_name):
    cursor = connection.cursor()
    print("update_player: ",old_name," NN ",new_name)
    cursor.execute(f"update player set player_name='{new_name}' where player_name='{old_name}'")
    #rows = cursor.execute("""select distinct player_name from player""").fetchall()
    #print(list(rows))
    connection.commit()

def delete_player(name):
    cursor = connection.cursor()
    print(name)
    cursor.execute(f"delete from player where player_name='{name}'")
    connection.commit()

def test_setup_database():
#  print("testing setup_database()")
    setup_database()
    #items = get_teams('rahul')
#    items=get_players()
 #   delete_player('Chase master Kohli ')

def test_method(team_name='INDIA'):
    cursor=connection.cursor()
    query = f"SELECT team_id FROM team WHERE UPPER(team_name) = UPPER('{team_name}'"
    result = cursor.execute(query).fetchone()
    team_id=int(result[0])       
    print("team id:",team_id)


if __name__ == "__main__":
    test_setup_database()
   

