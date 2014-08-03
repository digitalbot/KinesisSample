#!/bin/sh
aws kinesis put-record --stream-name test --data $(date +%Y%m%d%H%M%S) --partition-key key1
