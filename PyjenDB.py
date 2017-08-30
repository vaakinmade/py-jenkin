"""
Initialises db connection and sets up Jobs table.
Iterates through jobs dictionary, saves to db and closes connection.
"""

import sqlite3 as lite
 

class PyjenDB():
	
	def __init__(self):       
		self.db = lite.connect('jenkins.db')
		self.db.row_factory = lite.Row        
		self.db.execute('''CREATE TABLE IF NOT EXISTS Jobs
							(Name TEXT, Class TEXT, Url TEXT,
							Status TEXT, Checked_at TEXT)''')

	def save(self, jobs):
		status = ""
		for job in jobs:
			if job['color'] == "blue":
				status = "Successful"
			elif job['color'] == "red":
				status = "Failure"
			elif job['color'] == "notbuilt":
				status = "Not built"

			self.db.execute('''INSERT INTO Jobs (Name, Class, Url, Status, Checked_at)
							    VALUES (?, ?, ?, ?, ?)''', ((job['name'],
							                                       job['_class'],
							                                       job['url'],
							                                       status,
							                                       job['checked_at'])))
		self.db.commit()
		self.db.close()