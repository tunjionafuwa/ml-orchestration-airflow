#!/usr/bin/env sh


echo "####################### ACTIVATE GIT BRANCH NAME IN TERMINAL #######################"
echo 'parse_git_branch() {
    git branch --show-current 2>/dev/null
}
export PS1="\[\e[32m\]\u@\h \[\e[33m\]\w \[\e[36m\]\$(parse_git_branch)\[\e[0m\]$ "' >> ~/.bashrc
source ~/.bashrc

echo "####################### INSTALLING REQUIREMENTS #######################"
pip install -r requirements.txt

echo "####################### INSTALLING DEV REQUIREMENTS #######################"
pip install -r dev_requirements.txt
