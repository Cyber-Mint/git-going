# Git under the hood


## Git uses a hidden folder
When you create a new project and initialize a Git repo using `git init`, a hidden folder is created called `.git` which has all the git magic inside.

```
andrew@catnip:~/dev/cm/git-going$ ll
total 28
drwxrwxr-x  5 andrew andrew 4096 Oct 14 14:06 ./
drwxrwxr-x 32 andrew andrew 4096 Oct 14 09:49 ../
drwxrwxr-x  2 andrew andrew 4096 Oct 14 14:02 chapters/
drwxrwxr-x  8 andrew andrew 4096 Oct 14 15:30 .git/
drwxrwxr-x  2 andrew andrew 4096 Oct 14 12:43 images/
-rw-rw-r--  1 andrew andrew 1076 Oct 14 14:07 LICENSE
-rw-rw-r--  1 andrew andrew  802 Oct 14 15:29 README.md
```


## How Git keeps track
Git uses a SHA (cryptographic hash) of each change/commit to keep track of these changes.  

* The  `.git/`  directory holds subdirectories for objects,  refs,  config,  index,  HEAD, and more.

* The `objects/` folder is where the three objects: commit, tree and blob are housed.  Each object gets its own sub folder.

* The `refs/` folder holds references to all of the objects in the directory.  Let's say you have some orphaned objects on branches that no longer exist.  You can go into this folder and prune them off of your branch.

* The `config/` folder contains all of your configurations including the credentials you use to connect to GitHub; your email and name that you used to configure your global config.

* The `HEAD` file is what contains the pointer or reference to your working directory or branch and its latest commit.

* The `index` file is for when you use "git add" to stage your files for a commit.  They leave the index file after the commit.

> NOTE: Git uses [Merkle Tree Hashing](https://ieee.nitk.ac.in/blog/merkle-trees-and-their-application-in-git/) to encrypt its files and make them tamper proof.

Reference: `https://matthew-brett.github.io/curious-git/git_object_types.html`




---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.  