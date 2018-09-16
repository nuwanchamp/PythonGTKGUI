import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk as g

class HeaderBarWindow(g.Window):
	def __init__(self):
		g.Window.__init__(self, title="Header Window")
		self.set_border_width(10)
		self.set_default_size(400, 200)

		hb = g.HeaderBar()
		hb.set_show_close_button(True)
		hb.props.title = "HeaderBar example"
		self.set_titlebar(hb)

		button = g.Button()
		icon = Gio.ThemedIcon(name="mail-send-recieve-symbolic")
		image = g.Image.new_from_gicon(icon, g.IconSize.BUTTON)
		button.add(image)
		hb.pack_end(button)

		box = g.Box(orientation=g.Orientation.HORIZONTAL)
		g.StyleContext.add_class(box.get_style_context(), "linked")

		button = g.Button()
		button.add(g.Arrow(g.ArrowType.LEFT, g.ShadowType.NONE))
		box.add(button)

		button = g.Button()
		button.add(g.Arrow(g.ArrowType.RIGHT, g.ShadowType.NONE))
		box.add(button)

		hb.pack_start(box)

		self.add(g.TextView())

win = HeaderBarWindow()
win.connect("destroy", g.main_quit)
win.show_all()
g.main()
