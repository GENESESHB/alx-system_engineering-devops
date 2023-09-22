# Ensure the package is present with the specified version
package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

