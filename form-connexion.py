import fonctions
def index(req):
    req.content_type = "text/html"
    html = """
<form method="post" action="connexion.py">
 <table>
  <tr>
    <td>Login: </td>
    <td><input type="text" name="login"/></td>
  </tr>  
   <tr>
    <td>Mot de passe: </td>
    <td><input type="password" name="password"/></td>
    <td><input type="submit" value="Valider"/></td>
  </tr>
</table>
</form>"""
    req.write(fonctions.codeHTML('titre',html))



  