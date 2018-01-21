from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])

wm.render_to_file('americas.svg')