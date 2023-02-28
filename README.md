# canonical-devskiller

### Troubleshoot interview

---

- Fix `sudo` command.

Error: `sudo` command is opening `top` application.

Check the location of `sudo` command, right location should be: `/usr/bin/sudo`
```bash
which sudo
# /usr/local/sbin/sudo
```

Remove the incorrect binary:
```bash
/usr/bin/sudo rm /usr/local/sbin/sudo
```

Logout and SSH again.
```bash
exit
ssh ubuntu@3.113.3.190
```

---


- Fix `apt-get` command.

Error: too many files open at the same time.

Check `fs.file-max` value:
```bash
sudo sysctl -a | grep file
```

Increase the max file limit:
```bash
# Set this to some large number
sudo sysctl -w fs.file-max=99999999999999
```

---

- Fix the Apache server ASAP

Check the apache2 service status:
```bash
systemctl status apache2
```

Check the logs:
```bash
journalctl -fu apache2
```

Go to apache2 logs folder:
```bash
cd /var/log/apache2
```

Check the extended file attributes:
```bash
lsattr
```

Remove imutable flag from all the files:
```bash
chattr -i *
```

