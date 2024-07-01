# Ensure Python 3.8 is installed
package { 'python3.8':
  ensure   => 'installed',
  provider => 'apt',
}

# Ensure pip is installed for Python 3
package { 'python3-pip':
  ensure   => 'installed',
  provider => 'apt',
  require  => Package['python3.8'],  # Ensure pip is installed after Python 3.8
}

# Ensure Flask is installed using pip3
package { 'Flask':
  ensure   => '2.1.0',  # Correcting the version to 2.1.0 as per your requirements
  provider => 'pip3',
  require  => Package['python3-pip'],  # Ensure Flask is installed after pip
}

# Ensure Werkzeug is installed using pip3
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],  # Ensure Werkzeug is installed after Flask
}
