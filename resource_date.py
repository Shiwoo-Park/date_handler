#!/usr/bin/env python
#coding: utf8

# 안잡히는 문자열들
TIME_AGODATA= """
1분 ago
14초 전
1일 전
6개월 전
15일전
3달전
5 minutes ago
어제
28초 전 (2015.3.23 20:59)l
그제
그저께
엊그제
108명 읽음2개 덧글5 시간 전
한시간전
이주 전
ten minutes ago
11 일 전
"""

# 기존 예제들
TIME_DATEDATA ="""
2014 / 2 / 1
2013 - 01 - 24 16:38
13/02/22/15:41:12
PM 08:14
15:41:12
15:41
2014-3-1
Dec 2, 2014
2013.01.24
20130222

December 14 2014 at 5:46 pm
Mon 03 Feb 2014 19:01:00 -0500
Tue, 06 Aug 2013 06:42:22 +0000
Tue, 06 Aug 2013 PM 06:42:22 +0000
Mon 03 Feb 2014 19:01:00 -0500
2013/02/22 15:41:12
Tue Dec 30 2014 17:10:24 +0000
13-01-25 6:26
2013.01.25, 06:26 PM
2013-03-18[23:53]
13.01.24 16:38?:01
13.01.24 16:38
13.01.24 16 : 38
2013/11/18(21:44)
2013.01.24 16:38
2013-1-4 16 : 38
2013-01-24 (4:38:23) PM
2013.01.24 (16:38:23)
2013-01-24 (16:38:23)
12/11/2013 10:30:48 PM
2013.01.24 16:38:23
2013-01-24 16:38:23
2014-11-21T00:25:47+09:00
Mon 03 Feb 2014 19:01:00 -0500
13.01.25&nbsp;(금) 15:39
2013-01-25 (금) 15:39

10월 16, 2014
2013년 01월 28일 11시 11분
2013년 01월 28일 11시 11분 39초
2014년 1월 1일
2013-01-25 오후 6:26:37
2014년 12월 1일
2015/1/15 13:30
September 11, 2014 at 6:41 pm
입력 2015-03-13 14:53:32 | 조상현 csh@betanews.net
2013. 9. 29
입력 : 2015-03-16 21:20:52
[249호] 승인 2015.03.16 14:32:56
2015년03월11일 01시19분
By 레디앙 / 2015년 3월 17일, 3:32 PM
2015년03월18일 11시00분
데스크승인 [1325호] 2015.03.12 17:52:46(월)
울산/곽현 기자 , 2015-03-18 15:05:32
2015. 03.19
<무카스미디어 = 정길수 수습기자> (2015-03-17 오후 6:35)
June 18.2015
"""