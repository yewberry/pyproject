import wx
import wx.ribbon as RB
import zw.images as images
import zw.utils as utils
import ui.trayicon as trayicon

ID_BAR_FOO = wx.ID_HIGHEST + 1
ID_BAR_TOGGLE = ID_BAR_FOO + 1
ID_NEW_MAIL = ID_BAR_FOO + 2
ID_BTN_DROP = ID_BAR_FOO + 3
ID_BAR_TOGGLE2 = ID_BAR_FOO + 4

class RibbonFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title='', pos=wx.DefaultPosition,
				 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
		wx.Frame.__init__(self, parent, id, title, pos, size, style)
		if utils.isWin32():
			self._tbIcon = trayicon.TrayIcon(self, images.logo24.Icon)
		self._panel = wx.Panel(self)
		self._ribbon = RB.RibbonBar(self._panel, style=RB.RIBBON_BAR_DEFAULT_STYLE | RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)

		rb_page = RB.RibbonPage(self._ribbon, wx.ID_ANY, 'Examples', images.logo.Bitmap)
		rb_panel = RB.RibbonPanel(rb_page, wx.ID_ANY, 'Toolbar', style=RB.RIBBON_PANEL_NO_AUTO_MINIMISE | RB.RIBBON_PANEL_EXT_BUTTON)
		rb_bar = RB.RibbonToolBar(rb_panel, wx.ID_ANY)
		rb_bar.AddTool(ID_BAR_FOO, wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(16, 16))
						, help_string='This is simple toolbar')
		rb_bar.AddToggleTool(ID_BAR_TOGGLE, images.logo16.Bitmap, "help string")
		rb_bar.AddHybridTool(wx.ID_NEW, wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_OTHER, wx.Size(16, 16)),
							  'This is the AddHybridTool button tooltip\ndemonstrating a tooltip')
		rb_bar.AddDropdownTool(wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_ADD_BOOKMARK, wx.ART_OTHER, wx.Size(16, 16)))
		rb_bar.AddSeparator()
		rb_bar.AddTool(wx.ID_ANY, images.logo16.Bitmap, kind=RB.RIBBON_BUTTON_TOGGLE)
		rb_bar.AddTool(wx.ID_ANY, images.logo16.Bitmap, kind=RB.RIBBON_BUTTON_HYBRID)
		rb_bar.AddTool(wx.ID_ANY, images.logo16.Bitmap, kind=RB.RIBBON_BUTTON_DROPDOWN)

		rb_panel2 = RB.RibbonPanel(rb_page, wx.ID_ANY, 'Buttons')
		rb_bar2 = RB.RibbonButtonBar(rb_panel2, wx.ID_ANY)
		# also has AddToggleTool AddHybridTool and AddDropdownTool
		rb_bar2.AddButton(wx.ID_ANY, "NormalButton", images.logo48.Bitmap)
		rb_bar2.AddButton(ID_BAR_TOGGLE2, "ToggleButton", images.logo48.Bitmap, kind=RB.RIBBON_BUTTON_TOGGLE)
		rb_bar2.AddButton(wx.ID_ANY, "HybridButton", images.logo48.Bitmap, kind=RB.RIBBON_BUTTON_HYBRID)
		rb_bar2.AddButton(wx.ID_ANY, "DropButton", images.logo48.Bitmap, kind=RB.RIBBON_BUTTON_DROPDOWN)
		rb_bar2.AddDropdownButton(ID_BTN_DROP, "Other Polygon", images.logo16.Bitmap, "")

		# min rows and max rows
		rb_bar.SetRows(2, 3)
		
		other = RB.RibbonPage(self._ribbon, wx.ID_ANY, 'Other', images.logo.Bitmap)

		self._ribbon.Realize()
		s = wx.BoxSizer(wx.VERTICAL)
		s.Add(self._ribbon, 0, wx.EXPAND)
		self._panel.SetSizer(s)

		self.BindEvents([rb_panel, rb_panel2])
		#self.SetIcon(images.logo.Icon)
		self.CenterOnScreen()
		self.setArtProvider(RB.RibbonMSWArtProvider())

	def BindEvents(self, bars):
		rb_panel, rb_panel2 = bars
		# toolbar panel ext button click
		rb_panel.Bind(RB.EVT_RIBBONPANEL_EXTBUTTON_ACTIVATED, self.OnExtButton)

		# process events in frame msg loop
		# normal toolbar click
		self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnToolClick, id=ID_BAR_FOO)
		# toggle toolbar click
		self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnToogleClick, id=ID_BAR_TOGGLE)
		self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnToogleClick, id=ID_BAR_TOGGLE2)		
		# hybrid button, dropdown and menu click
		self.Bind(RB.EVT_RIBBONTOOLBAR_CLICKED, self.OnToolClick, id=wx.ID_NEW)
		self.Bind(RB.EVT_RIBBONTOOLBAR_DROPDOWN_CLICKED, self.OnToolDropdown, id=wx.ID_NEW)
		self.Bind(wx.EVT_MENU, self.OnMenuClick, id=wx.ID_NEW)
		# 
		# self.Bind(wx.EVT_BUTTON, self.OnColourGalleryButton, id=ID_SECONDARY_COLOUR)
		# 
		if utils.isWin32():
			self.Bind(wx.EVT_ICONIZE, self.onIconify)
		self.Bind(wx.EVT_CLOSE, self.onClose)

	def OnToolDropdown(self, event):
		menu = wx.Menu()
		menu.Append(wx.ID_NEW, "String 1")
		menu.Append(wx.ID_ANY, "String 2")
		menu.Append(wx.ID_ANY, "String 3")
		event.PopupMenu(menu)

	def OnToolClick(self, event):
		print('toolbar clicked.')
	
	def OnMenuClick(self, event):
		print('menu clicked.')
	
	def OnToogleClick(self, event):
		bar = event.GetBar()
		tool_id = event.GetId()
		print( 'tool:{0}, state:{1}'.format( tool_id, bar.GetToolState(tool_id)) )

	def OnButtonClick(self, event):
		print('button clicked.')
	
	def OnExtButton(self, event):
		wx.MessageBox('Extended button activated')

	def setArtProvider(self, prov):
		self._ribbon.DismissExpandedPanel()
		self._ribbon.Freeze()
		self._ribbon.SetArtProvider(prov)
		self._ribbon.Thaw()
		self._ribbon.Realize()

	def onIconify(self, event):
		self.Hide()

	def onClose(self, event):
		'''
		Destroy the taskbar icon and the frame
		'''
		if utils.isWin32():
			self._tbIcon.RemoveIcon()
			self._tbIcon.Destroy()
		self.Destroy()


