import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
faminsts = UnwrapElement(IN[0])
elementlist = list()
for item in faminsts:
	try:
		elementlist.append(item.Host.ToDSType(True))
	except:
		# if that doesn't work, maybe it's a WallSweep
		try:
			hostidlist = list()
			for host in item.GetHostIds():
				hostidlist.append(doc.GetElement(host).ToDSType(True))
			elementlist.append(hostidlist)
		except:
			elementlist.append(list())
OUT = elementlist