### What Ansible

1.IT automation tool

2.configure systems

3.deploy software-部署软件

4.orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling update -编排-持续部署-0停机滚动更新

### Ansible's main goals

1.simplicity and ease-of-use 简单、易用

2.security and reliability 安全、可靠性

3.featuring a minimum of movie parts,usage of OpenSSH for transport

4.a language that is designed around auditability by humans-围绕着人们可审计性进行设计

5.Ansible manager machines in an agent-less manner 不需要安装代理

### Get Start

#### Remote Connection Information

《Before we get started,it is important to understand how to Asible communicates whit remote machines over the **SSH protocol**》



### Working with Command Line Tools

#### ansible

##### Synopsis

ansible <host-pattern> [options]

##### Common Options

1.--ask-vault-pass

​	ask for vault password

2.--become-method <BECOME_METHOD>

​	privilege escalation method to use (default=%default),use ansible-doc -y become -l to list 	valid

3.--become-user <BECOME_USER>

​	run operations as this user (default=root)

4.--list-hosts

​	outputs a list of matching hosts;does not execute anything else 列出匹配的主机列表,不会执行任何的操作

5.--playbok-dir <BASEDIR>

​	Since this tool does not use playbooks,use this as a subtitute playbook directory.This sets the relative path for many features including roles/groups_vars/ etc.

6.--private-key,--key-file

​	use this file to authenticate the connection

7.--scp-extra-args <SCP_EXTRA_ARGS>

​	specify extra agruments to pass to scp only(e.g. -l)

8.`--sftp-extra-args <SFTP_EXTRA_ARGS>`

​	specify extra arguments to pass to sftp only (e.g. -f, -l)

9.`--ssh-common-args <SSH_COMMON_ARGS>`

​	specify common arguments to pass to sftp/scp/ssh (e.g. ProxyCommand)

more <https://docs.ansible.com/ansible/latest/cli/ansible.html#id3>

#### ansible-config

##### Synopsis

```
ansible-config [dump|list|view] [--help] [options] [ansible.cfg]
```

##### Description 

Config command line class

##### Common Options

sites:<https://docs.ansible.com/ansible/latest/cli/ansible-config.html>

##### Actions

###### view

Displays the current config file  

###### list

list all current configs reading lib/constants.py and show env and config file setting names

###### dump

Shows the current settings,merges absible.cif if specified 如果指定，合并ansible.cfg文件

--only-changes

​	Only show configurations that have changed from the default  仅仅改变从默认中改变的配置



#### ansible-console

##### Synopsis

```
ansible-console [<host-pattern>] [options]
```

##### Description 

a REPL that allows for running ad-hoc task agsinst a chosen inventory(base on domonis' ansible-shell)    一 个REPL，允许针对选定的库存运行临时任务（基于dominis的'ansible-shell）。

##### Common Options

more <https://docs.ansible.com/ansible/latest/cli/ansible-console.html>

#### ansible-doc

##### Synopsis

```
ansible-doc [-l|-F|-s] [options] [-t <plugin type> ] [plugin]
```

##### Description

displays information on modules installed in Ansible libraries . It display a terse listing of plugins and their descriptions, provides a printout of their  DOCUMENTATION strings,and it can create a short “snippet” which can be pasted into a playbook.





