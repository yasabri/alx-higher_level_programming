#!/bin/bash
#takes in a URL as argument sends a get request to URL and displays body of response
curl -sH "X-School-User-Id: 98" "$1"
