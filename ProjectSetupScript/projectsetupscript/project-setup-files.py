#!/usr/bin/env python3

import click
import os
import platform

class CommitlintSetup:
    
    def __init__(self, os):
        self.os_being_used = os
        self.os_being_used = platform.system()
        self.distro_being_used = platform.node()
        self.package_manager = ""
    
    def __install_package(self, package_manager, package="", options=""):
        """ We need to install some packages so this generic function will help with that. """
        if package_manager == "brew" or "npm" or "npx" or "apt-get":
            if self.os_being_used == "Linux" or self.os_being_used == "Darwin":
                if not self.__program_installed(package):
                    os.system(f"{package_manager} install {package} {options}")
                else:
                    print(f"{package} is already installed.")            
            else:
                print(f"{self.os_being_used} is unsupported right now")
            
        else:
            print("Please use a supported package manager.")
  
            
    def __program_installed(self, package):
        """ We want to check if an app is installed before going to try install it. """
        installed = False
        response = os.system(f"which {package}")
        
        if response == 256:
            print(f"{package} already seems to be installed.")
        elif response == 0:
            installed = True
        else:
            print(f"ERROR: There was a problem searching for {package}")#

        return installed
            
    def setup_commitlint_linux(self):
        """ This function will run the commitlint setup for a project on linux. """
        print("Running the setup on linux")
        
        # Install pre-requisites
        self.__install_package(self.package_manager, "npm", "-y")
        self.__install_package(self.package_manager, "yarn", "-y")

        # The following commands are attained from https://github.com/conventional-changelog/commitlint
        # Install commitlint packages
        self.__install_package("npm", "--save-dev", "@commitlint/{config-conventional,cli}")

        # # Tell commitlint to use conventional config
        # os.system("echo 'module.exports = {extends: ['@commitlint/config-conventional']}' > commitlint.config.js")
        # self.__install_package("npm", "husky", "--save-dev")
        
        # # Activate git hooks
        # self.__install_package("npx husky")
        
        # # Add hook
        # self.__install_package("npx", "husky", "add .husky/commit-msg  'npx --no -- commitlint --edit ${1}'")

    def setup_commitlint_macos(self):
        """ This function will run the commitlint setup for a project on macos. """
        print("Running the setup on macos")

@click.command()
@click.option("--package_manager", required=True, help="This is the package manager which your distro supports. NOTE! Only apt and brew are supported at the moment!")
def setup_commitlint(package_manager):
    """ Simple program to complete a quick project setup to use commitlint. """
    project_setup = CommitlintSetup(package_manager)
    project_setup.setup_commitlint_linux()

if __name__ == '__main__':
    setup_commitlint()