<html>
<body>
  <h2>Players List</h2>
  
  <hr/>
  <form id="searchPlayerForm" action="/search" method="post" oninput="enableSubmit()">
    <p>Search for a player: <input id="player" name="player" required/></p>
    <p><button id="submit_button" type="submit" disabled>Search</button></p>
  </form>
  <hr/>
  <form id="fetchTeamsForm" action="/fetch_teams" method="post">
    <table>
    % for player in players_list:
      <tr>
        <td>
          <a href="#" onclick="fetchTeams('{{player['player_name']}}')">
            {{player['player_name']}}
          </a>
        </td>
        <td><a href="/update/{{str(player['player_name'])}}">update</a></td>
        <td><a href="/delete/{{str(player['player_name'])}}">delete</a></td>
      </tr>
    % end
    </table>
    <!-- Set the player_name in the hidden input field -->
    <input type="hidden" id="player_name" name="player_name" value=""/>
  </form>
  <hr/>
  <a href="/add">Add new player</a>

  <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
  <script>
    function fetchTeams(playerName) {
      // Set the player_name value in the hidden input field
      $('#player_name').val(playerName);
      // Submit the form
      $('#fetchTeamsForm').submit();
    }
  </script>

   <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <script>
    function enableSubmit() {
      var playerInput = document.getElementById("player");
      var submitButton = document.getElementById("submit_button");

      // Enable the submit button if player name is entered
      submitButton.disabled = !(playerInput.value);
    }
  </script>
</body>
</html>
