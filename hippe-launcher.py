# MIT License

# Copyright (c) 2021 OldGameBox

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import hippe as hp
import wget
import os

__name__ = "HiPPe Launcher"
__version__ = "0.1"
__author__ = "OldGameBox Polus"

#hp.HideDebbuger()
hp.init(720,480,__name__,False)
hp.SetWindowIcon("data/hippe-logo.png")

path=""
status = 'Not Installed'

Create_project = hp.Button(hp.Vector(605,75+325),150,30,0,(190,190,190),"Create Project",(255,255,255),"data/Dosis.ttf",15,True)
Project_path = hp.Button(hp.Vector(645,33+325),70,26,0,(150,150,150),"Select",(255,255,255),"data/Dosis.ttf",15,True)

while hp.Drawing():
    hp.FPSLimit(60)
    hp.OnExit()
    hp.Fill(hp.WHITE)

    hp.DrawRect(0,0,100,40,(150,150,150))
    hp.DrawRect(0,40,100,440,(190,190,190))
    hp.DrawRect(150,20+325,460,26,(190,190,190))
    hp.Text("HiPPe", hp.Vector(50,20), hp.WHITE, 0, "data/PressStart2P.ttf", 15, True, True)
    hp.Text("HiPPe Engine", hp.Vector(410,75), hp.BLACK, 0, "data/PressStart2P.ttf", 45, True, True)
    hp.Text("Project Creator", hp.Vector(410,125), hp.BLACK, 0, "data/PressStart2P.ttf", 25, True, True)
    hp.Text("OldGameBox", hp.Vector(50,465), hp.WHITE, 0, "data/PressStart2P.ttf", 9, True, True)
    hp.Text("v."+__version__, hp.Vector(700,465), hp.BLACK, 0, "data/Dosis.ttf", 15, True, True)
    hp.Text("Status: "+status, hp.Vector(150,75+320), hp.BLACK, 0, "data/Dosis.ttf", 15, True, False)
    hp.Text("Path: "+path, hp.Vector(153,22+325), hp.WHITE, 0, "data/Dosis.ttf", 17, True, False)
    hp.DrawButton(Create_project)
    hp.DrawButton(Project_path)

    if hp.ButtonClick(Project_path,1):
        path = hp.GetFolder()
        if os.path.isfile(os.path.join(path, "hippe.py")):
            status = "Installed"
        else:
            status = "Not installed"
    if hp.ButtonClick(Create_project,1):
        try:
            if not os.path.isfile(os.path.join(path, "app.py")):
                file = open(os.path.join(path, "app.py"),"w")
                file.write('import hippe as hp\n\n__name__ = "App"\n__version__ = "1.0"\n__author__ = "name"\n\n#hp.HideDebbuger()\nhp.init(500,500,__name__,True)    #open window\n\n#vars\n\nwhile hp.Drawing():\n    hp.FPSLimit(60)\n    hp.OnExit()\n\n    #render code\n\n    hp.Render()\nhp.Exit()')
                file.close()
            if status == "Installed":
                os.remove(os.path.join(path, "hippe.py"))
            wget.download('https://raw.githubusercontent.com/OldGameBox/HiPPe-Engine/main/hippe.py', path)
            os.system("cls")
            if os.path.isfile(os.path.join(path, "hippe.py")):
                status = "Installed"
            else:
                status = "Not installed"

        except :
            os.system("cls")
            status = "Error: Access denied. Try another folder"
    hp.Render()
hp.Exit()

