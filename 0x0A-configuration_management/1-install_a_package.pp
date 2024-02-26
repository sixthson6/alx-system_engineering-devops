# This script installs flask using pip3

package { 'python3':
ensure  => 'installed'
}

package { 'python3-pip':
ensure  => 'installed'
}

package { 'werkzeug':
ensure   => '2.1.2',
provider => 'pip3'
}

package { 'flask':
ensure   => '2.1.0',
provider => 'pip3'
}
