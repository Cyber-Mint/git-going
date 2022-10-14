# Advanced Git

## Run your own git server

We are assuming you already have git installed locally and have already done an ssh-keygen etc.  For the purpose of this exercise I presume you have a user vagrant@remote.server and you use your id_rsa key to login to remote.server.

If not then add your key by logging in with a password:
```
cat ~/.ssh/id_rsa.pub | ssh vagrant@remote.server "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"
```

Now we can do the git parts ...
```
# On your remote server install git
sudo apt-get install git-core
ssh vagrant@remote.server "mkdir -p /home/vagrant/repo/project1.git"
ssh vagrant@remote.server "cd /home/vagrant/repo/project1.git && git init --bare"
```

Now we make the same repo on the local machine:
```
mkdir -p /home/$USER/dev/project1
cd /home/$USER/dev/project1
git init
touch README.md
git add .
git commit -m "Initial Commit" -a
git remote add origin ssh://vagrant@remote.server/home/vagrant/repo/project1.git
git push --set-upstream origin master
```

You can test it our by removing your local copy and cloning from your new git server.

```
cd /home/$USER/dev
rm -rf project1/
git clone vagrant@remote.server:/home/vagrant/repo/project1.git
```

And that is it ...


---
[MIT Licensed](LICENSE) and prepared for Varsity College by [Cyber-Mint (Pty) Ltd](https://www.cyber-mint.com)<br>
[Teamfu](https://teamfu.tech) &trade; is a trademark of Cyber-Mint (Pty) Ltd.<br>
&copy; Copyright 2022, Cyber-Mint (Pty) Ltd.  