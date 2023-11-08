# Puppet script that automates the fixing of bad extension '.phpp' to '.php' in the WordPress site file 'wp-settings.php'

exec { 'Fix-WordPress-site-settings':
  command => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider=> shell,
}
