# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 09:37:03 2023

@author: heidy
"""

import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        # Generate a unique key for this website/username combination
        key = hashlib.sha256((website + username).encode('utf-8')).hexdigest()

        # Store the password in the dictionary
        self.passwords[key] = password

    def get_password(self, website, username):
        # Generate the key for this website/username combination
        key = hashlib.sha256((website + username).encode('utf-8')).hexdigest()

        # Return the password for this key (or None if it doesn't exist)
        return self.passwords.get(key)

    def list_passwords(self):
        # Print a list of all website/username combinations and their corresponding passwords
        for key, password in self.passwords.items():
            website, username = key[:32], key[32:]
            print(f"{website}\t{username}\t{password}")

if __name__ == '__main__':
    password_manager = PasswordManager()
    password_manager.add_password('google.com', 'johndoe', 'password123')
    password_manager.add_password('facebook.com', 'janedoe', '123password')
    password_manager.list_passwords()
