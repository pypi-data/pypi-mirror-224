__version__ = "2023.08.13.01"
__description__ = "A Discord API wrapper so easy, a cat can code in it!"
__author__ = "rixthetyrunt@gmail.com"
intVals = {"GUILDS": 1, "GUILD_MEMBERS": 2, "GUILD_MODERATION": 4, "GUILD_EMOJIS_AND_STICKERS": 8, "GUILD_INTEGRATIONS": 16, "GUILD_WEBHOOKS": 32, "GUILD_INVITES": 64, "GUILD_VOICE_STATES": 128, "GUILD_PRESENCES": 256, "GUILD_MESSAGES": 512, "GUILD_MESSAGE_REACTIONS": 1024, "GUILD_MESSAGE_TYPING": 2048, "DIRECT_MESSAGES": 4096, "DIRECT_MESSAGE_REACTIONS": 8192, "DIRECT_MESSAGE_TYPING": 16384, "MESSAGE_CONTENT": 32768, "GUILD_SCHEDULED_eS": 65536, "AUTO_MODERATION_CONFIGURATION": 1048576, "AUTO_MODERATION_EXECUTION": 2097152}

class Intents:
	def __init__(self):
		super().__setattr__("__intObj__", {})
		for inte in intVals.keys():
			self.__intObj__[inte] = False
	def __setattr__(self, key, val):
		if key not in intVals.keys():
			raise ValueError(f"Invalid intent '{key}'; for more information, visit https://discord.com/developers/docs/topics/gateway#list-of-intents")
		if val not in [True, False]:
			raise TypeError(f"Value of intent '{key}' must be 'bool'")
		self.__intObj__[key] = val
	def __getattr__(self, key):
		if key not in intVals.keys():
			raise ValueError(f"Invalid intent '{key}'; for more information, visit https://discord.com/developers/docs/topics/gateway#list-of-intents")
		return self.__intObj__[key]
	def __int__(self):
		res = 0
		for inte in intVals.keys():
			if self.__intObj__[inte]:
				res += intVals[inte]
		return res

class Bot:
	def __init__(self):
		self.events = {}
		self.intents = Intents()
	def run(self, token):
		import websocket as ws
		import json
		import os
		gateway = "wss://gateway.discord.gg/?encoding=json"
		wsObj = websocket.create_connection(gateway)
		wsObj.send(json.dumps({
			"op": 2,
			"d": {
				"token": token,
				"intents": int(self.intents),
				"properties": {
					"$os": os.name,
					"$browser": __package__,
					"$device": "Python"
				}
			}
		}))
		try:
			while True:
				e = json.loads(ws.recv())
				if e["op"] == 10:
					heartbeat_interval = e["d"]["heartbeat_interval"]
					ws.send(json.dumps({"op": 1, "d": None}))
				elif e["op"] == 11:
					print("Received Heartbeat ACK")
				elif e["op"] == 0: 
					# Event type = e["t"]; data = e["d"]
					print(f"Received {e['t']} event:", e["d"])
		except: pass
		wsObj.close()
	def on(e):
		def wrap(func):
			if e not in self.events:
				self.events[e] = []
			self.events[e].append(func)
		return wrap

bot = Bot()
del globals()["Bot"]

__all__ = (
	"Intents",
	"bot",
	"__version__",
	"__description__",
	"__author__"
)

__dir__ = lambda: [].__class__(__all__)