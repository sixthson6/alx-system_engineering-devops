# Puppet script to kill a process

exec { 'killmenow':
command  => 'pkill killmenow',
onlyif   => 'pgrep killmenow',
path     => '/home/vagrant/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
provider => 'posix'
}
