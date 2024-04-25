#!/bin/bash
#un the URL, sends a request to URL,and displays size of body of response
curl -s "$1" | wc -c
