#This script is used to install Nginx

#!/bin/bash
sudo apt update
sudo apt install nginx -y

sudo systemctl enable nginx
sudo systemctl start nginx

sudo systemctl status nginx --no-pager
echo "Nginx install successfully"
