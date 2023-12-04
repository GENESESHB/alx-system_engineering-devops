# A Puppet manifest to install and configure Nginx.

$str = "add_header X-Served-By ${hostname};"

exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

-> package {'nginx':
  ensure => 'present',
}

-> file_line { 'X-Served-By':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'index yasin.html index.html index.nginx-debian.html;',
  line   => $str,
}

-> exec { 'restart':
  command => 'sudo service nginx restart',
  provider => shell,
}
