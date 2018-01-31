#!/usr/bin/python2
import os.path

def get_vault_password():
    """
    The magic happenz
    """

    pass_name = ""

    if os.path.isfile(".vault_pass"):
        with open(".vault_pass") as f:
            pass_name = f.read()
    else:
        pass

    if pass_name:
        print pass_name.strip()

if __name__ == '__main__':
    get_vault_password()