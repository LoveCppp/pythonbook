#coding:utf-8
import difflib
text1="""text1:
This modile provides classes and functions for compng sequerces.
including HTML and context and unified diffs.
diffilib document v7.4
add string
"""
text1_lines=text1.splitlines()
text2="""text2:
This module provides classes and functions for Comparing sequerces.
including HTML and  context and unified diffs.
difflib document v7.5"""
text2_lines=text2.splitlines()
#d=difflib.Differ()
#diff=d.compare(text1_lines,text2_lines)
#print '\n'.join(list(diff))

#create html
d=difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines)

