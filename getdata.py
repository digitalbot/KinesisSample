#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto.kinesis,datetime,time

con = boto.kinesis.connect_to_region('ap-northeast-1')
stream_name = 'test'

stream = con.describe_stream(stream_name)
shards =  stream['StreamDescription']['Shards'][0]['ShardId']

itr = con.get_shard_iterator(stream_name, shards, 'LATEST')

next_itr = itr['ShardIterator']
while True:
    res = con.get_records(next_itr, limit=1)
    print res['Records']
    next_itr = res['NextShardIterator']
    time.sleep(1)
