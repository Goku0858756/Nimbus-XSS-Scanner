#!/usr/bin/env bash

prog="Nimbus"
config="config.sh"
pidfile="/../"

function start() {
    echo "start function"
    echo "starting Database in Background"
    # "$CURR/mongodb/bin/mongod --dbpath $FULL_DB_PATH --pidfilepath $CURR/mongodb.pid --logpath $CURR/log/mongodb.log --verbose" &
}
function stop() {
    echo "stop function"
}
function status() {
    echo "status function"
}
function restart() {
    echo "restart function"
}
function idle() {
    echo "idle function"
}
function backup() {
    # Backup /data/db
    # tar -cZf /var/my-backup.tgz /home/me/
    echo "Backup Nimbus Scanner"
}
function server {
    case $1 in
        start)
            start
            ;;
        stop)
            stop
            ;;
        status)
            status
            ;;
        restart)
            restart
            ;;
        idle)
            idle
            ;;
        *)
            service
    esac
}
function service() {
    echo -n "Nimbus XSS Scanner options are as follow < start | stop | restart | status | idle > "
    read option
    server $option
}

service