import json

d0 = {'prefix': '\\prob',
                'left': r'\[',
                'right': r'\]',
                'points': 'pts'}

s = json.dumps(d0)

d1 = json.loads(s)
