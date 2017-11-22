Project description: Performs queries on news database to determine which author is most popular, which article is most popular, and which days has greater than 1% of failed access attempts. Uses PostgreSQL, Python, Flask

Author: Faiga Revah

Date: November 2017

Files:logs_analysis.py- Flask/Python file that starts the server and requests data from logs_analysisdb
logs_analysisdb.py- Functions for database queries
templates (dir)- contains HTML template for webpage

**VIEWS**
For the file to work, user must create the following view:
CREATE VIEW status_table AS SELECT t1.date, not_found, ok FROM (SELECT date(time), count(*) AS not_found FROM log WHERE status = '404 NOT FOUND' GROUP BY date(time)) AS t1 JOIN (select date(time), count(*) AS ok FROM log WHERE status = '200 OK' GROUP BY date(time)) AS t2 ON t1.date = t2.date GROUP BY t1.date, t1.not_found, t2.ok; 

To run the program: -clone the repository into a directory in your computer with command git clone https://github.com/FayeRevah/logs_analysis (note: must have downloaded news database) -Enter localhost:8000 in any web or mobile browser

Requirements: Working browser such as Chrome, Edge, Safari or Firefox
