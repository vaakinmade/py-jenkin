"""
connect_to_jenkins
------------------
Establishes remote connection with Jenkins server via python-jenkins api.
Authenticates using apitoken as opposed to password - less vulnerable.
Returns connection instance.
"""

"""
get_jenkins_jobs
-----------------
Uses established Jenkins server connection to get the list of existing jobs.
Appends timestamp to each job.
Returns a list of job dictionaries 
"""


import jenkins
import PyjenDB
import datetime


class PyjenApp:
	def __init__(self, username, apitoken):
		self.username = username
		self.token = apitoken

	def save_job(self):
		db_obj = PyjenDB.PyjenDB()
		jobs = self.get_jenkins_jobs()
		db_obj.save(jobs)


	def get_jenkins_jobs(self):
		server = self.connect_to_jenkins(self.username,	self.token)
		try: 
			jobs = server.get_jobs()
		except jenkins.JenkinsException as e:
			print(e)
			jobs = None

		if type(jobs) is list:
			timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
			for each in jobs:
				each.update({"checked_at":timestamp})
		return jobs

	def connect_to_jenkins(self, username, token):
		url = 'http://192.169.177.227:8080'
		server = jenkins.Jenkins(url, username=username, password=token)
		return server


obj = PyjenApp('jenkins_admin', 'aef5c4b166a5ead442da0d3131f8890b')
obj.save_job()
	

