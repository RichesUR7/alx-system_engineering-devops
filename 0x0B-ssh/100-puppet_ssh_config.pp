# This Puppet manifest configures the SSH client.
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '  IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '  PasswordAuthentication no',
}
