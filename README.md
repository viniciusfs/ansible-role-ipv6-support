# Ansible role: IPv6 Support

Configures IPv6 support in CentOS/RHEL systems.


## Role Variables

* `ipv6_enabled`:
    - Description: Enable service at boot time
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
