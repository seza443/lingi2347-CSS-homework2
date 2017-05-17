#!/bin/bash
echo "Content-type: text/html"
echo ""

decoded=$(printf '%b' "${QUERY_STRING//%/\\x}")
if [ -n "$decoded" ]; then
  cat <<EOT
  <html><body>
    <h1>Secret</h1>
    My password is 1234
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

echo $decoded
fi
