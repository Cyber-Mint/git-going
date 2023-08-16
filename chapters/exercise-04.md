# Exercise 4 - Advanced git

## Dealing with merge conflicts
* navigate to the repository that you created in excercises 1 and 2
* checkout a new branch and add a file `this_will_break.txt`
```bash
git checkout master
git pull
git checkout -b first_branch
touch this_will_break.txt
echo "The first line should be this" > this_will_break.txt
git add this_will_break.txt
git commit -m "Adding this_will_break.txt to repo on branch 1"
git checkout master
git checkout -b second_branch
touch this_will_break.txt
echo "No, the first line should be this" > this_will_break.txt
git add this_will_break.txt
git commit -m "Adding this_will_break.txt to repo on branch 2"
git merge first_branch
```
* this will briung up an error
```
Auto-merging this_will_break.txt
CONFLICT (add/add): Merge conflict in this_will_break.txt
Automatic merge failed; fix conflicts and then commit the result.
```
* open and edit the file
* The file should look something like this:
```bash
 <<<<<<< HEAD
No, the first line should be this
=======
The first line should be this
>>>>>>> first
```
* resolve the conflict:
  * If using vscode, you can choose which change to keep
  * If not, remove all the characters that you did not add, and decide what the file should say

---
> Exercise Time: 60 Minutes
---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.