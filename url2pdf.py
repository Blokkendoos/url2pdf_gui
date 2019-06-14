#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Save output from URL to a PDF file.
# A simpole front-end for the url2pdf command-line tool.
# url2pdf: https://github.com/rwelz/URL2PDF/releases/tag/6.2.6
#
# 2019-06-06 JvO
#

import wx
from url2pdf_gui import Url2pdfFrame
from pubsub import pub

import subprocess
import os.path
import xerox


class MyFrame(Url2pdfFrame):

    def __init__(self, *args, **kwds):
        Url2pdfFrame.__init__(self, *args, **kwds)

        size = self.GetSize()
        self.SetMinSize(size)

        self.url = ""
        self.landscape = False
        self.paginate = True
        self.print_background = True
        self.load_images = True
        self.save_path = ""

    # Properties

    @property
    def url(self):
        return self.text_ctrl_url.GetValue()

    @url.setter
    def url(self, value):
        self.text_ctrl_url.SetValue(value)

    @property
    def paginate(self):
        return self.checkbox_paginate.GetValue()

    @paginate.setter
    def paginate(self, value):
        self.checkbox_paginate.SetValue(value)
        self.sync_orientation()

    @property
    def enable_javascript(self):
        return self.checkbox_enable_javascript.GetValue()

    @enable_javascript.setter
    def enable_javascript(self, value):
        self.checkbox_enable_javascript.SetValue(value)

    @property
    def print_background(self):
        return self.checkbox_print_background.GetValue()

    @print_background.setter
    def print_background(self, value):
        self.checkbox_print_background.SetValue(value)

    @property
    def load_images(self):
        return self.checkbox_load_images.GetValue()

    @load_images.setter
    def load_images(self, value):
        self.checkbox_load_images.SetValue(value)

    @property
    def landscape(self):
        return self._landscape

    @landscape.setter
    def landscape(self, value):
        self._landscape = value

    @property
    def save_path(self):
        return self.ctrl_save_path.GetPath()

    @save_path.setter
    def save_path(self, value):
        self.ctrl_save_path.SetPath(value)

    # Event handlers

    def on_checkbox_paginate_clicked(self, event):
        self.sync_orientation()
        event.Skip()

    def sync_orientation(self):
        '''Orientation pertains to pagination only'''
        if self.paginate:
            self.button_orientation.Enable()
        else:
            self.button_orientation.Disable()

    def on_button_orientation_clicked(self, event):
        '''Toggle between landscape and portrait'''
        if self.landscape:
            self.landscape = False
            bmp = wx.Bitmap("./icons/orientation_portrait.png")
            self.button_orientation.SetBitmapLabel(bmp)
        else:
            self.landscape = True
            bmp = wx.Bitmap("./icons/orientation_landscape.png")
            self.button_orientation.SetBitmapLabel(bmp)
        event.Skip()

    def on_button_cancel_clicked(self, event):
        self.Close()
        event.Skip()

    def on_button_ok_clicked(self, event):
        if self.url == "":
            print('Please enter an URL first...')
        else:
            pub.sendMessage('confirmed_to_go')
            self.Close()
        event.Skip()


class MyApp(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        # use the clipboard content for the URL
        self.frame.url = xerox.paste()
        # https://stackoverflow.com/questions/32542703/how-to-find-a-folder-path-in-mac-os-x-using-python
        self.frame.save_path = os.path.expanduser("~/Desktop")

        # https://wiki.wxpython.org/WxLibPubSub
        pub.subscribe(self.do_url2pdf, 'confirmed_to_go')

        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

    def do_url2pdf(self):
        url = "--url=%s" % self.frame.url
        paginate = "--print-paginate=" + ("yes" if self.frame.paginate else "no")
        orientation = "--print-orientation=" + ("landscape" if self.frame.landscape else "portrait")
        print_background = "--print-background=" + ("yes" if self.frame.print_background else "no")
        load_images = "--load-images=" + ("yes" if self.frame.load_images else "no")
        enable_javascript = "--enable-javascript=" + ("yes" if self.frame.enable_javascript else "no")
        save_path = "--autosave-path=%s" % self.frame.save_path

        subprocess.call(["/opt/local/bin/url2pdf",
                         url,
                         paginate,
                         orientation,
                         print_background,
                         load_images,
                         enable_javascript,
                         save_path])
        return True


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
