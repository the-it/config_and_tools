#!/bin/sh
ansible-playbook -K --ask-vault-pass laptop.yml $1 $2 $3 $4 $5
