# This Puppet manifest installs the requirements for Flask using pip3.
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# This Puppet manifest installs Flask version 2.1.0 using pip3.
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['Werkzeug'],
}
