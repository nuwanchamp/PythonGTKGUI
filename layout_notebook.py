import gi 
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as g

class NoteBookWindow(g.Window):


	def __init__(self):

		g.Window.__init__(self, title="Simple notebook Example")
		self.set_border_width(10)

		self.notebook = g.Notebook()
		self.add(self.notebook)

		self.page1 = g.Box()
		self.page1.set_border_width(10)
		self.page1.add(g.Label("Default Page")) 
		self.notebook.append_page(self.page1, g.Label('Pain Title'))

		self.page2 = g.Box()
		self.page2.set_border_width(10)
		self.page2.add(g.Label("A page with an Image for title"))
		self.notebook.append_page(
			self.page2,
			g.Image.new_from_icon_name(
				"help-about",
				g.IconSize.MENU
			)
		)

win = NoteBookWindow()
win.connect('destroy', g.main_quit)
win.show_all()
g.main()