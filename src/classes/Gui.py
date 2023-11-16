import wx
from classes.Database import Database
from funcs.export_to_csv import export_to_csv

class Gui(wx.Frame):
    def __init__(self, parent, title, x, y):
        super(Gui, self).__init__(parent, title=title, size = (x, y))
        panel = wx.Panel(self)

        # create a sizer to managing gui
        sizer = wx.BoxSizer(wx.VERTICAL)

        tables = Database.get_table_list()
        self.checkbox_table_list = []

        if isinstance(tables, list):
            for table in tables:
                checkbox = wx.CheckBox(panel, label = table)
                # add the actual checkbox and table to the checkboxtable list
                self.checkbox_table_list.append((checkbox, table))
                sizer.Add(checkbox, flag = wx.ALL, border = 5)
        else:
            print("Error: something went wrong with the database")
        # add some space after the list
        sizer.Add((-1, -1), proportion = 1)

        self.save_button = wx.Button(panel, label = "Save")
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save_button_click)
        sizer.Add(self.save_button, flag = wx.ALIGN_CENTER | wx.ALL, border = 10)

        # set the sizer for the panel
        panel.SetSizer(sizer)
        self.Center()
        self.Show()

    def on_save_button_click(self, event):
        # get the checked tables
        checked_tables = [table for checkbox, table in self.checkbox_table_list if checkbox.GetValue()]
        # go trough on these tables and export to csv
        for table in checked_tables:
            export_to_csv(table)
        wx.MessageBox("Exporting finished", "Finished", wx.OK)