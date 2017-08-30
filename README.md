### 1 Install Python 2.7/3.5

Python 2.7.x/3.5.x https://www.python.org/downloads/

### 2 Clone the repository

Via https

    git clone https://github.com/vaakinmade/py-jenkins.git

or via ssh

    git clone git@github.com:vaakinmade/py-jenkins.git

### 3 Install dependencies
At the project root there is a requirements file

    pip install -r requirements.txt

Note that the python-jenkins package installs three other dependencies

### 4 Run the script
 
    python PyjenApp.py

Proceed to check the jenkins.db for retrieved jobs and statuses.

A live Jenkins server with login credentials was specifically setup for this task.
Feel free to use or swap out.

