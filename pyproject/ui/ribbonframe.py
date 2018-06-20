import wx
import zw.images as images
import wx.ribbon as RB

ID_NEW_DOC = wx.ID_HIGHEST + 1
ID_NEW_TEMP = ID_NEW_DOC + 1
ID_NEW_MAIL = ID_NEW_DOC + 2

class RibbonFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title='', pos=wx.DefaultPosition,
				 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
		wx.Frame.__init__(self, parent, id, title, pos, size, style)
		panel = wx.Panel(self)

		self._ribbon = RB.RibbonBar(panel, style=RB.RIBBON_BAR_DEFAULT_STYLE | RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)

		home = RB.RibbonPage(self._ribbon, wx.ID_ANY, 'Examples', images.logo.Bitmap)
		toolbar_panel = RB.RibbonPanel(home, wx.ID_ANY, 'Toolbar',
					style=RB.RIBBON_PANEL_NO_AUTO_MINIMISE | RB.RIBBON_PANEL_EXT_BUTTON)

		toolbar = RB.RibbonToolBar(toolbar_panel, wx.ID_ANY)
		# toolbar.AddTool(wx.ID_ANY, wx.Bitmap(images.logo.Bitmap, 16, 15))
		# toolbar.AddTool(wx.ID_ANY, images.logo.Bitmap)
		toolbar.AddTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddSeparator()

		toolbar.AddHybridTool(wx.ID_NEW, wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddSeparator()

		toolbar.AddDropdownTool(wx.ID_UNDO, wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddDropdownTool(wx.ID_REDO, wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_OTHER, wx.Size(16, 15)))
		toolbar.AddSeparator()

		toolbar.AddHybridTool(wx.ID_PRINT, wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_OTHER, wx.Size(16, 15)),
							  'This is the Print button tooltip\ndemonstrating a tooltip')
		toolbar.SetRows(2, 2)
		
		other = RB.RibbonPage(self._ribbon, wx.ID_ANY, 'Other', images.logo.Bitmap)

		self._ribbon.Realize()
		s = wx.BoxSizer(wx.VERTICAL)
		s.Add(self._ribbon, 0, wx.EXPAND)
		panel.SetSizer(s)
		self.panel = panel

		self.BindEvents(toolbar_panel)
		#self.SetIcon(images.zhao.Bitmap)
		self.CenterOnScreen()
		self.SetArtProvider(RB.RibbonMSWArtProvider())

	def BindEvents(self, toolbar_panel):
		toolbar_panel.Bind(RB.EVT_RIBBONPANEL_EXTBUTTON_ACTIVATED, self.OnExtButton)
		self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnNew, id=wx.ID_NEW)
		self.Bind(RB.EVT_RIBBONTOOLBAR_DROPDOWN_CLICKED, self.OnNewDropdown, id=wx.ID_NEW)
		self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnPrint, id=wx.ID_PRINT)
		self.Bind(wx.EVT_MENU, self.OnDropdownMenu, id=ID_NEW_DOC)
		self.Bind(wx.EVT_MENU, self.OnDropdownMenu, id=ID_NEW_TEMP)
		self.Bind(wx.EVT_MENU, self.OnDropdownMenu, id=ID_NEW_MAIL)
		# self.Bind(wx.EVT_BUTTON, self.OnColourGalleryButton, id=ID_SECONDARY_COLOUR)

	def OnNew(self, event):
		print('New button clicked.')
	
	def OnDropdownMenu(self, event):
		print('On dropdown menu.')

	def OnNewDropdown(self, event):
		menu = wx.Menu()
		menu.Append(ID_NEW_DOC, 'New Document')
		menu.Append(ID_NEW_TEMP, 'New Template')
		menu.Append(ID_NEW_MAIL, 'New Mail')
		event.PopupMenu(menu)

	def OnPrint(self, event):
		print('Print button clicked.')

	def OnUndoDropdown(self, event):
		menu = wx.Menu()
		menu.Append(wx.ID_ANY, 'Undo C')
		menu.Append(wx.ID_ANY, 'Undo B')
		menu.Append(wx.ID_ANY, 'Undo A')
		event.PopupMenu(menu)

	def OnExtButton(self, event):
		wx.MessageBox('Extended button activated')

	def SetArtProvider(self, prov):
		self._ribbon.DismissExpandedPanel()
		self._ribbon.Freeze()
		self._ribbon.SetArtProvider(prov)
		self._ribbon.Thaw()
		self._ribbon.Realize()

