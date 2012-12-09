#!/usr/bin/python

import gtk
from menu import Menu
from apropos import Apropos
from nouveau import Echarpe

class MainWindow:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Mon programme tricot")
        self.window.set_size_request(600, 440)
        self.window.set_position(gtk.WIN_POS_CENTER)

        mb = Menu()

        mb.echarpe().connect("activate", self.echarpe)

        mb.quit_menu().connect("activate", gtk.main_quit)

        mb.apropos().connect("activate", self.apropos)

        self.vbox = gtk.VBox(False, 2)
        self.vbox.pack_start(mb.get(), False, False, 0)
        self.window.add(self.vbox)
        
        self.window.connect("destroy", gtk.main_quit)
        self.window.show_all()

    def echarpe(self, obj):
        self.w_ech = Echarpe()
        self.vbox.pack_start(self.w_ech.get(), False, False, 0)
        
    def apropos(self, obj):
        Apropos()

MainWindow()
gtk.main()
