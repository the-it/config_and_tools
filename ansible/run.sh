#!/bin/sh
ANSIBLE_COW_SELECTION=random ansible-playbook -K --ask-vault-pass laptop.yml $1 $2 $3 $4 $5
