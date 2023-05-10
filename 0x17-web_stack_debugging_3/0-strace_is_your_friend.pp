# Using puppet to fix problem of Apache
# returning a 500 error

exec { 'fixing_apache':
    command => "sudo sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'"
    path    => ['/bin', '/usr/bin']
}
