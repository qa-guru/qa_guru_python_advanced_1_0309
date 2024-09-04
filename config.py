class Server:
    def __init__(self, env):
        self.reqres = {
            "dev": "",
            "beta": "",
            "rc": "https://reqres.in",
        }[env]
        self.ninjacats = {
            "dev": "",
            "beta": "",
            "rc": "https://ninjactas.com",
        }[env]
