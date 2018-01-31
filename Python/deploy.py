#!/usr/bin/python

import getopt
import sys
import os
import subprocess
from subprocess import Popen, PIPE



shop_repo = '/home/raj/Repo/store'
content_repo = '/home/raj/Repo/wp-cms'
ansible_content_dir = '/home/raj/Repo/wp-cms/trellis'
ansible_shop_dir = '/home/raj/Repo/store/ansible'

def usage():
	print '''
	usage:
		env=prod or staging (required),
		node=web or shop (required),
		deploy (required)
	'''


try:
    opts, args = getopt.getopt(sys.argv[1:], 'e:n:o:h', ['env=', 'node=', 'option=' ,'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    elif opt not in ( '--env', '-e', '--node', '-n', '--option', '-o'):
        usage()
else:
    env, node, option = [ o[1] for o in opts ]



def git_pull():
    
    if env == 'prod' and node == 'web' and option == 'deploy':
        try:
        	os.chdir(content_repo)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)
    
        if os.getcwd() == content_repo:
        	git_checkout = subprocess.Popen(["git", "checkout", "master"], stdout=PIPE, stderr=PIPE)
        	chk_out, chk_err = git_checkout.communicate()
        	if 'origin/master' not in chk_out:
        		sys.exit(1)
        	else:
        		git_pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE )
        		pull_out, pull_err = git_pull.communicate()
        		print "{}".format(pull_err)
        		if pull_err:
        			print "Following error occured while trying to git pull: {}".format(pull_err)
        			sys.exit(1)
        		else:
        		 	print "content master branch is updated: {}".format(pull_out.strip())
        else:
            print "cannot change directory: exiting"
            sys.exit(1)

    elif env == 'staging' and node == 'web' and option == 'deploy':
        try:
        	os.chdir(content_repo)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)
    
        if os.getcwd() == content_repo:
        	git_checkout = subprocess.Popen(["git", "checkout", "staging"], stdout=PIPE, stderr=PIPE)
        	chk_out, chk_err = git_checkout.communicate()
        	if 'origin/staging' not in chk_out:
        		sys.exit(1)
        	else:
        		git_pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE )
        		pull_out, pull_err = git_pull.communicate()
        		print "{}".format(pull_err)
        		if pull_err:
        			print "Following error occured while trying to git pull: {}".format(pull_err)
        			sys.exit(1)
        		else:
        		 	print "content master branch is updated: {}".format(pull_out.strip())
        else:
            print "cannot change directory: exiting"
            sys.exit(1)

    elif env == 'prod' and node == 'shop' and option == 'deploy':
        try:
        	os.chdir(shop_repo)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)
    
        if os.getcwd() == shop_repo:
        	git_checkout = subprocess.Popen(["git", "checkout", "master"], stdout=PIPE, stderr=PIPE)
        	chk_out, chk_err = git_checkout.communicate()
        	if 'origin/master' not in chk_out:
        		sys.exit(1)
        	else:
        		git_pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE )
        		pull_out, pull_err = git_pull.communicate()
        		print "{}".format(pull_err)
        		if pull_err:
        			print "Following error occured while trying to git pull: {}".format(pull_err)
        			sys.exit(1)
        		else:
        		 	print "content master branch is updated: {}".format(pull_out.strip())
        else:
            print "cannot change directory: exiting"
            sys.exit(1)

    elif env == 'staging' and node == 'shop' and option == 'deploy':
        try:
        	os.chdir(shop_repo)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)
    
        if os.getcwd() == shop_repo:
        	git_checkout = subprocess.Popen(["git", "checkout", "staging"], stdout=PIPE, stderr=PIPE)
        	chk_out, chk_err = git_checkout.communicate()
        	if 'origin/master' not in chk_out:
        		sys.exit(1)
        	else:
        		git_pull = subprocess.Popen(["git", "pull"], stdout=PIPE, stderr=PIPE )
        		pull_out, pull_err = git_pull.communicate()
        		print "{}".format(pull_err)
        		if pull_err:
        			print "Following error occured while trying to git pull: {}".format(pull_err)
        			sys.exit(1)
        		else:
        		 	print "content master branch is updated: {}".format(pull_out.strip())
        else:
            print "cannot change directory: exiting"
            sys.exit(1)



    return 0



def ansible_excute():
	if env == 'prod' and node == 'web' and option == 'deploy':
		try:
        	os.chdir(ansible_content_dir)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)

        if os.getcwd() == ansible_content_dir:
        	ansible_deploy = subprocess.Popen(["ansible-playbook","-e", "site=medreleaf.com", "env=production"], stdout=PIPE, stderr=PIPE)
        	dep_out, dep_err = ansible_deploy.communicate()
        	if dep_err:
        		print "Error"
        	else:
        		print dep_out
        else:
            print "cannot change directory: exiting"
            sys.exit(1)

	elif env == 'staging' and node == 'web' and option == 'deploy':
		try:
        	os.chdir(ansible_content_dir)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)

        if os.getcwd() == ansible_content_dir:
        	ansible_deploy = subprocess.Popen(["ansible-playbook","-e", "site=staging.medreleaf.com", "env=staging"], stdout=PIPE, stderr=PIPE)
        	dep_out, dep_err = ansible_deploy.communicate()
        	if dep_err:
        		print "Error"
        	else:
        		print dep_out
        else:
            print "cannot change directory: exiting"
            sys.exit(1)

	elif env == 'prod' and node == 'shop' and option == 'deploy':
		try:
        	os.chdir(ansible_shop_dir)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)

        if os.getcwd() == ansible_content_dir:
        	ansible_deploy = subprocess.Popen(["ansible-playbook", "-i", "hosts/production", "deploy.yml", "-e", "site=shop.medreleaf.com"], stdout=PIPE, stderr=PIPE)
        	dep_out, dep_err = ansible_deploy.communicate()
        	if dep_err:
        		print "Error"
        	else:
        		print dep_out
        else:
            print "cannot change directory: exiting"
            sys.exit(1)

	elif env == 'staging' and node == 'shop' and option == 'deploy':
		try:
        	os.chdir(ansible_shop_dir)
        	print os.getcwd()
        except:
        	print "cannot change directory"
        	sys.exit(1)

        if os.getcwd() == ansible_content_dir:
        	ansible_deploy = subprocess.Popen(["ansible-playbook", "-i", "hosts/staging", "deploy.yml", "-e", "site=shop-stage.medreleaf.com"], stdout=PIPE, stderr=PIPE)
        	dep_out, dep_err = ansible_deploy.communicate()
        	if dep_err:
        		print "Error"
        	else:
        		print dep_out
        else:
            print "cannot change directory: exiting"
            sys.exit(1)
    return 0     



if __name__ == "__main__":
    if git_pull() == 0:
    	ansible_excute()
    	print "App deployed sucessfully!"




