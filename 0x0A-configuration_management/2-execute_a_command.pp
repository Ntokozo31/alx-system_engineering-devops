# create a manifest that kills a process named killmenow

exec { 'kill_killmenow':
  command   => '/usr/bin/pkill -f killmenow',
  path      => ['/usr/bin', '/usr/local/bin', '/bin'],
  logoutput => true,
  provider  => shell,
  unless    => '/usr/bin/pgrep -f killmenow',
}
