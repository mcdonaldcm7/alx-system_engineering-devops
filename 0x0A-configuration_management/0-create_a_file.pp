#Create a file with the given content in the given mode, e.t.c
file {'/tmp/school':
  ensure  => present,
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet',
  mode    => '0744'
}
