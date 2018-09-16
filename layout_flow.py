import gi
gi.require_version('Gtk',  '3.0')
from gi.repository import Gdk, Gtk as g

class FlowWindow(g.Window):
	def __init__(self):
		g.Window.__init__(self, title="Flow Window")
		self.set_border_width(10)
		self.set_default_size(300, 250)

		header = g.HeaderBar(title="Flow Box")
		header.set_subtitle("sample flow app")
		header.props.show_close_button = True


		self.set_titlebar(header)

		scrolled = g.ScrolledWindow()
		scrolled.set_policy(g.PolicyType.NEVER, g.PolicyType.AUTOMATIC)

		flowbox = g.FlowBox()
		flowbox.set_valign(g.Align.START)
		flowbox.set_max_children_per_line(30)
		flowbox.set_selection_mode(g.SelectionMode.NONE)

		self.create_flowbox(flowbox)

		scrolled.add(flowbox)

		self.add(scrolled)
		self.show_all()

	def on_draw(self, widget, cr, data):
		context = widget.get_style_context()
		width = widget.get_allocated_width()
		height = widget.get_allocated_height()
		g.render_background(context, cr, 0, 0, width, height)
		
		r, gg, b, a = data['color']
		cr.set_source_rgba(r, gg, b, a)
		cr.rectangle(0, 0, width, height)
		cr.fill()

	def color_swatch_new(self, str_color):
		color = Gdk.color_parse(str_color)

		rgba = Gdk.RGBA.from_color(color)
		button = g.Button()

		area = g.DrawingArea()
		area.set_size_request(24, 24)
		area.connect("draw", self.on_draw, {'color':rgba})

		button.add(area)
		return button

	def create_flowbox(self, flowbox):
		colors = [
			'AliceBlue',
	        'AntiqueWhite',
	        'AntiqueWhite1',
	        'AntiqueWhite2',
	        'AntiqueWhite3',
	        'AntiqueWhite4',
	        'aqua',
	        'aquamarine',
	        'aquamarine1',
	        'aquamarine2',
	        'aquamarine3',
	        'aquamarine4',
	        'azure',
	        'azure1',
	        'azure2',
	        'azure3',
	        'azure4',
	        'beige',
	        'bisque',
	        'bisque1',
	        'bisque2',
	        'bisque3',
	        'bisque4',
	        'black',
	        'BlanchedAlmond',
	        'blue',
	        'blue1',
	        'blue2',
	        'blue3',
	        'blue4',
	        'BlueViolet',
	        'brown',
	        'brown1',
	        'brown2',
	        'brown3',
	        'brown4',
	        'burlywood',
	        'burlywood1',
	        'burlywood2',
	        'burlywood3',
	        'burlywood4',
	        'CadetBlue',
	        'CadetBlue1',
	        'CadetBlue2',
	        'CadetBlue3',
	        'CadetBlue4',
	        'chartreuse',
	        'chartreuse1',
	        'chartreuse2',
	        'chartreuse3',
	        'chartreuse4',
	        'chocolate',
	        'chocolate1',
	        'chocolate2',
	        'chocolate3',
	        'chocolate4',
	        'coral',
	        'coral1',
	        'coral2',
	        'coral3',
	        'coral4'
		]

		for color in colors:
			button = self.color_swatch_new(color)
			flowbox.add(button)


win = FlowWindow()
win.connect('destroy', g.main_quit)
win.show_all()
g.main()
