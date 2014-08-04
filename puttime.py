#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto.kinesis,datetime,time

con = boto.kinesis.connect_to_region('ap-northeast-1')
print("connected\n")
stream_name = 'test'
partition_key = 'key1'
sampledate = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#sampledate = 'hogehoge'

print(sampledate)
put_data = con.put_record(stream_name, sampledate, partition_key)
print(put_data)
time.sleep(1)
print("ok\n")
