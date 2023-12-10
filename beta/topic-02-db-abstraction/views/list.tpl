<html>
<body>
<h2>Players List</h2>
<hr/>
<table>
% for player in players_list:
  <tr>
    <td><a href="/fetch_teams/{{player['player_name']}}">{{player['player_name']}}</td>
    <td><a href="/update/{{str(player['player_id'])}}">update</a></td>
    <td><a href="/delete/{{str(player['player_id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add new player</a>
</body>
</html>