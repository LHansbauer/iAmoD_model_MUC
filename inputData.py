# m aus fm
customer = [
    'c1',
    'c2'
    ]
# alle Knoten
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

origins = [
    ['c1', 'a', 1],
    ['c1', 'b', 0],
    ['c1', 'c', 0],
    ['c1', 'd', 0],
    ['c1', 'e', 0],
    ['c1', 'f', 0],
    ['c1', 'g', 0],
    ['c1', 'h', 0],
    ['c1', 'i', 0],
    ['c1', 'j', 0],
    ['c1', 'k', 0],
    ['c2', 'a', 0],
    ['c2', 'b', 0],
    ['c2', 'c', 0],
    ['c2', 'd', 1],
    ['c2', 'e', 0],
    ['c2', 'f', 0],
    ['c2', 'g', 0],
    ['c2', 'h', 0],
    ['c2', 'i', 0],
    ['c2', 'j', 0],
    ['c2', 'k', 0],
]
originsAsDict = {
    ('c1', 'a'): 1,
    ('c1', 'b'): 0,
    ('c1', 'c'): 0,
    ('c1', 'd'): 0,
    ('c1', 'e'): 0,
    ('c1', 'f'): 0,
    ('c1', 'g'): 0,
    ('c1', 'h'): 0,
    ('c1', 'i'): 0,
    ('c1', 'j'): 0,
    ('c1', 'k'): 0,
    ('c2', 'a'): 0,
    ('c2', 'b'): 0,
    ('c2', 'c'): 0,
    ('c2', 'd'): 1,
    ('c2', 'e'): 0,
    ('c2', 'f'): 0,
    ('c2', 'g'): 0,
    ('c2', 'h'): 0,
    ('c2', 'i'): 0,
    ('c2', 'j'): 0,
    ('c2', 'k'): 0
}
destinationsAsDict = {
    ('c1', 'a'): 0,
    ('c1', 'b'): 1,
    ('c1', 'c'): 0,
    ('c1', 'd'): 0,
    ('c1', 'e'): 0,
    ('c1', 'f'): 0,
    ('c1', 'g'): 0,
    ('c1', 'h'): 0,
    ('c1', 'i'): 0,
    ('c1', 'j'): 0,
    ('c1', 'k'): 0,
    ('c2', 'a'): 0,
    ('c2', 'b'): 0,
    ('c2', 'c'): 0,
    ('c2', 'd'): 0,
    ('c2', 'e'): 0,
    ('c2', 'f'): 0,
    ('c2', 'g'): 0,
    ('c2', 'h'): 1,
    ('c2', 'i'): 0,
    ('c2', 'j'): 0,
    ('c2', 'k'): 0
}

destinations = [
    ['c1', 'a', 0],
    ['c1', 'b', 1],
    ['c1', 'c', 0],
    ['c1', 'd', 0],
    ['c1', 'e', 0],
    ['c1', 'f', 0],
    ['c1', 'g', 0],
    ['c1', 'h', 0],
    ['c1', 'i', 0],
    ['c1', 'j', 0],
    ['c1', 'k', 0],
    ['c2', 'a', 0],
    ['c2', 'b', 0],
    ['c2', 'c', 0],
    ['c2', 'd', 0],
    ['c2', 'e', 0],
    ['c2', 'f', 0],
    ['c2', 'g', 0],
    ['c2', 'h', 1],
    ['c2', 'i', 0],
    ['c2', 'j', 0],
    ['c2', 'k', 0],
    ]

#value of time for each customer
valueOfTimeAsDict = {
        ('c1'):25, ('c2'):15
        }


#capacity for each arc on the road
arcCapacitiesAsDict = {
 ('a','a'):0,	('a','b'):1,	('a','c'):1,	('a','d'):1,	('a','e'):1,	('a','f'):1,	('a','g'):1,	('a','h'):1,	('a','i'):1,	('a','j'):1,	('a','k'):1,
('b','a'):1,	('b','b'):0,	('b','c'):1,	('b','d'):1,	('b','e'):1,	('b','f'):1,	('b','g'):1,	('b','h'):1,	('b','i'):1,	('b','j'):1,	('b','k'):1,
('c','a'):1,	('c','b'):1,	('c','c'):0,	('c','d'):1,	('c','e'):1,	('c','f'):1,	('c','g'):1,	('c','h'):1,	('c','i'):1,	('c','j'):1,	('c','k'):1,
('d','a'):1,	('d','b'):1,	('d','c'):1,	('d','d'):0,	('d','e'):1,	('d','f'):1,	('d','g'):1,	('d','h'):1,	('d','i'):1,	('d','j'):1,	('d','k'):1,
('e','a'):1,	('e','b'):1,	('e','c'):1,	('e','d'):1,	('e','e'):0,	('e','f'):1,	('e','g'):1,	('e','h'):1,	('e','i'):1,	('e','j'):1,	('e','k'):1,
('f','a'):1,	('f','b'):1,	('f','c'):1,	('f','d'):1,	('f','e'):1,	('f','f'):0,	('f','g'):1,	('f','h'):1,	('f','i'):1,	('f','j'):1,	('f','k'):1,
('g','a'):1,	('g','b'):1,	('g','c'):1,	('g','d'):1,	('g','e'):1,	('g','f'):1,	('g','g'):0,	('g','h'):1,	('g','i'):1,	('g','j'):1,	('g','k'):1,
('h','a'):1,	('h','b'):1,	('h','c'):1,	('h','d'):1,	('h','e'):1,	('h','f'):1,	('h','g'):1,	('h','h'):0,	('h','i'):1,	('h','j'):1,	('h','k'):1,
('i','a'):1,	('i','b'):1,	('i','c'):1,	('i','d'):1,	('i','e'):1,	('i','f'):1,	('i','g'):1,	('i','h'):1,	('i','i'):0,	('i','j'):1,	('i','k'):1,
('j','a'):1,	('j','b'):1,	('j','c'):1,	('j','d'):1,	('j','e'):1,	('j','f'):1,	('j','g'):1,	('j','h'):1,	('j','i'):1,	('j','j'):0,	('j','k'):1,
('k','a'):1,	('k','b'):1,	('k','c'):1,	('k','d'):1,	('k','e'):1,	('k','f'):1,	('k','g'):1,	('k','h'):1,	('k','i'):1,	('k','j'):1,	('k','k'):0,
       }


# [start, end, capacity]
arcCapacities = [
['a', 'a', 0], 	['b', 'a', 2], 	['c', 'a', 2], 	['d', 'a', 2], 	['e', 'a', 2], 	['f', 'a', 2], 	['g', 'a', 2], 	['h', 'a', 2], 	['i', 'a', 2], 	['j', 'a', 2], 	['k', 'a', 2],
['a', 'b', 2], 	['b', 'b', 0], 	['c', 'b', 2], 	['d', 'b', 2], 	['e', 'b', 2], 	['f', 'b', 2], 	['g', 'b', 2], 	['h', 'b', 2], 	['i', 'b', 2], 	['j', 'b', 2], 	['k', 'b', 2],
['a', 'c', 2], 	['b', 'c', 2], 	['c', 'c', 0], 	['d', 'c', 2], 	['e', 'c', 2], 	['f', 'c', 2], 	['g', 'c', 2], 	['h', 'c', 2], 	['i', 'c', 2], 	['j', 'c', 2], 	['k', 'c', 2],
['a', 'd', 2], 	['b', 'd', 2], 	['c', 'd', 2], 	['d', 'd', 0], 	['e', 'd', 2], 	['f', 'd', 2], 	['g', 'd', 2], 	['h', 'd', 2], 	['i', 'd', 2], 	['j', 'd', 2], 	['k', 'd', 2],
['a', 'e', 2], 	['b', 'e', 2], 	['c', 'e', 2], 	['d', 'e', 2], 	['e', 'e', 0], 	['f', 'e', 2], 	['g', 'e', 2], 	['h', 'e', 2], 	['i', 'e', 2], 	['j', 'e', 2], 	['k', 'e', 2],
['a', 'f', 2], 	['b', 'f', 2], 	['c', 'f', 2], 	['d', 'f', 2], 	['e', 'f', 2], 	['f', 'f', 0], 	['g', 'f', 2], 	['h', 'f', 2], 	['i', 'f', 2], 	['j', 'f', 2], 	['k', 'f', 2],
['a', 'g', 2], 	['b', 'g', 2], 	['c', 'g', 2], 	['d', 'g', 2], 	['e', 'g', 2], 	['f', 'g', 2], 	['g', 'g', 0], 	['h', 'g', 2], 	['i', 'g', 2], 	['j', 'g', 2], 	['k', 'g', 2],
['a', 'h', 2], 	['b', 'h', 2], 	['c', 'h', 2], 	['d', 'h', 2], 	['e', 'h', 2], 	['f', 'h', 2], 	['g', 'h', 2], 	['h', 'h', 0], 	['i', 'h', 2], 	['j', 'h', 2], 	['k', 'h', 2],
['a', 'i', 2], 	['b', 'i', 2], 	['c', 'i', 2], 	['d', 'i', 2], 	['e', 'i', 2], 	['f', 'i', 2], 	['g', 'i', 2], 	['h', 'i', 2], 	['i', 'i', 0], 	['j', 'i', 2], 	['k', 'i', 2],
['a', 'j', 2], 	['b', 'j', 2], 	['c', 'j', 2], 	['d', 'j', 2], 	['e', 'j', 2], 	['f', 'j', 2], 	['g', 'j', 2], 	['h', 'j', 2], 	['i', 'j', 2], 	['j', 'j', 0], 	['k', 'j', 2],
['a', 'k', 2], 	['b', 'k', 2], 	['c', 'k', 2], 	['d', 'k', 2], 	['e', 'k', 2], 	['f', 'k', 2], 	['g', 'k', 2], 	['h', 'k', 2], 	['i', 'k', 2], 	['j', 'k', 2], 	['k', 'k', 0]
    ]

requests = [
    ['a', 'b', 1]
]


# 'origin': [neighbours]
graph = {
    'a': ['e', 'f', 'h'],
    'b': ['g', 'h'],
    'c': ['g', 'i'],
    'd': ['i', 'j'],
    'e': ['a', 'k'],
    'f': ['a', 'g', 'i', 'k'],
    'g': ['b', 'c', 'f', 'h'],
    'h': ['a', 'b', 'g'],
    'i': ['c', 'd', 'f'],
    'j': ['d', 'k'],
    'k': ['e', 'f', 'j']
}


# [start, end, distance]
distances = [
['e', 'a', 4.12], ['f', 'a', 12.53], ['h', 'a', 8.25],
['g', 'b', 11.05], ['h', 'b', 10.2],
['g', 'c', 13.6], ['i', 'c', 8.06],
['i', 'd', 8.25], ['j', 'd', 4.47],
['a', 'e', 4.12], ['k', 'e', 16.55],
['a', 'f', 12.53], ['g', 'f', 13.6], ['i', 'f', 13.45], ['k', 'f', 5.83],
['b', 'g', 11.05], ['c', 'g', 13.6], ['f', 'g', 13.6], ['h', 'g', 14.21],
['a', 'h', 8.25], ['b', 'h', 10.2], ['g', 'h', 14.21],
['c', 'i', 8.06], ['d', 'i', 8.25], ['f', 'i', 13.45],
['d', 'j', 4.47], ['k', 'j', 3.61],
['e', 'k', 16.55], ['f', 'k', 5.83], ['j', 'k', 3.61],
]

#shortest distance between all nodes
shortestDistancesAsDict = {
('a', 'a'): 1000,('b', 'a'): 1000,('c', 'a'): 1000,('d', 'a'): 1000,('e', 'a'): 4.12,('f', 'a'): 12.53,('g', 'a'): 1000,('h', 'a'): 8.25,('i', 'a'): 1000,('j', 'a'): 1000,('k', 'a'): 1000,
('a', 'b'): 1000,('b', 'b'): 1000,('c', 'b'): 1000,('d', 'b'): 1000,('e', 'b'): 1000,('f', 'b'): 1000,('g', 'b'): 11.05,('h', 'b'): 10.2,('i', 'b'): 1000,('j', 'b'): 1000,('k', 'b'): 1000,
('a', 'c'): 1000,('b', 'c'): 1000,('c', 'c'): 1000,('d', 'c'): 1000,('e', 'c'): 1000,('f', 'c'): 1000,('g', 'c'): 13.6,('h', 'c'): 1000,('i', 'c'): 8.06,('j', 'c'): 1000,('k', 'c'): 1000,
('a', 'd'): 1000,('b', 'd'): 1000,('c', 'd'): 1000,('d', 'd'): 1000,('e', 'd'): 1000,('f', 'd'): 1000,('g', 'd'): 1000,('h', 'd'): 1000,('i', 'd'): 8.25,('j', 'd'): 4.47,('k', 'd'): 1000,
('a', 'e'): 4.12,('b', 'e'): 1000,('c', 'e'): 1000,('d', 'e'): 1000,('e', 'e'): 1000,('f', 'e'): 1000,('g', 'e'): 1000,('h', 'e'): 1000,('i', 'e'): 1000,('j', 'e'): 1000,('k', 'e'): 16.55,
('a', 'f'): 12.53,('b', 'f'): 1000,('c', 'f'): 1000,('d', 'f'): 1000,('e', 'f'): 1000,('f', 'f'): 1000,('g', 'f'): 13.6,('h', 'f'): 1000,('i', 'f'): 13.45,('j', 'f'): 1000,('k', 'f'): 5.83,
('a', 'g'): 1000,('b', 'g'): 11.05,('c', 'g'): 13.6,('d', 'g'): 1000,('e', 'g'): 1000,('f', 'g'): 13.6,('g', 'g'): 1000,('h', 'g'): 14.21,('i', 'g'): 1000,('j', 'g'): 1000,('k', 'g'): 1000,
('a', 'h'): 8.25,('b', 'h'): 10.2,('c', 'h'): 1000,('d', 'h'): 1000,('e', 'h'): 1000,('f', 'h'): 1000,('g', 'h'): 14.21,('h', 'h'): 1000,('i', 'h'): 1000,('j', 'h'): 1000,('k', 'h'): 1000,
('a', 'i'): 1000,('b', 'i'): 1000,('c', 'i'): 8.06,('d', 'i'): 8.25,('e', 'i'): 1000,('f', 'i'): 13.45,('g', 'i'): 1000,('h', 'i'): 1000,('i', 'i'): 1000,('j', 'i'): 1000,('k', 'i'): 1000,
('a', 'j'): 1000,('b', 'j'): 1000,('c', 'j'): 1000,('d', 'j'): 4.47,('e', 'j'): 1000,('f', 'j'): 1000,('g', 'j'): 1000,('h', 'j'): 1000,('i', 'j'): 1000,('j', 'j'): 1000,('k', 'j'): 3.61,
('a', 'k'): 1000,('b', 'k'): 1000,('c', 'k'): 1000,('d', 'k'): 1000,('e', 'k'): 16.55,('f', 'k'): 5.83,('g', 'k'): 1000,('h', 'k'): 1000,('i', 'k'): 1000,('j', 'k'): 3.61,('k', 'k'): 1000
}

#time on a specific arc
timeOnArcAsDict = {
        ('a','a'):0,	('a','b'):12,	('a','c'):7,	('a','d'):6,	('a','e'):6,	('a','f'):6,	('a','g'):9,	('a','h'):3,	('a','i'):5,	('a','j'):8,	('a','k'):12,
('b','a'):5,	('b','b'):0,	('b','c'):4,	('b','d'):9,	('b','e'):7,	('b','f'):3,	('b','g'):3,	('b','h'):4,	('b','i'):3,	('b','j'):4,	('b','k'):7,
('c','a'):5,	('c','b'):6,	('c','c'):0,	('c','d'):5,	('c','e'):11,	('c','f'):7,	('c','g'):8,	('c','h'):2,	('c','i'):5,	('c','j'):3,	('c','k'):2,
('d','a'):5,	('d','b'):2,	('d','c'):4,	('d','d'):0,	('d','e'):5,	('d','f'):4,	('d','g'):5,	('d','h'):9,	('d','i'):8,	('d','j'):10,	('d','k'):8,
('e','a'):6,	('e','b'):6,	('e','c'):3,	('e','d'):8,	('e','e'):0,	('e','f'):11,	('e','g'):11,	('e','h'):5,	('e','i'):7,	('e','j'):7,	('e','k'):6,
('f','a'):4,	('f','b'):6,	('f','c'):4,	('f','d'):10,	('f','e'):11,	('f','f'):0,	('f','g'):2,	('f','h'):7,	('f','i'):11,	('f','j'):8,	('f','k'):7,
('g','a'):5,	('g','b'):3,	('g','c'):12,	('g','d'):9,	('g','e'):2,	('g','f'):7,	('g','g'):0,	('g','h'):4,	('g','i'):11,	('g','j'):10,	('g','k'):2,
('h','a'):11,	('h','b'):6,	('h','c'):3,	('h','d'):7,	('h','e'):3,	('h','f'):11,	('h','g'):8,	('h','h'):0,	('h','i'):9,	('h','j'):5,	('h','k'):9,
('i','a'):8,	('i','b'):10,	('i','c'):6,	('i','d'):2,	('i','e'):4,	('i','f'):8,	('i','g'):11,	('i','h'):9,	('i','i'):0,	('i','j'):6,	('i','k'):8,
('j','a'):7,	('j','b'):6,	('j','c'):2,	('j','d'):10,	('j','e'):3,	('j','f'):9,	('j','g'):8,	('j','h'):4,	('j','i'):9,	('j','j'):0,	('j','k'):8,
('k','a'):5,	('k','b'):11,	('k','c'):12,	('k','d'):6,	('k','e'):7,	('k','f'):4,	('k','g'):7,	('k','h'):5,	('k','i'):10,	('k','j'):3,	('k','k'):0
}

#price for the starting node on the road
priceOriginAsDict = {
        ('a'):3,
('b'):3,
('c'):4,
('d'):4,
('e'):2,
('f'):6,
('g'):1,
('h'):1,
('i'):4,
('j'):3,
('k'):5
}
#price for the destination node on the road
priceDestinationAsDict = {
        ('a'):4,
('b'):2,
('c'):1,
('d'):3,
('e'):1,
('f'):3,
('g'):4,
('h'):5,
('i'):6,
('j'):5,
('k'):1
}

#price for each arc on the road
priceRoadAsDict = {
        ('a','a'):0,	('a','b'):6,	('a','c'):7,	('a','d'):6,	('a','e'):4,	('a','f'):7,	('a','g'):4,	('a','h'):8,	('a','i'):6,	('a','j'):7,	('a','k'):6,
('b','a'):7,	('b','b'):0,	('b','c'):7,	('b','d'):6,	('b','e'):5,	('b','f'):5,	('b','g'):5,	('b','h'):5,	('b','i'):5,	('b','j'):6,	('b','k'):5,
('c','a'):5,	('c','b'):6,	('c','c'):0,	('c','d'):5,	('c','e'):7,	('c','f'):5,	('c','g'):7,	('c','h'):5,	('c','i'):5,	('c','j'):7,	('c','k'):5,
('d','a'):7,	('d','b'):7,	('d','c'):7,	('d','d'):0,	('d','e'):5,	('d','f'):4,	('d','g'):5,	('d','h'):8,	('d','i'):7,	('d','j'):7,	('d','k'):5,
('e','a'):5,	('e','b'):7,	('e','c'):6,	('e','d'):6,	('e','e'):0,	('e','f'):5,	('e','g'):7,	('e','h'):5,	('e','i'):5,	('e','j'):8,	('e','k'):4,
('f','a'):7,	('f','b'):7,	('f','c'):5,	('f','d'):6,	('f','e'):7,	('f','f'):0,	('f','g'):8,	('f','h'):6,	('f','i'):7,	('f','j'):7,	('f','k'):7,
('g','a'):4,	('g','b'):5,	('g','c'):6,	('g','d'):5,	('g','e'):5,	('g','f'):4,	('g','g'):0,	('g','h'):4,	('g','i'):7,	('g','j'):7,	('g','k'):5,
('h','a'):7,	('h','b'):8,	('h','c'):7,	('h','d'):6,	('h','e'):8,	('h','f'):7,	('h','g'):5,	('h','h'):0,	('h','i'):4,	('h','j'):8,	('h','k'):7,
('i','a'):4,	('i','b'):7,	('i','c'):7,	('i','d'):7,	('i','e'):5,	('i','f'):6,	('i','g'):6,	('i','h'):5,	('i','i'):0,	('i','j'):5,	('i','k'):6,
('j','a'):5,	('j','b'):8,	('j','c'):5,	('j','d'):7,	('j','e'):5,	('j','f'):7,	('j','g'):6,	('j','h'):7,	('j','i'):6,	('j','j'):0,	('j','k'):6,
('k','a'):5,	('k','b'):4,	('k','c'):8,	('k','d'):4,	('k','e'):8,	('k','f'):5,	('k','g'):5,	('k','h'):4,	('k','i'):5,	('k','j'):6,	('k','k'):0
}