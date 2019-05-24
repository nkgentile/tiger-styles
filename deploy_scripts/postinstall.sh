#!/bin/bash

#at this time expect install by codedeploy has copied all foles to pur-draft folder
cd /home/ec2-user/pur-draft
export PROJ_ROOT=/home/ec2-user/pur-draft
export MODELDIR=$PROJ_ROOT/xform
export PYTHONPATH=$PROJ_ROOT:$PROJ_ROOT/xform:$PROJ_ROOT/tools:$PROJ_ROOT/xform/src
cd $PROJ_ROOT
python3 -m venv py35_env
source py35_env/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install gunicorn
