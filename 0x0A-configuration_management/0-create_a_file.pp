# puppet file resource type to print a string
file { '/tmp/school':
ensure  => 'file',
path    => '/tmp/school',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
