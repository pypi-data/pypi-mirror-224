import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json

class LonadbClient:
    def __init__(self, host, port, name, password):
        self.name = name
        self.password = password
        self.port = port
        self.host = host

    async def encrypt(self, string, key):
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(string.encode())
        return {"nonce": nonce.hex(), "ciphertext": ciphertext.hex(), "tag": tag.hex()}

    async def decrypt(self, nonce, ciphertext, tag, key):
        cipher = AES.new(key, AES.MODE_EAX, nonce=bytes.fromhex(nonce))
        decrypted = cipher.decrypt(bytes.fromhex(ciphertext))
        return decrypted.decode()

    async def makeid(self, length):
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
        result = ""
        counter = 0
        while counter < length:
            result += characters[ord(get_random_bytes(1)) % len(characters)]
            counter += 1
        return result

    async def send_receive(self, data):
        process_id = await self.makeid(5)
        with socket.create_connection((self.host, self.port)) as client:
            client.sendall(json.dumps(data).encode())
            data_raw = client.recv(1024)
            return json.loads(data_raw)

    async def getTables(self):
        data = {
            "action": "get_tables",
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response.get("tables", [])

    async def getTableData(self, table):
        data = {
            "action": "get_table_data",
            "table": table,
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def deleteTable(self, table):
        data = {
            "action": "delete_table",
            "table:" {"name": table},
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def createTable(self, table):
        data = {
            "action": "create_table",
            "table:" {"name": table},
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def set(self, table, name, value):
        data = {
            "action": "set_variable",
            "table:" {"name": table},
            "variable": {
                "name": name,
                "value": value
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def delete(self, table, name):
        data = {
            "action": "remove_variable",
            "table:" {"name": table},
            "variable": {
                "name": name
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def get(self, table, name):
        data = {
            "action": "get_variable",
            "table:" {"name": table},
            "variable": {
                "name": name
            },
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def getUsers(self):
        data = {
            "action": "get_users",
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def createUser(self, name, password):
        data = {
            "action": "create_user",
            "user": {
                "name": name,
                "password": password
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def createUser(self, name):
        data = {
            "action": "delete_user",
            "user": {
                "name": name
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def checkPassword(self, name, password):
        data = {
            "action": "check_password",
            "checkPass": {
                "name": name,
                "password": password
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def checkPermission(self, name, permission):
        data = {
            "action": "create_user",
            "permission": {
                "user": name,
                "name": permission
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def removePermission(self, name, permission):
        data = {
            "action": "remove_permission",
            "permission": {
                "user": name,
                "name": permission
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def getPermissionsRaw(self, name):
        data = {
            "action": "get_permissions_raw",
            "user": {
                "name": name
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response

    async def addPermission(self, name, permission):
        data = {
            "action": "add_permission",
            "permission": {
                "user": name,
                "name": permission
            }
            "login": {
                "name": self.name,
                "password": await self.encrypt(self.password, process_id)
            },
            "process": process_id
        }
        response = await self.send_receive(data)
        return response