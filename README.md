# Ansible role: IPv6 Support

[![Build Status](https://travis-ci.org/viniciusfs/ansible-role-ipv6-support.svg?branch=master)](https://travis-ci.org/viniciusfs/ansible-role-ipv6-support)

Configures IPv6 support in CentOS/RHEL systems.


## Role Variables

* `ipv6_enabled`:
    - Description: Enables IPv6 support
    - Values: `True | False`
    - Default: `False`


## Example Playbook

    - hosts: servers
      roles:
        - { role: viniciusfs.ipv6-support }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
