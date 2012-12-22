#!/usr/bin/python
#-*- coding: utf-8 -*-

import gtk

class Menu:

	def __init__(self):
		self.mb = gtk.MenuBar()
		''' tricot '''
		mb_file = gtk.Menu()
		mb_filem = gtk.MenuItem("Tricot")
		mb_filem.set_submenu(mb_file)

		nmb_new = gtk.Menu()

		nmb_newn = gtk.MenuItem("Nouveau...")
		nmb_newn.set_submenu(nmb_new)

		self.nmb_pull = gtk.MenuItem("Pull")
		self.nmb_debardeur = gtk.MenuItem(u'Débardeur')
		self.nmb_echarpe = gtk.MenuItem(u'Echarpe')

		nmb_new.append(self.nmb_pull)
		nmb_new.append(self.nmb_debardeur)
		nmb_new.append(self.nmb_echarpe)

		mb_file.append(nmb_newn)
	   
		self.mb_quit = gtk.MenuItem("Quitter")
		mb_file.append(self.mb_quit)

		''' aide '''
		mb_help = gtk.Menu()
		mb_aide = gtk.MenuItem("Aide")
		mb_aide.set_submenu(mb_help)

		self.mb_apropos = gtk.MenuItem("A propos")
		mb_help.append(self.mb_apropos)

		mb_manuel = gtk.MenuItem("Manuel")
		mb_manuel.connect("activate", self.manuel)
		mb_help.append(mb_manuel)

		self.mb.append(mb_filem)
		self.mb.append(mb_aide)

	def get(self):
		return self.mb

	def echarpe(self):
		return self.nmb_echarpe

	def quit_menu(self):
		return self.mb_quit

	def apropos(self):
		return self.mb_apropos
	
	def manuel(self, obj):
		print "Manuel utilisateur"
		print u'Prévoir la gestion des accents ?'
