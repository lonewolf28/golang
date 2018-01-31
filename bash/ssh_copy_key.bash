#!/bin/bash

server_ips=(
"169.55.137.228" 
"169.55.137.249"
"169.55.137.248"
"169.55.137.247"
"158.85.100.135"
"169.55.176.85"
"169.55.176.94"
"158.85.100.141"
"158.85.100.134"
"158.85.100.138"
"158.85.100.136"
"169.55.176.83"
"158.85.100.132"
"169.55.176.89"
"169.55.137.233"
)



for server in server_ips;
do
	ssh-keyscan -H "$i" >> ~/.ssh/known_hosts
	ssh -o 'UserKnownHostsFile=/dev/null' -o 'StrictHostKeyChecking no' ${server}
done