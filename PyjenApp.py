import jenkins


class PyjenApp:
	def __init__(self, username, apitoken):
		self.username = username
		self.token = apitoken

	def get_jenkins_jobs(self):
		server = self.connect_to_jenkins(self.username, self.token)
		return server.get_jobs()

	def connect_to_jenkins(self, username, token):
		url = 'http://160.153.231.66:8080'
		server = jenkins.Jenkins(url, username=username, password=token)
		return server


obj = PyjenApp()
obj.get_version('http://160.153.231.66:8080', 'jenkins_admin', 'f525b32a5a42ddb819a2c59f5599c915')

	

