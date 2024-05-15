# File: 0-the_sky_is_the_limit_not.pp
# Purpose: Increase the open file limit for the nginx

# Level up open file limit
exec { 'set-limit-to-4096':
  path    => '/bin',
  command => "sed -i 's/15/4096/' /etc/default/nginx"
}

# Reboot nginx
exec { 'reboot nginx':
  command => '/usr/sbin/service nginx restart'
}
