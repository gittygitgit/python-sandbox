#!/usr/bin/python

print '{0}, {1}, {2}'.format('a', 'b', 'c')
print '{1}, {0}, {2}'.format('a', 'b', 'c')
print '{0}, {1}, {0}'.format('a', 'b', 'c')

print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')

coord={'latitude': '37.24N', 'longitude': '-115.81W'}
print  'Coordinates: {latitude}, {longitude}'.format(**coord)

print '{0:<30}'.format('left aligned')
print '{0:>30}'.format('right aligned')
print '{0:*^30}'.format('centered')  # use '*' as a fill char

print "repr() shows quotes: {0!r}; str() doesn't: {1!s}".format('test1', 'test2')

