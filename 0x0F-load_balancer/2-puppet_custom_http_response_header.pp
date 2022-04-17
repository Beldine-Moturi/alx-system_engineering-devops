# installs and configures HAproxy load balancer on a brand new ubuntu machine

#update apt-get
exec { 'apt-get update':
  command => 'sudo apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# install nginx server
package { 'nginx':
  ensure => 'installed',
}

# adjust the firewall
exec { 'allow HTTP':
  command => 'sudo ufw allow HTTP',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# file permissions and ownership
exec { 'change file permissions':
  command => 'sudo chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# custom 404 page
# create custom 404 page
file { '/var/www/html/custom_404.html':
  content => "Ceci n'est pas une page\n",
}


# change index file
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Hello World!\n",
}

# configure nginx:
#   lsiten on port 80
#   redirect /redirect_me to 301
#   custom 404 page
#   custom response header
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
	listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
	add_header X-Served-By \$hostname;
        location / {
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /custom_404.html;
        location  /custom_404.html {
            internal;
        }
        location /redirect_me {
		  rewrite ^/redirect_me$ https://github.com/Beldine-Moturi permanent;
	}
}
",
}


# restart nginx
exec { 'restart nginx':
  command => 'sudo service nginx restart',
}

# start nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
