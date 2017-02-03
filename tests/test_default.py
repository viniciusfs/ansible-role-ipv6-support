import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_ipv6_support(File):
    sysctl = File('/etc/sysctl.conf')

    assert sysctl.contains("net.ipv6.conf.all.disable_ipv6\=0")
    assert sysctl.contains("net.ipv6.conf.default.disable_ipv6\=0")
