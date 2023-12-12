<html>
<body>
<h2>Update Item</h2>
<form action="/update" method="post">
  <input type="hidden" name="old_name" value="{{old_name}}"/>
  <p>New name: <input name="new_name" value="{{new_name}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>