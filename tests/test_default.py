import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_sysctl_file(File):
    sysctl = File('/etc/sysctl.conf')

    assert sysctl.contains("net.ipv6.conf.all.disable_ipv6\=1")
    assert sysctl.contains("net.ipv6.conf.default.disable_ipv6\=1")


def test_sysctl(Sysctl):
    sysctl1 = Sysctl('net.ipv6.conf.all.disable_ipv6')
    sysctl2 = Sysctl('net.ipv6.conf.default.disable_ipv6')

    assert sysctl1 == 1
    assert sysctl2 == 1
