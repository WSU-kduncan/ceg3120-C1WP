* status
    * shows: files not being tracked, files with changes that need to be committed, files out of sync with the remote repo
    * `git status`

* clone
    * clones an existing repo and creates a copy in pwd
    * `git clone 'url'`

* add 
    * adds a file in the local directory to the staging area, ready to be committed 
    * `git add 'filename'`

* rm 
    * removes a file from the staging area 
    * `git rm 'filename'`

* commit 
    * creates a new commit, files are ready to be pushed after being committed
    * `git commit`
    * `git commit -a`
        * adds all tracked files first
    * `git commit -m 'message'`
        * include your commit message in the command

* push 
    * upload your local repo to the remote repo
    * `git push`

* fetch 
    * checks the remote repo for changes without merging them into your local repo
    * `git fetch`

* merge 
    * merges all committed changes from one branch to the current 
    * `git merge 'branchname'`

* pull 
    * fetches, then merges
    * `git pull`

* branch 
    * create, delete, and list branches
    * `git branch 'branchname'`
        * creates a new branch
    * `git branch -d 'branchname'`
        * deletes a branch
    * `git branch -a`
        * lists branches

* checkout 
    * use to switch branches
    * `git checkout 'branchname'`