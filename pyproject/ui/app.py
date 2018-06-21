import os
import wx
import zw.logger as logger
from zw.utils import Timeit
from ui.ribbonframe import RibbonFrame
LOG = logger.getLogger(__name__)
class App(wx.App):
	def OnInit(self):
		t = Timeit()
		LOG.debug("OnInit")

		# setup MainFrame
		# frame = MyMainFrame(None, res.S_MF_TITLE)
		# self.SetTopWindow(frame)
		# frame.Show(True)

		frm = RibbonFrame(None, -1, "wx.ribbon Sample Application", size=(800, 600))
		frm.Show()

		LOG.debug('Elapsed time: %f ms' % t.end())
		return True

	def OnExit(self):
		# exit but main process still there why?
		wx.Exit()




