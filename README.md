# Uni-Manager
#How do I install the environment?
Below are the steps to
#!shell
git init
git remote add upstream https://USER_NAME@bitbucket.org/loducode/glypi.git
git checkout -b develop
git pull upstream develop
git checkout -b mi_rama
git rebase develop
