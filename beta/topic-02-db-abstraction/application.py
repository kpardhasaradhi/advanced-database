from bottle import route, post, run, template, redirect, request, debug

import database

debug(True)

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    rows = database.get_players()
    return template("list.tpl", players_list=rows)

@route("/add")
def get_add():
    return template("add_item.tpl")

@post("/add")
def post_add():
    player_name = request.forms.get("player_name")
    team_name = request.forms.get("team_name")
    print(player_name)
    print(team_name)
    database.add_player(player_name,team_name)
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/list")

@route("/delete/<name>")
def get_delete(name):
    print("/delete ",name)
    database.delete_player(name)
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    rows = database.get_items(id)
    if len(rows) != 1:
        redirect("/list")
    description = rows[0]['description']
    return template("update_item.tpl", id=id, description=description)

@post("/update")
def post_update():
    description = request.forms.get("description")
    id = request.forms.get("id")
    database.update_item(id, description)
    redirect("/list")


@post("/search")
def get_player():
    player = request.forms.get("player")
    rows=database.search_player(player)
    if rows is "None":
        redirect("/list")
    print("/search ",rows)
    return template("player_view.tpl", players_list=rows)
    

# Updating the player name ************************************************
@route("/update/<name>")
def get_update(name):
    return template("update_item.tpl",old_name=name,new_name=name)


@post("/update")
def post_update():
    old_name = request.forms.get("old_name")
    new_name = request.forms.get("new_name")
    database.update_player(old_name,new_name)
    redirect("/list")
# ****************** Fetch teams *********************************
@post("/fetch_teams")
def get_teams():
    player_name = request.forms.get("player_name")
    rows=database.get_teams(player_name)
    return template("team_view.tpl", team_list=rows)

# ****************** Fetch Players *********************************
@post("/fetch_players")
def get_players():
    team_name = request.forms.get("team_name")
    rows=database.get_players(team_name)
    return template("player_view.tpl", players_list=rows)


run(host='localhost', port=8081)