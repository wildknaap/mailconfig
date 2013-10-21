#!/usr/local/bin/python
#
# Mon Oct  7 16:32:13 CEST 2013 

import MySQLdb
import os
import sys


# vars
dbhost='localhost'
dbport=3306
dbmail='mail'
dbuser='dbuser'
dbpasswd='dbpasswd'


# create a connection to the database
db=MySQLdb.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbmail)  
cursor=db.cursor()


# functions

def error():
	print ''
	print '   Fatal error right in front of screen.'
	print ''

	return


def exit():
	print ''
	print '   You must have hit the wrong any key.'
	print ''	


def query_list_aliases():
	cursor.execute("""select mail,destination from aliases; """)		

	return
	

def list_aliases():
	query_list_aliases()
	listaliases=cursor.fetchall()
	print ''
	print '+-----------------------------------------------------------------+'	
	def1='Email alias'
        def2='POP account'
	print '| %-30s | %-30s |' % (def1,def2)
	print '+-----------------------------------------------------------------+'	
	for row in listaliases:
		emailalias=row[0]
		popaccount=row[1]
		print '| %-30s | %-30s |' % (emailalias,popaccount)		
	print '+-----------------------------------------------------------------+'
	print ''

	mainmenu()

	return	


def query_add_alias():
	cursor.execute("""insert into aliases (mail,destination) values (%s,%s); """, (emailalias,popaccount))	

	return


def add_alias():
	global emailalias
	global popaccount
	print ''
	print 'Add an email alias to POP account'
	print '-------------------------------------------------------------'
	print ''
	emailalias = raw_input('Email alias: ')
	popaccount = raw_input('POP account to add email alias to: ')

	query_add_alias()
	
	print ''
	print emailalias, 'has been added to', popaccount
	print '-------------------------------------------------------------'
	print ''

	mainmenu()
	
	return		


def query_remove_alias():
	cursor.execute("""delete from aliases where mail = %s; """, (emailalias))

	print 'Removed alias emailalias'	

	return


def remove_alias():
	global emailalias
	print ''
	print 'Remove an email alias of a POP account'
	print '-------------------------------------------------------------'
	print ''
	emailalias = raw_input('Email alias to remove: ')
	print ''
	removeyesno = raw_input('Are you sure to remove '+emailalias+' : [y/n]')
	if 'y' in removeyesno: query_remove_alias()
	elif 'n' in removeyesno: print 'Good choice!'
	else:
		error()
	print ''

	mainmenu()

	return


#def popbox_add():


#def popbox_remove():


def mainmenu():
	print ''
	print 'Hello and welcome to the virtual mailaccount managler for mysql' 
	print ''
	print '1. List all email aliases'
	print '2. Add an email alias'
	print '3. Remove an email alias'
	print '4. Exit'
	print ''
	selection = raw_input('   Select a number: ')
	print ''
	if '1' in selection: list_aliases()
	elif '2' in selection: add_alias()
	elif '3' in selection: remove_alias()
	elif '4' in selection: exit()
	else:
		error()
	return


# execute

mainmenu()

cursor.close()


# EOF
