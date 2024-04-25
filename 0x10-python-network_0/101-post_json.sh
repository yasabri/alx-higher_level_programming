#!/bin/bash
# sends a josn POST request to give url with given josn file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
