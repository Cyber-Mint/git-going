# Git Overview
This a quick introduction to git and the common commands that you are most likely to need on a day-to-day basis.

## Git
Git is a distributed version control system widely used for software development projects.

[A useful introduction to git](https://guides.github.com/introduction/git-handbook/)

## Github Flow
The branching process that is followed on a git repository is known as a "flow". Flows are very important because the define how a team works together to build the code for a project.

We follow [Github flow](https://guides.github.com/introduction/flow/) which advocates a single long-lived branch. This keeps the repository very simple as we create a branch for features and merge them using a Pull Request (PR) when the feature is complete. PR's must be reviewed and approved by another team member before they can be merged. Once we have Continuous Integration (CI) pipelines in place these must pass before the PR can be approved. 

## Setting up git
You will need to setup a few things to get git working on your machine. 

If you have not already created an account on github, then [this guide will show you how to create an account.](https://docs.github.com/en/github/getting-started-with-github/signing-up-for-a-new-github-account)

If you don't have git installed locally, then [this guide will show you how to do this.](https://www.atlassian.com/git/tutorials/install-git)

### Generate SSH Keys
It is possible to download source code from a repository as a compressed zip file, or using HTTPS, or using SSH. 
In my experience SSH is the most stable and the most performant.
In order to use SSH, you must have an SSH key pair generated on your machine and you must associate the public key with your github account.
Here are the basic instructions:
```bash
ssh-keygen -t ed25519 -C "<your-email-address>"
```
We recommend an empty passphrase as this will speed up your git interactions. If you add a passphrase on Windows, every time you execute a git command you must enter in the SSH passphrase and this can quickly become onerous. 

The default location and filename for the generated private key is: `~/.ssh/ed25519`. The content of the public key (`~/.ssh/ed25519.pub`) must be copied to your clipboard.

On Ubuntu, you can use the following to copy the content of a the public key to your clipboard:
```bash
xclip -sel c < ~/.ssh/ed25519.pub
```

You then need to [open your account settings (SSH and GPG keys) on github](https://github.com/settings/keys).
Click the `New SSH Key` and enter a friendly name for the key. Paste the content of your key in the section titled `Key` and then click the `Add SSH Key` option.

To test that your key is working correctly, try to clone a repo. That is copy a repo from Github to your local machine.
E.g.
```bash
git clone git@github.com:Cyber-Mint/devops-bootcamp.git
```
Note that this will create a folder in the directory where you were before running the git clone command. In order to view the code, simply change into the newly created folder. 
```bash
cd devops-bootcamp
ls -l
```

You are now able to start working with git on your local machine.

[A useful guide to setting up SSH with github](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## Git Repositories
A git repository (or repo) is typically used to house a single project. Ideally, each repo should be able to be worked on independently from other repo's.

[Guide to creating a github repo](https://docs.github.com/en/github/getting-started-with-github/create-a-repo)

There are many public and open source repo's on GitHub and it is possible to fork these repo's and further develop the code yourself. Forking essentially creates a copy of the original github repo, but in your own GitHub account. Be aware of the license used on the source repository because it will affect what you are allowed to do with the code. 

[More about git forking](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

[More about Open Source Licenses](https://opensource.org/licenses)


## Common git commands
There are a number of user interfaces that wrap the commands used in the command line. It is always best to understand the underlying commands before using a UI tool as they often "group" git commands together in order to "hide complexity". Unfortunately, when things go wrong these UI tools often fall short when trying to resolve a problem.

### Setup commands
The following are typically used when setting up git on your system. As a minimum, you will need to setup the email address before you can use git locally. 

| Command | Description |
| ----------------- | ------------------ |
| `git config --global user.name "[name]"` | Sets the name you want attached to your commit transactions |
| `git config --global user.email "[email address]"` | Sets the email you want attached to your commit transactions |
| `git config --global color.ui auto` | Enables helpful colorization of command line output|


### Repo Initialization
In order to work with a repo locally, you must either initialize a directory as a git repo. Or you can clone a repository (using SSH) from the git server.

| Command | Description |
| ----------------- | ------------------ |
| `git init` | initialize an existing directory as a Git repository |
| `git clone [url]` | retrieve an entire repository from a hosted location via URL. Remember to use the ssh option for the url. |


### Branching
Each feature that we create or bug that we fix should be on a branch. The following commands all relate to git branches.

| Command | Description |
| ----------------- | ------------------ |
| `git branch [branch-name]` | Creates a new branch |
| `git checkout [branch-name]`| Switches to the specified branch and updates the working directory |
| `git checkout -b [new-branch-name]`| Uses the current branch to create a new branch with the given `new-branch-name` |
| `git merge [branch]` | Combines the specified branch’s history into the current branch. This is usually done in pull requests, but is an important Git operation. We recommend that your latest `main` branch is merged into your branch before creating a PR. |
| `git branch -d [branch-name]` | Deletes the specified branch |


### Synchronizing
| Command | Description |
| ----------------- | ------------------ |
| `git fetch --all` | Downloads all history from all of the remote tracking branches |
| `git merge` | Combines remote tracking branch into current local branch |
| `git push` | Uploads all local branch commits to GitHub |
| `git pull` | Updates your current local working branch with all new commits from the corresponding remote branch on GitHub. `git pull` is a combination of `git fetch` and `git merge` |


### Making Changes
The following commands relate to making changes to the code on your local machine.

| Command | Description |
| ----------------- | ------------------ |
| `git log` | Lists version history for the current branch |
| `git log --follow [file]` | Lists version history for a file, including renames |
| `git diff [first-branch]...[second-branch]` | Shows content differences between two branches |
| `git show [commit]` | Outputs metadata and content changes of the specified commit. Note that a commit is a hash of the changes, e.g. `9eae6848ac7e6be1154c258bc972137689c58fc7` but we can use the shorthand for this `9eae684` |
| `git add [file]` | Snapshots the file in preparation for versioning. It is possible to add all changes using `git add .` however this often leads to files being added that were not intended to be. Be sure that your `.gitignore` file is up to date if you plan to use this version of the command. |
| `git commit -m "[descriptive message]"` | Records file snapshots permanently in version history on your local machine. In order to publish your changes to the server, you must follow this command with a `git push` |


### .gitignore file
This file is used to describe file patterns that should be ignored by git. The file is usually placed in the root of the repository. Files that match the patterns described in this file will not be added to the git repo. 

If you need to add a file that is ignored by default, it is possible to "force add" the file. For example, if configuration files `.config` are ignored by default and you want to add `develop.config` to your repo, you can use the following:
```bash
git add -f develop.config
```

### Undoing mistakes
Mistakes happen to all of us. The following commands describe common undo commands for git:

| Command | Description |
| ----------------- | ------------------ |
| `git reset [commit]` | Undoes all commits after `[commit]`, preserving changes locally |
| `git reset --hard [commit]` | Discards all history and changes back to the specified commit |

---

### References
* [Atlassian git cheatsheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)
* [Another git cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf)

---

> [Home](../README.md) | [Chapter 1](chapter-01.md)| Chapter 2 | Chapter 3 | Exercises 1 | Exercises 2 | 

---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
TeamFu &trade; is trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2020, Cyber-Mint (Pty) Ltd.  
