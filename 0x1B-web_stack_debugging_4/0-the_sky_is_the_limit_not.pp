# fixes nginx failes requests by increasing the ulimit value
exec { 'modify_file':
  command => "sed -i 's|ULIMIT=\"-n ..\"|ULIMIT=\"-n 2000\"|g' /etc/default/nginx",
  path    => '/bin',
  notify  => Exec['Restart'],
}

exec { 'Restart':
  command     => 'service nginx restart',
  path        => '/usr/bin',
  refreshonly => true,
}
