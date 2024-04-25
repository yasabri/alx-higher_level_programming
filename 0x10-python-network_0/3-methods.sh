#!/bin/bash
# in a URL and displays all HTTP the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
