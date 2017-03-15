states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'New York': 'NY',
    'California': 'CA',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'PortLand'

print '-'*10
print "NY state has: ",cities['NY']
print "OR state has: ",cities['OR']

print '-'*10
print "Michigan : ",states['Michigan']
print "Florida : ",states['Florida']

print '-'*10
print "Michigan has : ",cities[states['Michigan']]
print "florida has : ",cities[states['Florida']]

print '-'*10
for state, abbrev in states.items():
    print"%s is abbrevated as %s and has city %s."%(
        state,abbrev,cities[abbrev]
    )

print '-'*10
state = states.get('Texas',None)

if not state:
    print "Soryr no texas!"

city = cities.get('TX','Does not exist')
print "the city for the state 'TX' is %s"%city