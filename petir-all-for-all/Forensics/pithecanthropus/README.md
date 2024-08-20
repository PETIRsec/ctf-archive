# Pithecanthropus

A provided web log is showing a blind SQL injection time-based attack. In this attack, the web application delays respond based on the SQL query's success.

To extract data from the log, split the log to get the ASCII codes from each entries when the time difference is 3 seconds or more, or if the ASCII code resets to 0.