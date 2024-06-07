#!/bin/bash

# Function to check MySQL availability
wait_for_mysql() {
    until mysqladmin ping -h db --silent; do
        echo "Waiting for MySQL server to become available..."
        sleep 1
    done
    echo "MySQL server is available!"
}

# Call the function to wait for MySQL
wait_for_mysql

# Run the command passed to this script
exec "$@"
