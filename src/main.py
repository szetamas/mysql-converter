import sys
import wx
from classes.Gui import Gui
from config import db_config

if __name__ == "__main__":
    size_x = 400
    size_y = 500
    # check commandline arguments
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.startswith("-dbname="):
                # replace the database with the second part after =
                db_config["database"] = arg.split("=")[1]
            if arg.startswith("-sizex="):
                size_x = int(arg.split("=")[1])
            elif arg.startswith("-size_x="):
                size_x = int(arg.split("=")[1])
            if arg.startswith("-sizey="):
                size_y = int(arg.split("=")[1])
            elif arg.startswith("-size_y="):
                size_y = int(arg.split("=")[1])

    app = wx.App(False)
    frame = Gui(None, "Database Exporter to CSV", size_x, size_y)
    app.MainLoop()