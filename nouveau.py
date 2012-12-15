#!/usr/bin/python
#-*- coding: utf-8 -*-

import gtk

class Echarpe:

    def __init__(self):

	self.echarpe = gtk.VBox(False, 0)
	self.echarpe.set_border_width(5)
        
	frame_echan = gtk.Frame(u"Votre échantillon")

        echantillon = gtk.VBox(False, 0)
        
        label_ma = gtk.Label("Nombre de mailles : ")
        self.text_ma = gtk.Entry()
        label_cm = gtk.Label(u"Nombre de centimètres : ")
        self.text_cm = gtk.Entry()
        
        set_ma = gtk.HBox(False, 1)
        set_ma.pack_start(label_ma, False, False, 0)
        set_ma.pack_start(self.text_ma, False, False, 0)
        
        set_cm = gtk.HBox(False, 1)
        set_cm.pack_start(label_cm, False, False, 0)
        set_cm.pack_start(self.text_cm, False, False, 0)
        
        echantillon.pack_start(set_ma, False, False, 2)
        echantillon.pack_start(set_cm, False, False, 2)

	frame_echan.add(echantillon)
	
	self.echarpe.pack_start(frame_echan, False, False, 2)

	frame_mes = gtk.Frame(u"Vos mesures :")

	mesures = gtk.VBox(False, 0)

        label_lng = gtk.Label(u"Longueur en centimètres : ")
        self.text_lng = gtk.Entry()
        label_lrg = gtk.Label(u"Largeur en centimètres : ")
        self.text_lrg = gtk.Entry()

        set_lng = gtk.HBox(False, 1)
        set_lng.pack_start(label_lng, False, False, 0)
        set_lng.pack_start(self.text_lng, False, False, 0)

        set_lrg = gtk.HBox(False, 1)
        set_lrg.pack_start(label_lrg, False, False, 0)
        set_lrg.pack_start(self.text_lrg, False, False, 0)

        mesures.pack_start(set_lng, False, False, 2)
        mesures.pack_start(set_lrg, False, False, 2)

	frame_mes.add(mesures)
	self.echarpe.pack_start(frame_mes, False, False, 2)

        get_values = gtk.Button("Calculer")
        get_values.connect("clicked", self.calculer)

        self.echarpe.pack_start(get_values, False, False, 2)   

	frame_calc = gtk.Frame(u"Les mesures pour votre nouvelle écharpe :")

	calculs = gtk.VBox(False, 2)
        
        longueur = gtk.Label(u"Longueur : ")
        self.lng_cm = gtk.Label()
        self.lng_ma = gtk.Label()
        set_longueur = gtk.HBox(False, 1)
        set_longueur.pack_start(longueur, False, False, 2)
        set_longueur.pack_start(self.lng_cm, False, False, 2)
        set_longueur.pack_start(self.lng_ma, False, False, 2)
        calculs.pack_start(set_longueur, False, False, 2)

        largeur = gtk.Label(u"Largeur : ")
        self.lrg_cm = gtk.Label()
        self.lrg_ma = gtk.Label()

        set_largeur = gtk.HBox(False, 1)
        set_largeur.pack_start(largeur, False, False, 2)
        set_largeur.pack_start(self.lrg_cm, False, False, 2)
        set_largeur.pack_start(self.lrg_ma, False, False, 2)
        calculs.pack_start(set_largeur, False, False, 2)     

	frame_calc.add(calculs)
	self.echarpe.pack_start(frame_calc, False, False, 2)

	self.echarpe.show_all()
        
    def get(self):
        return self.echarpe

    def afficher(self, obj):
        print u"Votre échantillon fait",self.text_ma.get_text(),u"mailles pour",self.text_cm.get_text(),u"centimètres de long."

    def calculer(self, obj):
	if len(self.text_lng.get_text()) > 0 \
		and len(self.text_lrg.get_text()) > 0 \
		and len(self.text_ma.get_text()) > 0 \
		and len(self.text_cm.get_text()) > 0:
		try:
			float(self.text_lng.get_text())
		except ValueError:
			print u"La longueur doit être un nombre et peut être un flottant."
		try:
			float(self.text_lrg.get_text())
		except ValueError:
			print u"La largeur doit être un nombre et peut être un flottant."
		try:
			int(self.text_ma.get_text())
		except ValueError:
			print u"Le nombre de mailles doit être un nombre entier."
		try:
			float(self.text_cm.get_text())
		except ValueError:
			print u"Le nombre de centimètres doit être un nombre et peut être un flottant."
	        self.lng_cm.set_text(self.text_lng.get_text()+u" centimètres - ")
	        self.lng_ma.set_text(self.regle_de_trois(self.text_ma.get_text(), self.text_lng.get_text(), self.text_cm.get_text())+u" mailles")
        	self.lrg_cm.set_text(self.text_lrg.get_text()+u" centimètres - ")
	        self.lrg_ma.set_text(self.regle_de_trois(self.text_ma.get_text(), self.text_lrg.get_text(), self.text_cm.get_text())+u" mailles")

    def regle_de_trois(self, depart, fin, convertion):
        calcul = (int(depart)*int(fin))/int(convertion)
        return str(calcul)

