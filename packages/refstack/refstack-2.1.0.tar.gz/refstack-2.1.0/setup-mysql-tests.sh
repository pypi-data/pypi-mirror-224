#!/bin/bash -x

wait_for_line () {
    while read line
    do
        echo "$line" | grep -q "$1" && break
    done < "$2"
    # Read the fifo for ever otherwise process would block
    cat "$2" >/dev/null &
}

# insert sbin into path if it exists and isnt already there
echo $PATH | grep -q "/usr/sbin"

if [ $? -ne 0 ] && [ -d "/usr/sbin" ]; then
  echo "SBIN NOT IN PATH"
  export PATH="$PATH:/usr/sbin"
  echo "$PATH"
fi

# If test DB url is provided, run tests with it
if [[ "$REFSTACK_TEST_MYSQL_URL" ]]
then
    $*
    exit $?
fi

# Else setup mysql base for tests.
# Start MySQL process for tests
MYSQL_DATA=`mktemp -d /tmp/refstack-mysql-XXXXX`
ls -lshd ${MYSQL_DATA}
mkfifo ${MYSQL_DATA}/out
# On systems like Fedora here's where mysqld can be found
PATH=$PATH:/usr/libexec
MYSQL_SOCKET="/var/run/mysqld/mysqld.sock"
sudo chown -R mysql:mysql ${MYSQL_DATA}
mysqld --initialize-insecure --basedir=${MYSQL_DATA} --datadir=${MYSQL_DATA}/data --pid-file=${MYSQL_DATA}/mysql.pid --socket=${MYSQL_SOCKET}/ --skip-networking --skip-grant-tables &> ${MYSQL_DATA}/out &
# Wait for MySQL to start listening to connections
wait_for_line "mysqld: ready for connections." ${MYSQL_DATA}/out
sudo mysql -S ${MYSQL_SOCKET} -e 'set @@global.show_compatibility_56=ON;' > /dev/null 2>&1
sudo mysql -S ${MYSQL_SOCKET} -e 'CREATE DATABASE test;'
sudo mysql -S ${MYSQL_SOCKET} -e "CREATE USER 'refstack'@'localhost' IDENTIFIED BY 'ref_pass';"
sudo mysql -S ${MYSQL_SOCKET} -e "GRANT ALL PRIVILEGES ON test . * TO 'refstack'@'localhost';"
sudo mysql -S ${MYSQL_SOCKET} -e "FLUSH PRIVILEGES;"
export REFSTACK_TEST_MYSQL_URL="mysql+pymysql://refstack:ref_pass@localhost/test?unix_socket=${MYSQL_SOCKET}&charset=utf8"

# Yield execution to venv command
$*

# Cleanup after tests
ret=$?
kill $(jobs -p)
rm -rf "${MYSQL_DATA}"
exit $ret
