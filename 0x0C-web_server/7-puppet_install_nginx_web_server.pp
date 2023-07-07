package { 'curl':
  ensure => installed,
}

package { 'wget':
  ensure => installed,
}

package { 'git':
  ensure => installed,
}

package { 'nginx':
  ensure => installed,
  require => Package['curl', 'wget', 'git'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('my_module/default.conf.erb'),
  require => Package['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}
