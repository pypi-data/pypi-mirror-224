#!/usr/bin/env python
# Copyright 2023 Chathuranga Abeyrathna. All Rights Reserved.
# iam-ssh-cli to sync IAM ssh keys to Linux boxes
# 
# ssh users
#

import boto3
from functions.common import get_users_in_group

def ssh_users(group):
    group_users = get_users_in_group(group)
    for user in group_users:
        get_user_ssh(user)
