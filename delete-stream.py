#!python

import boto.kinesis

con = boto.kinesis.connect_to_region('ap-northeast-1')
res = con.delete_stream('test')
print res
