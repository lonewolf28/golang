#!/bin/bash

if [ -e .vault_pass ]; then
	PASS=`cat .vault_pass`
	declare -x ANSIBLE_VAULT_PASSWORD=$PASS
else
	echo "Please create vault_pass file"
	exit
fi



