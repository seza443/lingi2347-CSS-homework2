#!/bin/bash
echo "Content-type: text/html"
echo ""


cat <<EOT
<html><body>
  <h1>Users List :</h1>
  <table>
  <tr>
    <th>Username</th>
    <th>Password</th>
  </tr>
EOT

PGPASSWORD=mysecretpassword psql -h postgres -U postgres -c 'SELECT * from USERSX;' -Xt | while read -a Record; do echo "<tr><td>${Record[0]}</td><td>${Record[2]}</td></tr>"; done;

cat <<EOT
    </table>
</body></html>
EOT
