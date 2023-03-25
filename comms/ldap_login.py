from ldap3 import Server, Connection, SAFE_SYNC
import os
import json

class LDAP():

    def __init__(self) -> None:
        self.conn = Connection(os.environ.get("LDAP_URI"), auto_bind=True)

    def log_in(self, username, password):
        query = "(&(&(userid={username})(userPassword={password})))".format(username=username, password=password)
        
        if not self.conn.search("ou=users,dc=fiit,dc=stu,dc=org", query):
            # no user found
            return None
        user = json.loads(self.conn.entries[0].entry_to_json())
        parts = user["dn"].split(",")
        for part in parts:
            if part.startswith("cn="):
                logged_in_user = part.replace("cn=", "")
                break
        
        return logged_in_user