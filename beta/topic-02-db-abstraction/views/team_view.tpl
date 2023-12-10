<html>
<body>
  <h2>Teams List</h2>
  <hr/>
  <form id="fetchPlayersForm" action="/fetch_players" method="post">
    <table>
    % for team in team_list:
      <tr>
        <td>
          <a href="#" onclick="fetchPlayers('{{team['team_name']}}')">
            {{team['team_name']}}
          </a>
        </td>
      </tr>
    % end
    </table>
    <!-- Set the team_name in the hidden input field -->
    <input type="hidden" id="team_name" name="team_name" value=""/>
  </form>
  <hr/>
  <a href="/add">Add a new player</a>

  <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
  <script>
    function fetchPlayers(teamName) {
      // Set the team_name value in the hidden input field
      $('#team_name').val(teamName);
      // Submit the form
      $('#fetchPlayersForm').submit();
    }
  </script>
</body>
</html>


