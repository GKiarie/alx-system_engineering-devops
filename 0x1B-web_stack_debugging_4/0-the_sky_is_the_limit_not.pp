# Puppet script that increases amt of traffic
# that an Nginx server can handle

exec {'upscale nginx traffic':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# restart nginx
exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/etc/init.d/'
}
