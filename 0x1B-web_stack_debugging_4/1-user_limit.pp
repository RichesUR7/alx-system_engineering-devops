# File: 1-user_limit.pp
# Purpose: Increase the open file limit for the 'holberton' user


# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/65535/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/65535/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
