# User limit

exec { 'more limit hard':
  command  => "sed -i 's/holberton hard.*/holberton hard nofile 6000/' /etc/security/limits.conf",
  provider => 'shell',
}

exec { 'more limit soft':
  command  => "sed -i 's/holberton soft.*/holberton soft nofile 6000/' /etc/security/limits.conf",
  provider => 'shell',
}

