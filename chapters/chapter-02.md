# Git concepts explained

## Under the hood
When you create a new project and initialize a Git repo using `git init`, a hiden folder is created called `.git` which has all the git magic inside.

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

In addition to the `.git` folder we may add a `.gitignore` to list the files and file patterns we don't want Git to track while working in this folder.  Github has some best practice examples of `.gitignore` files here: `https://github.com/github/gitignore`


---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.  