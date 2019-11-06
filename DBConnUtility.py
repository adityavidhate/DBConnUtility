# This code has functions to help set a psycopg2 connection to a database and return the connection or the cursor as required
# It reads from the general config file cfg.json

import json
import psycopg2 as pg
import getpass
from pathlib import Path

class DBConnUtility:

	def __init__(self, config_file=None):
		if config_file==None:
			config_file="cfg.json"

		self.conf_master=json.loads(open(config_file).read())
		self.db=self.conf_master['db']
		self.db['password']=getpass.getpass('Password for {}: '.format(self.db['user']))

	def connection(self):
		conn=pg.connect(dbname=self.db['dbname'], host=self.db['host'], port=self.db['port'], user=self.db['user'], password=self.db['password'])
		return conn