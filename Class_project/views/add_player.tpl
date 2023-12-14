<html>
<head>
  <script>
    function enableSubmit() {
      var playerInput = document.getElementById("player_name");
      var teamInput = document.getElementById("team_name");
      var submitButton = document.getElementById("submit_button");

      // Enable the submit button if both player and team are entered
      submitButton.disabled = !(playerInput.value && teamInput.value);
    }
  </script>
</head>
<body>
  <h2>Add New Player</h2>
  <hr/>
  <form action="/add" method="post" oninput="enableSubmit()">
    <p>Player: <input id="player_name" name="player_name" required/></p>
    <p>Team  : <input id="team_name" name="team_name" required/></p>
    <p><button id="submit_button" type="submit" disabled>Add</button></p>
  </form>
  <hr/>
</body>
</html>