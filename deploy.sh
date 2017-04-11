#!/bin/sh

ps -ef | grep python | awk '{print $2}' | xargs kill -9
cd /var/www/github_src
rm -rf zilong
git clone https://github.com/suibiangao/zilong.git
cp -rf /var/www/github_src/zilong /var/www/
cd ..
rm -rf zilong_new
mv zilong zilong_new
cp -rf /var/www/github_src/*.py /var/www/zilong_new
cd zilong_new
nohup python manager.py &
cd app/controler
nohup python service_json_A.py &
nohup python monitor.py &

