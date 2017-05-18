#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><body>"


is_root=false

decoded=$(printf '%b' "${QUERY_STRING//%/\\x}")
if [ -n "$decoded" ] && [[ $decoded =~ password=(.*) ]]; then
  password="${BASH_REMATCH[1]}"

  is_root="$(/home/root_access $password)"
fi

if ($is_root); then
cat <<EOT
  <h1>Users List :</h1>
  <table>
  <tr>
    <th>Username</th>
    <th>Password</th>
  </tr>
EOT

PGPASSWORD=mysecretpassword psql -h postgres -U postgres -c 'SELECT * from USERSX;' -Xt | while read -a Record; do echo "<tr><td>${Record[0]}</td><td>${Record[2]}</td></tr>"; done;

echo "</table>"
fi

cat <<EOT
<h1>Access to root dashboard</h1>
<form action="/cgi-bin/root.cgi">
  <label>Password: <input type="password" name="password" id="password"></label><br/>
  <input type="submit" value="Login">
</form>
</body></html>
EOT
