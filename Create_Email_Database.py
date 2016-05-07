# This code takes a text file of emails, counts the number of times each email has been written, and writes it's count to a database
# Import library to talk to SQL database
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')			# Use database in application, and store it in "emaildb.sqlite"
cur = conn.cursor()									# Create cursor/connection to send commands

cur.execute('''
DROP TABLE IF EXISTS Counts''')						# Send a drop table

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')	# Create table called counts

# Familiar code
fname = raw_input('Enter file name: ')				# Ask user for filename
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)									# Open the file
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    print email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))	# ? = placeholder to be filled in, line ends in a tuple
	# First thing in tuple substitutes in for ?
	# Now, cursor has done rowselect
    row = cur.fetchone()							# Brings us back 1 row, and into memory, gives it back as a list
	# Should be count field from database
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) 
                VALUES ( ?, 1 )''', ( email, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', 
            (email, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()									# If doing things in memory in SQLite, write it back to disk

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'	# Order emails by count, and then only take top 10

# Code below prints out sqlstr
print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()											# Close the cursor
