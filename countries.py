from pygal.maps.world import COUNTRIES

# find two digit codes for each country
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])