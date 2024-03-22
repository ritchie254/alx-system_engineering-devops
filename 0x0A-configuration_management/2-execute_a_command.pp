# executr a command
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin'
}
