#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : rrd.py
# @Author: For lg224@foxmail.com
# @Date  : 9/28/17

###创建rrd
# !/usr/bin/python
import rrdtool

rrdb = rrdtool.create('rest.rrd', '--step', '60', '--start', '1369982786',
                      'DS:input:GAUGE:120:U:U',
                      'DS:output:GAUGE:120:U:U',
                      'RRA:LAST:0.5:1:600',
                      'RRA:AVERAGE:0.5:5:600',
                      'RRA:MAX:0.5:5:600',
                      'RRA:MIN:0.5:5:600')
if rrdb:
    print rrdtool.error()

