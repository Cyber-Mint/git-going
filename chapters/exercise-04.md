# Exercise 4 - Advanced git

## Dealing with merge conflicts
* navigate to the repository that you created in excercises 1 and 2
* checkout a new branch and add a file `this_will_break.txt`
```bash
git checkout master
git pull
git checkout -b first_branch
touch this_will_break.txt
git add this_will_break.txt
git commit -m "Adding this_will_break.txt to repo on branch 1"
git checkout master
git checkout -b second_branch
touch this_will_break.txt
git add this_will_break.txt
git commit -m "Adding this_will_break.txt to repo on branch 2"
git merge first_branch
```

---
> Exercise Time: 60 Minutes
---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.