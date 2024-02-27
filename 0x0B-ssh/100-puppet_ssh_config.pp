# Puppet to configure local ssh client

exec { 'Puppet Configuration':
path    => '/usr/bin/:/bin',
command => 'echo -e "Host 100.25.34.201\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
