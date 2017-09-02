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
		self.save_job()

	def save_job(self):
		jobs = self.get_jenkins_jobs()
		PyjenDB.PyjenDB(jobs)


	def get_jenkins_jobs(self):
		server = self.connect_to_jenkins(self.username,	self.token)
		try: 
			jobs = server.get_jobs()
			
		except jenkins.JenkinsException as e:
			print(e)
			print("\nProceeding to use stub data")
			"""
			This is a simulation of what the get_jobs method returns.
			It will be used if a connection cannot be established to the live server
			"""
			jobs = [{'name': 'BLOG_PROJ',
				'_class': 'hudson.model.FreeStyleProject', 'url':
				'http://160.153.231.66:8080/job/BLOG_PROJ/', 'fullname': 'BLOG_PROJ',
				'color': 'notbuilt'}, {'name': 'LAGOROKU', '_class':
				'hudson.model.FreeStyleProject', 'url':
				'http://160.153.231.66:8080/job/LAGOROKU/', 'fullname': 'LAGOROKU', 'color':
				'red'}, {'name': 'LAGOROKU_PROJ', '_class': 'hudson.model.FreeStyleProject',
				'url': 'http://160.153.231.66:8080/job/LAGOROKU_PROJ/', 'fullname':
				'LAGOROKU_PROJ', 'color': 'blue'}]

		if type(jobs) is list:
			timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
			for each in jobs:
				each.update({"checked_at":timestamp})
		return jobs

	def connect_to_jenkins(self, username, token):
		url = 'http://192.169.177.227:8080'
		server = jenkins.Jenkins(url, username=username, password=token)
		return server


PyjenApp('jenkins_admin', 'aef5c4b166a5ead442da0d3131f8890b')	

