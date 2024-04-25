#!/bin/bash
# send a get request to given url and display response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
