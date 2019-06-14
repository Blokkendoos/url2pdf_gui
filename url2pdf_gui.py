#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Sat Jun  8 20:00:07 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Url2pdfFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Url2pdfFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.text_ctrl_url = wx.TextCtrl(self, wx.ID_ANY, "")
        self.checkbox_paginate = wx.CheckBox(self, wx.ID_ANY, "")
        self.checkbox_print_background = wx.CheckBox(self, wx.ID_ANY, "")
        self.checkbox_load_images = wx.CheckBox(self, wx.ID_ANY, "")
        self.checkbox_enable_javascript = wx.CheckBox(self, wx.ID_ANY, "")
        self.button_orientation = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("./icons/orientation_portrait.png", wx.BITMAP_TYPE_ANY))
        self.ctrl_save_path = wx.DirPickerCtrl(self, wx.ID_ANY)
        self.button_cancel = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.button_ok = wx.Button(self, wx.ID_OK, "Ok")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox_paginate_clicked, self.checkbox_paginate)
        self.Bind(wx.EVT_BUTTON, self.on_button_orientation_clicked, self.button_orientation)
        self.Bind(wx.EVT_BUTTON, self.on_button_cancel_clicked, self.button_cancel)
        self.Bind(wx.EVT_BUTTON, self.on_button_ok_clicked, self.button_ok)
        # end wxGlade

        # http://wxpython-users.1045709.n5.nabble.com/Catching-ESCAPE-Key-td2349044.html
        self.SetAcceleratorTable(wx.AcceleratorTable([
            (wx.ACCEL_NORMAL, wx.WXK_ESCAPE, wx.ID_CANCEL),
        ]))

    def __set_properties(self):
        # begin wxGlade: Url2pdfFrame.__set_properties
        self.SetTitle("URL to PDF")
        self.button_orientation.SetSize(self.button_orientation.GetBestSize())
        self.button_ok.SetFocus()
        self.button_ok.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Url2pdfFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Save path"), wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Options"), wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "URL"), wx.HORIZONTAL)
        sizer_2.Add(self.text_ctrl_url, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        sizer_1.Add(sizer_2, 0, wx.EXPAND | wx.TOP, 10)
        sizer_6.Add(self.checkbox_paginate, 0, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Paginate")
        sizer_6.Add(label_1, 0, 0, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_7.Add(self.checkbox_print_background, 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Print background")
        sizer_7.Add(label_2, 0, 0, 0)
        sizer_4.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.checkbox_load_images, 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Load images")
        sizer_8.Add(label_3, 0, 0, 0)
        sizer_4.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_9.Add(self.checkbox_enable_javascript, 0, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Enable javascript")
        sizer_9.Add(label_4, 0, 0, 0)
        sizer_4.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_orientation, 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Orientation")
        sizer_5.Add(label_5, 0, 0, 0)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 10)
        sizer_10.Add(self.ctrl_save_path, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_10, 0, wx.EXPAND, 10)
        sizer_11.Add(self.button_cancel, 0, wx.LEFT, 10)
        sizer_11.Add(self.button_ok, 0, wx.LEFT, 10)
        sizer_1.Add(sizer_11, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_checkbox_paginate_clicked(self, event):  # wxGlade: Url2pdfFrame.<event_handler>
        print("Event handler 'on_checkbox_paginate_clicked' not implemented!")
        event.Skip()

    def on_button_orientation_clicked(self, event):  # wxGlade: Url2pdfFrame.<event_handler>
        print("Event handler 'on_button_orientation_clicked' not implemented!")
        event.Skip()

    def on_button_cancel_clicked(self, event):  # wxGlade: Url2pdfFrame.<event_handler>
        print("Event handler 'on_button_cancel_clicked' not implemented!")
        event.Skip()

    def on_button_ok_clicked(self, event):  # wxGlade: Url2pdfFrame.<event_handler>
        print("Event handler 'on_button_ok_clicked' not implemented!")
        event.Skip()

# end of class Url2pdfFrame


class MyApp(wx.App):
    def OnInit(self):
        self.frame = Url2pdfFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
