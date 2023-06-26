#A puppet file to make changes to a configuration file
class mymodule::config_file {
  file { '2-ssh_config':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('mymodule/config_file.erb'),
  }
  privte_key = '~/.ssh/school'
}

