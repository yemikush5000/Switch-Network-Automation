# Devops-project
This script is written by Idowu Kusoro, but I bear no responsibility to its effect on your production Network,
first try it out with a show command and not a configuration change command on your switch before you deploy

Also, The code is written to solve a proble of changing passwords on and Enterprise switch could be hundreds or thousand, but the switches has no Tacacs login  but only different local passwords, so normally a user will need to try a couple of passwords from a list in a password file before they can login to one switch and make their config change.
This program solves that with the Intelligence built into it.
There are 2 files one for IP addresses of all switches in the Enterprise, one per line
a second file with the list of passwords to try and login to the switch
once logged in we can submit the commands we want the switch to do either a show or configuration change.
