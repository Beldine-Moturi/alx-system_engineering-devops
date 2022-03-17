# configures the ssh config file

include stdlib
file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'password authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication yes',
}

file_line { 'use private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
}