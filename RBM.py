#!usr/bin/env python
#coding:utf-8

'''
Author: Haidong Zhang
E-mail: haidong_zhang13@163.com
Date: 2016.1.31
'''

from graphviz import Graph
from network import Network

class RBM(Network):
    def __init__(self, numHidden, numVisible, direction='LR'):
        '''
        numHidden: the number of hidden units;
        numVisible: the number of visible units;
        direction: the direction
            LR: from left to right;
            RL: from right to left;
            TB: from top to bottom;
            BT: from bottom to top;
        '''
        self.numHidden = numHidden
        self.numVisible = numVisible
        self.direction = direction

    def plot(self):
        g = Graph(format='png')
        styles = {
            'graph': {
                'rankdir': self.direction,
                'splines': 'line',
                'label': 'Restricted Boltzmann Machine',
                'labelloc': 't', ## t: top, b: bottom, c: center
                'labeljust': 'c', ## l: left, r: right, c: center
            },
            'edge':{
                'color': 'black',
                # 'constraint': 'false',
                'style': 'filled',
            }
        }
        self.add_styles(g, styles)

        vLayer = Graph('cluster_0')
        styles = {
            'graph': {
                'rankdir': 'LR',
                'splines': 'line',
                'label': 'Visible Units',
                'labelloc': 't', ## t: top, b: bottom, c: center
                'labeljust': 'c', ## l: left, r: right, c: center
            },
            'node': {
                'shape': 'circle',
                'color': 'lightblue3',
                'label': '',
            },
            'edge':{
                'color': 'black',
                'constraint': 'false',
                'style': 'filled',
            }
        }
        self.add_styles(vLayer, styles)
        vNodes = ['v%d'%i for i in range(self.numVisible)]
        vNodes[-2] = (vNodes[-2], {'label': '...', 'style': '', 'shape': 'circle', 'color':'white'})
        self.add_nodes(vLayer, vNodes)


        hLayer = Graph('cluster_1')
        styles = {
            'graph': {
                'rankdir': 'LR',
                'splines': 'line',
                'label': 'Hidden Units',
                'labelloc': 'b', ## t: top, b: bottom, c: center
                'labeljust': 'c', ## l: left, r: right, c: center
            },
            'node': {
                'shape': 'circle',
                'color': 'red3',
                'label': '',
            },
            'edge':{
                'color': 'black',
                'constraint': 'false',
                'style': 'filled',
            }
        }
        self.add_styles(hLayer, styles)
        hNodes = ['h%d'%i for i in range(self.numHidden)]
        hNodes[-2] = (hNodes[-2], {'label': '...', 'style': '', 'shape': 'circle', 'color':'white'})
        self.add_nodes(hLayer, hNodes)

        g.subgraph(hLayer)
        g.subgraph(vLayer)
        edges = []
        for vn in vNodes:
            for hn in hNodes:
                if isinstance(vn, tuple):
                    if isinstance(hn, tuple):
                        edges.append(((vn[0], hn[0]), {'style':'invis'}))
                    else:
                        edges.append(((vn[0], hn), {'style': 'invis'}))
                else:
                    if isinstance(hn, tuple):
                        edges.append(((vn, hn[0]), {'style':'invis'}))
                    else:
                        edges.append((vn, hn))
        self.add_edges(g, edges)
        print (g.source)
        g.view()


if __name__ == '__main__':
    rbm = RBM(5, 5, 'BT')
    rbm.plot()
