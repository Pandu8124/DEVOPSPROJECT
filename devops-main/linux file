Linux Command Cheatsheet
========================

# Linux Keyboard shortcuts
open terminal: Ctrl+Alt+T

*Ctrl + C* is used to kill a process with signal SIGINT , in other words it is a polite kill .

*Ctrl + Z* is used to suspend a process by sending it the signal SIGTSTP , which is like a sleep signal, that can be undone and the process can be resumed again.

*Ctrl+D*: log out of current session, similar to exit.

`history | grep "command looking for"`
* Ctrl+R – type to bring up a recent command
* !! - repeats the last command
* exit – log out of current session

 * fg in the foreground or bg in the background
 * Ctrl+W – erases one word in the current line
 * Ctrl+U – erases the whole line

# Password
Change password for user

    passwd user

# User and group

    sudo groupadd ic-api
    sudo usermod -g ic-api ic-api

# SSH 

[miranda-zhang/ssh.md](https://gist.github.com/miranda-zhang/74a2e1c5888b69f170792a107cd67011)

# Searching:

## Find

    find . -type f -name "*.conf"

## Grep
Example:

    grep -lr 'gceu' .

`grep` pattern dir - Search for pattern in dir.

Flags:
    
`-l` (or `--files-with-matches`) option is used to only print filenames of matching files, and not the matching lines (this could also improve the speed, given that grep stop reading a file at first match with this option).

`-r` recursive 

`-i` ignore-case 

`--include` search only files that match the file pattern  

    grep -ril --include \*.py --include \*.html ".id" 

 * command | grep pattern – search for pattern in the output of command

[More about regex](https://gist.github.com/miranda-zhang/127ff89ca8737cdb9dac404955f7f34c).

### Grep OR
https://www.thegeekstuff.com/2011/10/grep-or-and-not-operators/

    grep 'pattern1\|pattern2' filename
    grep -E 'pattern1|pattern2' filename

### Grep before after

    grep -B 4 -A 4 

# Locate 
Find all instances of file

    locate file

# System Info:

 * cal – show this month's calendar
 * uptime – show current uptime
 * w – display who is online
 * whoami – who you are logged in as
 * finger user – display information about user
 * htop - a lightweight text-mode process viewer packed with handy features such as killing processes without entering their PID, displaying full command lines, etc with a colour display

## OS Version
Show kernel information

    uname -a

Ubuntu

    lsb_release -a

CentOS

    hostnamectl
http://whatsmyos.com

## Cpu information

    cat /proc/cpuinfo

Show number of cores only

    grep -c ^processor /proc/cpuinfo

https://stackoverflow.com/questions/6481005/how-to-obtain-the-number-of-cpus-cores-in-linux-from-the-command-line

## Memory information

    cat /proc/meminfo

Show memory and swap usage, show output in gigabytes.

    free -g

## date time
Show the current date and time, in the format of: date+"T"+hour+minute+second+UTC time zone offset

    $ date +"%FT%H%M%S%z"
    2019-02-19T104943+1100

https://www.cyberciti.biz/faq/linux-display-date-and-time/

## Disk

    df -h

show disk usage with human readable unit.

    du -h --max-depth=1

show directory space usage, only one level deep.
## IP

    ip a 

One line command to just grep the ip:

    ip a | grep "scope global" | grep -Po '(?<=inet )[\d.]+'

For older version of centOS:

    ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}'

# Port and socket

CentOS older

`netstat`  - Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships

`-a, --all` Show  both  listening  and  non-listening (for TCP this means established connections) sockets.  With the --interfaces option, show interfaces that are not up

`--numeric , -n` Show numerical addresses instead of trying to determine symbolic host, port or user names.

`-p, --program` Show the PID and name of the program to which each socket belongs.

    netstat -anp | grep :8
https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s1-server-ports.html

CentOS 7 netstat, which is part of the package net-tools has been officially
**deprecated**, so you should be using `ss` (part of the package `iproute2`),
going forward.

    ss -anp | grep :8443

https://unix.stackexchange.com/a/385500/36816

    ss -lnpt 'sport = :3000'

`-l, --listening` Display only listening sockets (omitted by default).

`-n, --numeric` Do not try to resolve service names.

`-p, --processes` Show process using socket.

`-t, --tcp` Display TCP sockets.

https://unix.stackexchange.com/questions/106561/finding-the-pid-of-the-process-using-a-specific-port

# log

    journalctl -u nginx.service --since today
https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs

# Environment variables

[Ubuntu doc](https://help.ubuntu.com/community/EnvironmentVariables)

## Prints the names and values of all currently defined environment variables

    printenv 

## Examine the value of a particular variable

    printenv DBPASS

or

    echo $TERM

## Dollar sign

The dollar sign `$` can actually be used to combine the values of environment variables in many shell commands. For example, the following command can be used to list the contents of the "Desktop" directory within the current user's home directory. 

    ls $HOME/Desktop

## System wide environment variables

Add var into this file:

    sudo -H nano /etc/environment

It's important to do exact the way above, and not as the root user,
as it may cause problems like
[unable to login](https://askubuntu.com/questions/994127/cant-login-ubuntu-but-can-ssh-to-it). 
If you use normal sudo to start graphical applications
(including editors e.g. gedit), sometimes it results in the
configuration files being owned by root,
[read more about it here](https://askubuntu.com/questions/270006/why-should-users-never-use-normal-sudo-to-start-graphical-applications).

The only time the file is read is on login, when the PAM stack is activated – specifically pam_env.so, which reads the file.

Logging out and back in would apply the changes – and in fact you must do this if you want all your processes to receive the new environment. 
[All other solutions](https://superuser.com/questions/339617/how-to-reload-etc-environment-without-rebooting)
will only apply the environment to the single shell process, but not to anything you launch through the GUI including new terminal windows.

# App info

    which app
show which app will be run by default

    man command
show the manual for command

 * whereis app – show possible locations of app

# Bash Shell Script

`miranda-zhang/bash.md`
https://gist.github.com/miranda-zhang/9871f934edbb87a23c11185b85e191be

# File Commands:

 * cd dir - change directory to dir
 * cd – change to home
 * pwd – show current directory
 * mkdir dir – create a directory dir
 * rm file – delete file
 * rm -r dir – delete directory dir
 * rm -f file – force remove file
 * rm -rf dir – force remove directory dir *
 * cp file1 file2 – copy file1 to file2
 * cp -r dir1 dir2 – copy dir1 to dir2; create dir2 if it doesn't exist
 * mv file1 file2 – rename or move file1 to file2 if file2 is an existing directory, moves file1 into directory file2
 * touch file – create or update file
 * cat > file – places standard input into file
 * more file – output the contents of file
 * head file – output the first 10 lines of file
 * tail file – output the last 10 lines of file
 * tail -f file – output the contents of file as it grows, starting with the last 10 lines 

## GUI file manager

    xdg-open .

https://askubuntu.com/a/31196/202823

## Directory listing:

show hidden files with`-a`, show details with `-l`

    ls -al 

Determine file type, i.e. check if somthing is a symbolic link.
    
    file

Counting Files in the Current Directory

    ls -1 | wc -l
This uses wc to do a count of the number of lines (-l) in the output of ls -1. 
http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x700.html

## File Permissions
 * chmod octal file – change the permissions of file to octal, which can be found separately for user, group, and world by adding:
 * 4 – read (r)
 * 2 – write (w)
 * 1 – execute (x)

 Examples:
 * chmod 777 – read, write, execute for all
 * chmod 755 – rwx for owner, rx for group and world

## Compression
 * tar cf file.tar files – create a tar named file.tar containing files
 * tar xf file.tar – extract the files from file.tar
 * tar czf file.tar.gz files – create a tar with Gzip compression
 * tar xzf file.tar.gz – extract a tar using Gzip
 * tar cjf file.tar.bz2 – create a tar with Bzip2 compression
 * tar xjf file.tar.bz2 – extract a tar using Bzip2
 * gzip file – compresses file and renames it to file.gz
 * gzip -d file.gz – decompresses file.gz back to file

# Process Management:
 * top – display all running processes
 * kill pid – kill process id pid
 * killall proc – kill all processes named proc *
 * bg – lists stopped or background jobs; resume a stopped job in the background
 * fg – brings the most recent job to foreground
 * fg n – brings job n to the foreground

## ps
Display your currently active processes
- https://unix.stackexchange.com/questions/163145/how-to-get-whole-command-line-from-a-process

Show full command including arguments.

    $ ps -p [PID] -o args

# Network:
 * ping host – ping host and output results
 * whois domain – get whois information for domain
 * dig domain – get DNS information for domain
 * dig -x host – reverse lookup host
 * wget file – download file
 * wget -c file – continue a stopped download

# Installation:

Debian

    dpkg -i pkg.deb

RPM

    rpm -Uvh pkg.rpm

CentOS

    yum install pkg

Ubuntu
    apt update
    apt upgrade
    apt install pkg

Node.js, Javascript package manager

    npm install

## Install from source:

 * ./configure
 * make
 * make install

# Audit
Possible log location
>/var/log/audit/audit.log

    grep "denied" /var/log/audit/audit.log

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sec-understanding_audit_log_files

# Plot
Graph with `gnuplot` interactively:

    apt update
    apt install gnuplot-x11
    gnuplot

```gnuplot
# SET TERMINAL
set term gif
set output 'frequency.gif'
# set title "Word Frequency"

# Axes label
# set xlabel "Words"
# set ylabel "Frequency"

set xtics rotate by -90

plot "frequency.dat" using 1:xticlabels(2) with boxes
```

# Symlink
 https://shapeshed.com/unix-ln/#how-to-create-a-symbolic-link
 
 Create symbolic link link to file

    ln -s source_file link

Without `-s`, then create hard link.
