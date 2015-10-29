#!/usr/bin/env bash

temp_link="https://fastdl.mongodb.org/osx/"
temp_file="mongodb-osx-x86_64-3.0.7.tgz"
current_dir="`pwd`"
database_dir="/data/db"
full_db_path="$current_dir$database_dir"

function download() {
    echo "Downloading MongoDB"
    wget $temp_link$temp_file -P $current_dir
}
function unpack() {
    mkdir -p $current_dir/mongodb
    tar -zxvf $current_dir/$temp_file --directory mongodb --strip-components=1
    export PATH=$current_dir/mongodb/bin
}
function create_database() {
    mkdir -p $database_dir
    chmod +x $current_dir/$database_dir
    export PATH=$current_dir/$database_dir:$PATH
}
function logging() {
    local log_dir="nimbus_log"
    mkdir -p $current_dir/$log_dir
    export PATH=$current_dir/$log_dir:$PATH
}
function install() {
    export PATH=$current_dir:$PATH

    echo "Start Spider to get latest MongoDB version (latest.py)"
    echo "Downloading"
    echo "Unpacking"
    echo "Installing"
}

install