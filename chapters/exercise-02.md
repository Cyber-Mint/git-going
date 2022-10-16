# Exercise 2 - Branching & Merging

## Branching

* create two or three branches, one by each team member as follows `git checkout -b 001-update-README.md`
* each team member makes a small change to the same section of the README.md file.
* add, commit and push these changes to the server
* all view the state of the repo branches on the github server
* create a PR for `001`, add another team member as an approver.
* once approved, merge on github into `master` and delete the `001` branch
* now view the state of the remaining repo branches on github.  The remaining branches should now be behind `master` as well as ahead of `master` meaning that (a) there are changes in `master` not in `002` and (b) there are changes in '002` not in master.

## Merging
* now the next team meber can `git checkout master` and `git pull` to ensure they have the latest version of master locally.  This is an important step to do BEFORE doing a local merge
* now `git checkout 002-update-README.md` 
* lets do a `git diff master` to see what is different between our version of the README.md and the version in the `master` branch
* then we are ready to merge `master` into `002` by doing a `git merge master`.  This may result merge conflicts if changes occur in the same place in the file - these will need to be resolved before a safe merge can be completed.
* the final state would be all feature branches merged into master and only master, correctly updated remains.

---
> Exercise Time: 30 Minutes


---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.