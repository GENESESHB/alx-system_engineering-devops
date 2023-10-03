# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to get the hostname of the server
Facter.add('custom_hostname') do
  setcode 'hostname'
end

# Configure Nginx to add custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  mode    => '0644',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}


