# Introduction to Git and CI/CD for Students and Lecturers

## Objectives:

-   Understand basic Git commands and principles.

-   Learn about source code management principles.

-   Build a simple Git Actions pipeline using open-source example
    > repositories.

-   Understand common Git workflows for teamwork.

-   Learn about resolving merge conflicts and other advanced Git topics.

-   Discuss best practices for managing a team using Git.

### Materials Needed:

-   Git installed on each student's computer

-   Access to an open-source example repository

-   Presentation slides or whiteboard for visual aids

## Lesson Outline:

### 1. Introduction to Git (20 minutes)

-   Explain what Git is and why it's important for version control.

    -   Git is a tool that tracks changes in code, allowing multiple
        > people to work on the same project without conflicts. It
        > stores versions of files, making it easy to revert to earlier
        > states if needed. Git's branching system enables developers to
        > work on features independently and merge changes seamlessly.
        > With remote repositories, developers can collaborate from
        > anywhere. Git promotes accountability by attributing changes
        > to specific users. It simplifies code reviews and ensures
        > project integrity. In summary, Git streamlines collaboration,
        > safeguards code, and enhances efficiency in software
        > development.

-   Discuss the basic Git workflow: add, commit, push, pull, fetch.

    -   The basic Git workflow revolves around five essential commands:
        > add, commit, push, pull, and fetch. Adding stages changes for
        > commit, specifying which modifications to include in the next
        > snapshot of the code. Committing records these changes into
        > the project's history, accompanied by a descriptive message.
        > Pushing uploads committed changes from the local repository to
        > a remote repository, ensuring that others can access and
        > collaborate on the codebase. Pulling retrieves changes from
        > the remote repository and merges them into the local
        > repository, keeping the codebase up to date. Fetching
        > retrieves changes from the remote repository without merging
        > them, providing an opportunity to review modifications before
        > incorporating them into the local codebase. Together, these
        > commands facilitate efficient collaboration, version control,
        > and synchronization in software development projects.

### 2. Basic Git Commands (30 minutes)

-   Distribute cheat sheets with simple Git commands.

-   Demonstrate how to add files to the staging area, commit changes,
    > push to remote repositories, and pull changes from remotes.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Add Files to Staging Area</th>
<th><p># Add a specific file to staging area</p>
<p>git add filename</p>
<p># Add all modified files to staging area</p>
<p>git add .</p></th>
</tr>
<tr class="odd">
<th>Commit Changes</th>
<th><p># Commit staged changes with a descriptive message</p>
<p>git commit -m "Commit message"</p></th>
</tr>
<tr class="header">
<th>Push to Remote Repository:</th>
<th><p># Push committed changes to a remote repository</p>
<p>git push origin branch_nam</p></th>
</tr>
<tr class="odd">
<th>Pull Changes from Remote:</th>
<th><p># Pull changes from a remote repository and merge into local branch</p>
<p>git pull origin branch_name</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Exercises 01 - Installation & basics

## Create Team Wiki Project

-   break into teams of not more than six (6) members per team!

-   each generate an RSA ssh-key called id_vc

-   one of the team members create a Public repository with a default
    > README.md file and a suitable .gitignore file from the available
    > templates and an appropriate LICENSE file for your team project

-   add the other team members to that public repo

-   each team member clone the newly created repo locally

-   each team member edit, add a small section to the README.md

-   each team member should include their github profile link at the
    > bottom of the section they added

-   each team member should successfully git push their changes to the
    > server.

-   use git log --graph --oneline --all or git log --graph to see the
    > commits pushed to your repo.

### 3. Git Flow and Source Code Management Principles

-   Introduce Git Flow as a branching model.

-   <img src="../images/basic-branching.png" style="width:6.26772in;height:4.05556in" />

-   Discuss source code management principles such as versioning,
    > branching strategies, and pull requests.

> Source code management principles encompass various practices that
> govern how code is managed, versioned, and collaborated on within a
> development team. Here's a breakdown of some key principles:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Principle</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th>Versioning</th>
<th>Systematically tracking changes to source code over time, enabling developers to understand the codebase's history, revert to previous states, and manage releases effectively. Uses schemes like Semantic Versioning (SemVer) with major, minor, and patch versions indicating the significance of changes.</th>
</tr>
<tr class="header">
<th><p>Branching</p>
<p>Strategies</p></th>
<th>Define how code changes are managed in separate branches within a repository, facilitating parallel development, experimentation, and code isolation. Examples include GitFlow with long-lived branches for feature development and release preparation, and GitHub Flow with short-lived feature branches.</th>
</tr>
<tr class="odd">
<th>Pull Requests</th>
<th>Mechanism for proposing and reviewing code changes before merging them into the main codebase. Encourages collaboration, code review, and quality assurance. Developers create branches, make commits, and open pull requests for feedback and approval before integration, ensuring code meets project standards.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Overall, these source code management principles promote collaboration,
transparency, and efficiency within development teams, enabling them to
maintain a high level of code quality, manage project timelines
effectively, and deliver reliable software products.

-   Show examples of branching strategies using visual aids or a
    > collaborative coding session.

-   GitHub Flow Branching Strategy:

GitHub Flow is a simpler and more continuous approach to branching,
commonly used with GitHub's pull request feature:

1.  Main Branch (e.g., main or master): Represents the production-ready
    > code.

2.  Feature Branches: Developers create short-lived branches for each
    > new feature or change. These branches are typically branched off
    > from main.

3.  Pull Requests: Once work is complete in a feature branch, developers
    > open a pull request to merge changes into main. This allows for
    > code review, discussion, and automated testing before merging.

4.  Merge to Main: After review and approval, changes are merged into
    > the main branch, making them available for deployment.

####  Git for Working in Teams 

-   Discuss branching strategies for team collaboration, including
    > feature branches, long-lived branches, and hotfixes.

-   Explain how to create pull requests and merge strategies.

-   Conduct a group activity where students simulate a team
    > collaboration scenario, including creating branches, making
    > changes, and merging pull requests.

.

Exercise - Git Branching, Merging, and Collaboration

Objective: Practise branching, merging, and collaboration workflows
using Git.

1.  Setup Project:

2.  One team member registers on teamfu.tech and creates a project
    > (e.g., "Team Wiki").

3.  Invite and add other team members to the project.

4.  Create Tickets:

5.  Add a sprint (e.g., "Sprint 02") and add tickets to this sprint.

6.  Include feature tickets for each team member to update/add a new
    > section.

7.  Add one hotfix ticket to add/replace the MIT LICENSE file.

8.  Branching and Changes:

9.  Each team member re-clones the "Team Wiki" repo.

10. Create a feature branch named after the assigned ticket number.

11. Make changes to the wiki as per the respective ticket.

12. Add, commit, and push these changes to the server.

13. Pull Requests and Reviews:

14. Create a pull request (PR) and assign it to another team member for
    > approval.

15. Ensure the branch is up to date with master before approving the PR.

16. Merging Workflow:

17. Merge one feature branch, then the hotfix, then the other feature
    > branches.

18. Review and merge each PR as a team.

19. Final State:

20. All feature branches merged into master.

21. Only master, correctly updated, remains.

### 4. Building a simple git action pipeline 

-   During this mention git actions workshop

-   Might show examples from gitea work flows ask andrew

# Exercise 4 - Git flow for Team work

-   In your repository on GitHub.com, create a workflow file called
    > github-actions-demo.yml in the .github/workflows directory. To do
    > this:

-   If the .github/workflows directory already exists, navigate to that
    > directory on GitHub, click Add file, then click Create new file,
    > and name the file github-actions-demo.yml.

-   If your repository doesn't have a .github/workflows directory, go to
    > the main page of the repository on GitHub, click Add file, then
    > click Create new file, and name the file
    > .github/workflows/github-actions-demo.yml. This creates the
    > .github and workflows directories and the github-actions-demo.yml
    > file in a single step.

```
name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v4
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```

```
git add .
git commit -m "Commit message"
git push
```
-   

### 5. Advanced Git Topics (30 minutes)

-   Cover Git log and Git stats for tracking changes and analyzing
    > project history.

-   Provide tips and tricks for resolving difficult merge conflicts.

-   Discuss when to reset the HEAD and other advanced source code
    > management topics.

-   Conduct a live demo of resolving merge conflicts using a sample
    > repository.

### 6. Best Practices in Git for Managing a Team (30 minutes)

-   Summarize best practices for managing a team using Git.

-   Encourage students to maintain clear documentation, follow naming
    > conventions, and adopt a consistent workflow.

-   Highlight the importance of code reviews, continuous integration,
    > and regular communication.

-   Facilitate a discussion on real-world scenarios and challenges in
    > team collaboration using Git.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><blockquote>
<p><strong>Clear Documentation and Naming Conventions:</strong> Encourage team members to maintain clear and consistent documentation for project structure, coding standards, and workflow guidelines. Establish naming conventions for branches, commits, and files to enhance clarity and organization within the repository.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Consistent Workflow Adoption:</strong> Standardize the team's Git workflow to ensure everyone follows the same process for branching, committing, and merging changes. Whether using GitFlow, GitHub Flow, or another model, consistency streamlines collaboration and reduces confusion.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Code Reviews</strong>: Emphasize the importance of code reviews as a quality assurance measure. Encourage team members to review each other's code before merging changes, providing feedback, identifying bugs, and sharing knowledge. Code reviews improve code quality, promote best practices, and foster learning within the team.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Continuous Integration (CI):</strong> Implement CI pipelines to automate the process of testing and integrating code changes into the main branch. CI systems, such as Jenkins, Travis CI, or GitHub Actions, automatically build, test, and validate code changes, ensuring that new features or bug fixes do not introduce regressions. This promotes stability and reliability in the codebase.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Regular Communication</strong>: Foster open communication among team members to discuss project progress, challenges, and decisions related to Git workflows. Encourage the use of collaboration tools, such as Slack, Microsoft Teams, or project management platforms, to facilitate discussions, share updates, and address issues promptly.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Version Control Etiquette:</strong> Teach team members to use Git responsibly, including committing atomic changes, writing meaningful commit messages, and avoiding unnecessary commits. Emphasize the importance of branching for feature development or bug fixes, minimizing disruptions to the main codebase.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Handling Merge Conflicts:</strong> Provide guidance on resolving merge conflicts effectively when multiple team members are working on the same files concurrently. Teach techniques for reviewing changes, communicating with team members, and resolving conflicts collaboratively to maintain code integrity.</p>
</blockquote></li>
<li><blockquote>
<p><strong>Backup and Disaster Recovery:</strong> Educate team members on the importance of regular backups and disaster recovery plans for Git repositories. Implement strategies for backing up repositories, storing them securely, and ensuring redundancy to prevent data loss in case of accidents or system failures.</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
