#!/usr/bin/env python
# Copyright 2023 Chathuranga Abeyrathna. All Rights Reserved.
# iam-ssh-cli to sync IAM ssh keys to Linux boxes
# 
# ssh sudo users
# 

import boto3
from functions.common import add_to_sudo

def ssh_sudo_users(group):
    group_users = get_users_in_group(group)
    for user in group_users:
        add_to_sudo(user)
