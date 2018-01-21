import json

from pygal.maps.world import World

from country_codes import get_country_code

# Load the data into a list.
filename = 'na.json'
with open(filename) as f:
    pop_data = json.load(f)

# create a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)

        #put codes in dictionary
        if code:
            cc_populations[code] = population

    wm = World()
    wm.force_uri_protocol = 'http'
    wm.title = 'World Population in 2010'
    wm.add('2010', cc_populations)

    wm.render_to_file('northamerica2010_population.svg')