#!/usr/bin/env python
# Copyright 2023 Chathuranga Abeyrathna. All Rights Reserved.
# iam-ssh-cli to sync IAM ssh keys to Linux boxes
# 
# Common Functions
#

import boto3
import os
import subprocess
from pwd import getpwnam 


def create_user(username):
    try:
        # Check if the user already exists
        subprocess.run(["id", username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"User '{username}' already exists.")
    except subprocess.CalledProcessError:
        # User doesn't exist, so create a new user
        try:
            subprocess.run(["sudo", "useradd", "-m", username], check=True)
            print(f"User '{username}' created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating user: {e.stderr.decode('utf-8')}")


def add_to_sudo(username):
    try:
        # Check if the user is already in the 'sudo' group
        subprocess.run(["groups", username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"User '{username}' is already in the 'sudo' group.")
    except subprocess.CalledProcessError:
        # User is not in the 'sudo' group, so add them
        try:
            subprocess.run(["sudo", "usermod", "-aG", "sudo", username], check=True)
            print(f"User '{username}' added to 'sudo' group.")
        except subprocess.CalledProcessError as e:
            print(f"Error adding user to 'sudo' group: {e.stderr.decode('utf-8')}")


def write_ssh_key(username, body, path):
    if not os.path.exists(path):
        os.makedirs(path)
    keys = open(path + "/authorized_keys.txt", "a")
    keys.write(body)
    keys.write("\n")
    keys.close()
    # Change permissions
    user_id = getpwnam(username).pw_uid
    group_id = grp.getgrnam(username)[2]
    os.chown(path, user_id, group_id)


def get_user_ssh(username):
    home_path = "home/" + username + "/.ssh"
    if os.path.exists(home_path + "/authorized_keys.txt"):
        os.remove(home_path + "/authorized_keys.txt")
    client = boto3.client('iam')
    # List SSH keys to get the SSHPublicKeyId
    list_ssh_keys = client.list_ssh_public_keys(
        UserName=username
    )
    key_ids = []
    for ids in list_ssh_keys['SSHPublicKeys']:
        key_ids.append(ids['SSHPublicKeyId'])
        get_ssh_key = client.get_ssh_public_key(
            UserName=username,
            SSHPublicKeyId=ids['SSHPublicKeyId'],
            Encoding='SSH'
        )
        if get_ssh_key['SSHPublicKey']['Status'] == 'Active':
            ssh_public_key_body = get_ssh_key['SSHPublicKey']['SSHPublicKeyBody']
            # create_user(username)
            write_ssh_key(username, ssh_public_key_body, home_path)


def get_users_in_group(group):
    client = boto3.client('iam')
    users = client.get_group(
        GroupName=group
    )
    usernames = []
    for user in users['Users']:
        usernames.append(user['UserName'])
        get_user_ssh(user['UserName'])
    
    return usernames
