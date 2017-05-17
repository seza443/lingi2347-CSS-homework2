#!/bin/bash
echo "Content-type: text/html"
echo ""

decoded=$(printf '%b' "${QUERY_STRING//%/\\x}")
if [ -n "$decoded" ] && [[ $decoded =~ username=(.*)\&password=(.*) ]]; then
  username="${BASH_REMATCH[1]}"
  password="${BASH_REMATCH[2]}"
  echo "it is a match with $username and $password"

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
  <form action="/cgi-bin/login.cgi">
    <label>Username: <input type="text" name="username"></label><br/>
    <label>Password: <input type="password" name="password"></label><br/>
    <input type="submit" value="Login">
  </form>
</body></html>
EOT

fi
