# GIT

## 2005, April 7th

When [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) made his initial commit of Git's code on April 7th 2005, he supplied the commit message:

```
Initial revision of "git", the information manager from hell
```

In this commit, he included a file called README. The first paragraph in this file reads:

```
GIT - the stupid content tracker

"git" can mean anything, depending on your mood.

 - random three-letter combination that is pronounceable, and not 
   actually used by any common UNIX command.  The fact that it is a
   mispronunciation of "get" may or may not be relevant.
 - stupid. contemptible and despicable. simple. Take your pick from the 
   dictionary of slang.
 - "global information tracker": you're in a good mood, and it actually
   works for you. Angels sing, and a light suddenly fills the room. 
 - "goddamn idiotic truckload of sh*t": when it breaks

This is a stupid (but extremely fast) directory content manager.  It  
doesn't do a whole lot, but what it _does_ do is track directory
contents efficiently.
```

## Before GIT and why GIT

Version Control Systems before `git` came along were typically centralised systems into which you checked in and checked our your code.  Over the past several decades there have been many [popular source code versioning systems](https://www.softwaretestinghelp.com/version-control-software/) and they generally fall into two types, centralised and decentralised. 

Centralised SCV tend to be client-server and are loosely based on the idea that no two developers work on the same file at the same time.  This  requires every team to be synchronised and coordinated when checking in and checking out code.

> GIT is **decentralised**.

This means that the usage philosophy is completely different with `git`.  Each developer has a complete copy of the repository they are working on, on their own PC. At some time changes are merged from developers when git is used to push changes to a shared server.

Typically this shared server is [gitub](https://github.com) but it could be any git compatible shared server.

---
```Git was also created by Linus Torvalds in the process of developing Linux. Many people were involved in the development of Linux by making small or large contributions. 

After some time, it became really hard to manage and maintain all the changes and updates. That is the reason why Git was created.

Git is a version control system that maintains a history of all changes made to the code. Code changes are stored in a special database called a “repository”, also known as “repo”.

Two main advantages of using Git at software development:

    * Tracking the changes and updates. We are able to see who made which changes. 
      Git also provides when and why a change was made.
    * Allowing to work collaboratively. 
      Software development projects usually require many  people to work together.
      Git provides the developers with a systematic way of doing that.
      Thus, the developers focus on the project instead of extensive communication.

Git has become the globally preferred SCV tool because of it's:

    * Speed
    * Scalability, and
    * being free and open source
```

---
References:<br>
* [What is Git and Why is It So Important?](https://towardsdatascience.com/what-is-git-and-why-is-it-so-important-dce559b27833)
* Centralised VCS Systems: [Microsoft Visual SourceSafe](https://en.wikipedia.org/wiki/Microsoft_Visual_SourceSafe), [SVN-Apache Subversion](https://subversion.apache.org/)
* Distributed VCS Systems: [mercurial](https://www.mercurial-scm.org/about), [git](https://github.com/git)

---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.