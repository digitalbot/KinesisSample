#!python

import boto.kinesis

con = boto.kinesis.connect_to_region('ap-northeast-1')
res = con.create_stream('test', 1)
print res
