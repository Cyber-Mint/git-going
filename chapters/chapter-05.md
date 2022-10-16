# Advanced Git

## Git Stash

Reference: `https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning#_git_stashing`

## git reset
### As an alternative to git stash 
When you are busy with an incomplete branch say `900-feature-branch` but need to switch to another branch, you can create a WIP (Work in Progress) commit with `git commit -all -m "WIP"` and then switch branches to the desired branch eg `git checkout master` and then when you are done with `master` and wish to return to your Work in Progress, you need to `git checkout 900-feature-branch` and the roll back the **HEAD** to the parent of the "WIP" commit with a `git reset HEAD^`.  This will **unstage** the files in the WIP commit and leave you where you were before you were diverted.

### Using git reset
Git reset may be used in three modes:
`git reset --mixed` (the default) - updates the branch tip to the specified commit and unstages any changes by moving them to the working tree again
`git reset -soft` - updates the branch tip but makes no other changes ie leaves any staged files staged
`git reset --hard` - updates the branch tip to the specified commit and unstages any changes and **deletes** any changes from the working tree

> WARNING: `git reset --hard` may/will result in unrecoverable files so use with caution.<br>NOTE: `git reset` does not remove stash.

Reference: `https://www.atlassian.com/git/tutorials/undoing-changes/git-reset`

### git reset vs git restore
`git restore` is like a simplified `git reset` for undoing changes and reversing files back to a previous state. Example, having somehow broken/deleted `Makefile` in my current branch, I could `git restore --source master Makefile` to restore it from the `master` branch.

## squashing commits


## rebasing & cherry picking


## reverting



## forking & PR upstream
`https://jarv.is/notes/how-to-pull-request-fork-github/`


##  signed commits with GPG
`https://www.freecodecamp.org/news/what-is-commit-signing-in-git/`

---

> [Exercise 4](./exercise-04.md) : makes changes, use `git reflog` and `git reset` to move HEAD around and see effects.


---

## Run your own git server
> **SELF STUDY**

### Self Hosted Git Servers

The following are two good examples of self hosted git servers that could be used as a free alternative to github.  They also both can be run using docker which makes deployment very easy.
* https://gogs.io/  

* https://gitea.io/en-us/


### SSH Server as Remote Git Server
We are assuming you already have git installed locally and have already done an ssh-keygen etc.  For the purpose of this exercise I presume you have a user vagrant@remote.server and you use your id_rsa key to login to remote.server.

If not then add your key by logging in with a password:
```
cat ~/.ssh/id_rsa.pub | ssh vagrant@remote.server "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"
```

Now we can do the git parts ...
```
# On your remote server install git
sudo apt-get install git-core
ssh vagrant@remote.server "mkdir -p /home/vagrant/repo/project1.git"
ssh vagrant@remote.server "cd /home/vagrant/repo/project1.git && git init --bare"
```

Now we make the same repo on the local machine:
```
mkdir -p /home/$USER/dev/project1
cd /home/$USER/dev/project1
git init
touch README.md
git add .
git commit -m "Initial Commit" -a
git remote add origin ssh://vagrant@remote.server/home/vagrant/repo/project1.git
git push --set-upstream origin master
```

You can test it our by removing your local copy and cloning from your new git server.

```
cd /home/$USER/dev
rm -rf project1/
git clone vagrant@remote.server:/home/vagrant/repo/project1.git
```

And that is it ...


---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.  