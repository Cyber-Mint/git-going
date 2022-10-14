# GIT

## 2005, April 7th

When Linus Torvalds made his initial commit of Git's code on April 7th 2005, he supplied the commit message:

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

## Before GIT

Version Control Systems before `git` came along were typically centralised systems into which you checked in and checked our your code.  Over the past several decades there have been many [popular source code versioning systems](https://www.softwaretestinghelp.com/version-control-software/) and they generally fall into two types, centralised and decentralised. 

Centralised SCV tend to be client-server and are loosely based on the idea that no two developers work on the same file at the same time.  This  requires every team to be synchronised and coordinated when checking in and checking out code.

> GIT is **decentralised**.



---
References:
* Centralised VCS Systems: [Microsoft Visual SourceSafe](https://en.wikipedia.org/wiki/Microsoft_Visual_SourceSafe), [SVN-Apache Subversion](https://subversion.apache.org/)
* Distributed VCS Systems: [mercurial](https://www.mercurial-scm.org/about), [git](https://github.com/git)