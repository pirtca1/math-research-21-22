geocode = lambda query: geolocator.geocode("%s, Cleveland OH" % query)

print(geocode("11111 Euclid Ave"))