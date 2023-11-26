# 1-install_a_package.pp

# Ensure the package is present and at the specified version
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify that the package installation is completed
notify { 'Flask installed':
  require => Package['Flask'],
}
