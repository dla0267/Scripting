Assignment 3: Log Analysis
Yuun Lim


A cookie = a 64-bit number (printed out in hexadecimal),
 represents a browser for the purposes of tracking behavior across the web.

A segment is denoted by 
an uppercase letter, followed by a decimal number, followed by an underscore, followed by a second decimal number. 
E.g. G07610_12083. It contains a set of cookies representing individuals with the characteristic behaviors of the segment.

To generate segments, features associated with each cookie are evaluated and the cookie is placed into 0 or more segments.

The segment evaluator generates log files showing the segments to which each cookie belongs, 
but the final product requires the cookies that belong to each segment.


Given the baseline and test-run log files of the integration test, generate a report of the following validation errors:

Segments that gained extra cookies (segements are not in the baseline cookies, but there are some segments in cookies for log.)
Segments that lost cookies  (segements are in the baseline, but not in just log)
Cookies assigned to extra segments (segments that appears more than one)
Cookies omitted from segments

A segment may have both extra cookies and missing cookies (different cookies!). Similarly, a cookie may be both assigned to extra segments and omitted from segments.


both files have differnet number of lines
log file has 1000013
baseline has 1000009