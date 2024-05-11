# Debug error code 500 error when request using GET HTTP to Apache web server

exec {'replace_in_config_file':
	provider => shell,
	command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
