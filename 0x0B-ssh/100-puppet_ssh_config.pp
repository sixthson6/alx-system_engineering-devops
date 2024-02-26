# Puppet to configure local ssh client

file_line { 'disble passwd auth':
ensure  => present,
line    => 'PassowordAuthentication no',
path    => '/etc/ssh/ssh_config',
match   => '^\s*#?\s*PasswordAuthentication'
}

file_line { 'use private key for auth'
ensure   => present,
line     => 'IdentifyFile ~/.ssh/school',
path     => '/etc/ssh/ssh_config',
match    => '^\s*#?\s*IdentifyFile ~/.ssh/school'
}
