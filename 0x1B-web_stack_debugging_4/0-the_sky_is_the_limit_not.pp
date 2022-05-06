# fixes nginx faile requests by increasing ulimit
exec { 'increase ulimit':
  command => "sed -i 's|ULIMIT=\"-n ..\"|ULIMIT=\"-n 2000\"|g' /etc/default/nginx",
  path    => '/bin',
  notify  => Exec['Restart'],
}

exec { 'restart nginx':
  command     => 'service nginx restart',
  path        => '/usr/bin',
  refreshonly => true,
}