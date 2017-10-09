#! /usr/bin/bash
# auto run test bash
# 将 服务器在后台运行，并在bash 结束时 结束两个进程 server端需要
# cd $(dirname $0)
source activate py2
pip install -r requirements.txt
python ./HTTP-Server.py &
python ./HTTP-Client.py &

sleep 2s
echo "=================================================="
read -p "PRESS [ENTER] TO TERMINATE PROCESSES." PRESSKEY

kill $(jobs -p)
