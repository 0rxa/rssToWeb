#!/bin/bash

curl -X POST -H 'application/xml' -F 'data=@feed.rss' 'http://localhost:8008/'
