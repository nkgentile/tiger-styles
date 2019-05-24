#!/bin/bash
export PROJ_ROOT=/home/ec2-user/pur-draft
export MODELDIR=$PROJ_ROOT/xform
export PYTHONPATH=$PROJ_ROOT:$PROJ_ROOT/xform:$PROJ_ROOT/tools:$PROJ_ROOT/xform/src
cd $PROJ_ROOT
#<---for local run block; uncomment below 3 lines -->
#python3 -m venv py35_env
#source py35_env/bin/activate
#flask run

#<-- AWS setup block ---->
#run below commands before entering virtual env -
#sudo vi /etc/nginx/nginx.conf
#inside http block in above file add 'server_names_hash_bucket_size 128;'

#<-- change nginx conf below to redirect local traffic to public DNS -->
#sudo vi /etc/nginx/conf.d/virtual.conf
#add below lines
#server {
#    listen       80;
#    server_name  your_public_dnsname_here;
#
#    location / {
#        proxy_pass http://127.0.0.1:8000;
#    }
#}
#sudo /etc/rc.d/init.d/nginx start

#<-- Below block to turn the website on -->
# -- Notice that we are using gunicorn as its prod ready
#TODO - need to secure the website AWS doesn't render it without ctfkt
#python3 -m venv py35_env
#source py35_env/bin/activate
#add .env contents
#gunicorn app:app -b localhost:8000 &

echo "Ready to rumble .. set env contents and kick off the run"
