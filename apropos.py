#!/usr/bin/python
#-*- coding: utf-8 -*-

import gtk

class Apropos:

    def __init__(self):
        self.about = gtk.AboutDialog()
        self.about.set_program_name("Mon programme tricot")
        self.about.set_version("0.1")
        self.about.set_copyright("CC-by-SA Nolwenn Lavielle")
        self.about.set_comments('''Mon programme tricot est un programme simple vous permettant de calculer rapidement les différentes longueurs pour vos mesures de tricot.''')
        self.about.run()
        self.about.destroy()
