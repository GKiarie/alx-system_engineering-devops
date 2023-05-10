# Using puppet to fix problem of Apache
# returning a 500 error

exec { 'Fixing_apache2':
    command => "sudo sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'"
    path => '/usr/local/bin/:/bin/'
}
