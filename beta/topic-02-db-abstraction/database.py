import sqlite3

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
        id_count = int(result[0])
        print("Count:", id_count)
        team_id=0
        if result is not None:
            team_id = int(result[0])
        print("team_id",team_id)
        if team_id != 0:
            query = f"SELECT max(team_id) FROM team"
            result = cursor.execute(query).fetchone()
            team_id=int(result[0])       
            print("id",id)
            max_team_id=team_id+1
            print("max team id",max_team_id)
            cursor.execute("INSERT INTO team (team_id, team_name) VALUES (?, ?)", (max_team_id, team_name))
            cursor.execute("INSERT INTO player (player_name, team_id) VALUES (?, ?)", (player_name, max_team_id))
            connection.commit()
        else:
            pass
       
    except Exception as e:
        pass
         
        


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
    cursor.execute(f"insert into player (player_name,team_id) values ('rahul','1')")
    cursor.execute(f"insert into player (player_name,team_id) values ('rahul','2')")

    connection.commit()

    cursor.execute("INSERT INTO team (team_id, team_name) VALUES (1, 'India')")
    cursor.execute("INSERT INTO team (team_id, team_name) VALUES (2, 'RCB')")
    cursor.execute("INSERT INTO team (team_id, team_name) VALUES (3, 'CSK')")
    connection.commit()

    rows = cursor.execute("""select player_id, player_name,team_name from player p join team t on 
                          p.team_id=t.team_id """)


    rows = cursor.execute("select player_name,team_name from team t join player p on t.team_id=p.team_id")

    connection.commit()

def add_item(student_name):
    cursor = connection.cursor()
    cursor.execute(f"insert into student (name) values ('{student_name}')")
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    rows = cursor.execute(f"delete from student where id={id}")
    connection.commit()

def update_item(id, description):
    cursor = connection.cursor()
    cursor.execute(f"update student set name='{description}' where id={id}")
    connection.commit()

def test_get_items():
    print("testing get_items()")
    items = get_teams()
    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert 'id' in item
        assert type(item['id']) is int
        assert 'description' in item
        assert type(item['description']) is str
    example_id = items[0]['id']
    example_description = items[0]['description']
    items = get_teams(example_id)
    assert len(items) == 1
    assert example_id == items[0]['id']
    assert example_description == items[0]['description']

def test_setup_database():
    print("testing setup_database()")
    setup_database()
    #items = get_teams('rahul')
    items=get_players('India')
    #print(items)
    #assert len(items) == 5
    #descriptions = [item['description'] for item in items]
    #for description in ['apples', 'broccoli', 'pizza', 'tangerines', 'potatoes']:
    #    assert description in descriptions
"""
def test_add_item():
    print("testing add_item()")
    setup_database()
    items = get_items()
    original_length = len(items)
    add_item("licorice")
    items = get_items()
    assert len(items) == original_length + 1
    descriptions = [item['description'] for item in items]
    assert "licorice" in descriptions
"""

"""
def test_delete_item():
    print("testing delete_item()")
    setup_database()
    items = get_items()
    original_length = len(items)
    deleted_description = items[1]['description']
    deleted_id = items[1]['id']
    delete_item(deleted_id)
    items = get_items()
    assert len(items) == original_length - 1
    for item in items:
        assert item['id'] != deleted_id
        assert item['description'] != deleted_description
"""
"""
def test_update_item():
    print("testing update_item()")
    setup_database()
    items = get_items()
    original_description = items[1]['description']
    original_id = items[1]['id']
    update_item(original_id,"new-description")
    items = get_items()
    found = False
    for item in items:
        if item['id'] == original_id:
            assert item['description'] == "new-description"
            found = True
    assert found
"""
if __name__ == "__main__":
   # test_get_items()
    test_setup_database()
 #   test_add_item()
  #  test_delete_item()
   # test_update_item()
    #print("done.")
