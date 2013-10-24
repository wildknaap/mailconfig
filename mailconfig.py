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


def query_list_popbox():
	cursor.execute("""select name, maildir from users;""")
	
	return


def list_popbox():
	query_list_popbox()
	listpopboxes=cursor.fetchall()
        print ''
        print '+-----------------------------------------------------------------+'
        def1='POP account'
        def2='Mail directory'
        print '| %-30s | %-30s |' % (def1,def2)
        print '+-----------------------------------------------------------------+'
        for row in listpopboxes:
                popbox=row[0]
                maildir=row[1]
                print '| %-30s | %-30s |' % (popbox,maildir)
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

	print 'Removed alias '+emailalias+''	

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


def query_add_popbox():
	cursor.execute("""insert into users (id,name,maildir,crypt) values (%s,%s,%s,encrypt(%s));""", (id,name,maildir,password))

	return


def add_popbox():
	global id
	global name
	global maildir
	global password
	print ''
	print 'Add a POP account'
	print '-------------------------------------------------------------'
	print ''
	name = raw_input('POP account to add: ')
	password = raw_input('Password: ')
	maildir = ''+name+'/'
	id = name
	print ''
	correctyesno = raw_input('POP account '+name+' correct? [y/n]')
	if 'y' in correctyesno: query_add_popbox() 
	elif 'n' in correctyesno: print 'Goodbye and thank you!'
	else:
		error()
	print ''
	
	mainmenu()		

	return
	

def query_remove_popbox():
	cursor.execute("""delete from users where name = %s;""", (popbox))

	print 'Removed POP account '+popbox+''
	
	return 	


def remove_popbox():
	global popbox
        print ''
        print 'Remove a POP account'
        print '-------------------------------------------------------------'
        print ''
        popbox = raw_input('POP account to remove: ')
        print ''
        removeyesno = raw_input('Are you sure to remove '+popbox+' : [y/n]')
        if 'y' in removeyesno: query_remove_popbox()
        elif 'n' in removeyesno: print 'Good choice!'
        else:
                error()
        print ''

        mainmenu()

        return	


def mainmenu():
	print ''
	print 'Hello and welcome to the virtual mailaccount managler for mysql' 
	print ''
	print '1. List all email aliases'
	print '2. Add an email alias'
	print '3. Remove an email alias'
	print '4. List all pop boxes'
	print '5. Add a POP account'
	print '6. Remove a POP account'
	print '7. Exit'
	print ''
	selection = raw_input('   Select a number: ')
	print ''
	if '1' in selection: list_aliases()
	elif '2' in selection: add_alias()
	elif '3' in selection: remove_alias()
	elif '4' in selection: list_popbox()
	elif '5' in selection: add_popbox()
	elif '6' in selection: remove_popbox()
	elif '7' in selection: exit()
	else:
		error()
	return


# execute

mainmenu()

cursor.close()


# EOF
