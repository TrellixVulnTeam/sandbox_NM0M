#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

con = lite.connect('test.db')
#con = None

with con:

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    cur.execute("CREATE TABLE CARS(ID INT, Name TEXT, Price REAL)")

    data = cur.fetchone()

    print "SQLite Version: %s" % data

