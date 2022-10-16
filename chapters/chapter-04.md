# Github best practices

* **branch names** - Naming your branches in a consist way such as using the project management tool `{ticket#}-{ticket-name}` means it is easy to do branch maintenance and reduces overall cognitive load for other developers.
* **repo README.md** - a must have, short and clear. Use a `docs/` folder for all other project documentation and hyperlink these in a meaningful way.
* **branch rules** - set up branch rules in github to enforce PRs on `master` and otehr important long lived branches, such as `BETA` or `development`.
* **PR rules** - set up rules to enforce at least one reviewer, preferably, two (a) code review by another developer and (b) sign off by tester
* **DELETE merged branches** - with teh exception of long-lived branches, all merged branches should be deleted.  Be careful when a merge must happen to both a `master` and for example a `BETA` branch, not to delete until both are merged correctly.
* **meaningful commit messages** - ensure that all commit messages are short but meaningful, to enable easy viewing of the git logs.
* **commit early & often.Push less often but at least once a day.** - this means you make you commits chewable size chunks and by pushing at least once a day, possibly twice, no other developer eneds to wait for you if teyd epend in some way on your branch.
* **always pull before pushing** - this ensures that your branch never diverges too far as to prevent it from being pushable. If you have local clashes with the git pull, try `git stash save && git pull && git stash pop`. 
* **burn it down** - periodically `rm -rf local-repo/` and re-clone to get a clean setup.
* **


---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.