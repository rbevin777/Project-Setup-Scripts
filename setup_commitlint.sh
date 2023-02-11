#!/bin/bash

# Some initial functions to compartmentalise code to make it slightly more maintainable
function install_prerequisites()
{
    echo "Info ---> Installing pre-requisite package managers"
    sudo apt-get install npm -y
    sudo apt-get install yarn -y
}

function setup_commitlint()
{
    echo "Info ---> Installing and configuring commitlint"
    npm install --save-dev @commitlint/{cli,config-conventional}
    echo "module.exports = { extends: ['@commitlint/config-conventional'] };" > commitlint.config.js
}

function install_and_setup_husky()
{
    echo "Info ---> Installing husky"
    npm install husky --save-dev
    npx husky install
}

function test_setup()
{
    echo "Info ---> Test the commitlint and husky setup"
    npx husky add .husky/commit-msg  'npx --no -- commitlint --edit ${1}'
}

install_prerequisites
setup_commitlint
install_and_setup_husky
test_setup