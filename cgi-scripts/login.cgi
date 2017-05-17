#!/bin/bash
echo "Content-type: text/html"
echo ""

decoded=$(printf '%b' "${QUERY_STRING//%/\\x}")
login_ok=false
login_attempted=false
if [ -n "$decoded" ] && [[ $decoded =~ username=(.*)\&password=(.*) ]]; then
  login_attempted=true
  username="${BASH_REMATCH[1]}"
  password="${BASH_REMATCH[2]}"

  sql_result=$(PGPASSWORD=mysecretpassword psql -h postgres -U postgres -c "SELECT * from USERSX WHERE username='$username' AND password='$password';")
  if [[ $sql_result =~ .*1.row.* ]]; then
    login_ok=true
  else
    login_ok=false
  fi
fi

if ( $login_ok ); then
  cat <<EOT
  <html><body>
    <h1>Profile of $username</h1>
    Your password is "$password"
  </body></html>
EOT
else

cat <<EOT
<html><body>
  <h1>Login form</h1>
EOT
if ( $login_attempted ); then
  echo "<strong style='color:red;'>Invalid username or password</strong>"
fi
cat <<EOT
  <form action="/cgi-bin/login.cgi">
    <label>Username: <input type="text" name="username" id="username"></label><br/>
    <label>Password: <input type="password" name="password" id="password"></label><br/>
    <input type="submit" value="Login">
  </form>
</body></html>
EOT

fi
