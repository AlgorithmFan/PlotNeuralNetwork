#!usr/bin/env python
#coding:utf-8

'''
Author: Haidong Zhang
E-mail: haidong_zhang13@163.com
Date: 2016.1.31
'''

from graphviz import Graph, Digraph
from network import Network

class DBN(Network):
    def __init__(self, numList, direction = 'TB'):
        '''
        numList: the number of hidden units;
        direction: the direction
            LR: from left to right;
            RL: from right to left;
            TB: from top to bottom;
            BT: from bottom to top;
        '''
        self.numList = numList
        self.direction = direction

    def plot(self):
        g = Digraph(format='png')

        # g.graph_attr['rankdir'] = self.direction
        # g.graph_attr['splines'] = 'line'

        vLayer = Digraph('cluster_0')
        self.add_nodes(vLayer, ['v1', 'v2',])
        vLayer.body.append('label="Visible Units"')

        h1Layer = Digraph('cluster_1')
        self.add_nodes(h1Layer, ['h11', 'h12', ])
        h1Layer.body.append('label="Visible Units"')

        h2Layer = Digraph('cluster_2')
        self.add_nodes(h2Layer, ['h21', 'h22',])
        h2Layer.body.append('label="Visible Units"')

        h3Layer = Digraph('cluster_3')
        self.add_nodes(h3Layer, ['h31', 'h32',])
        h3Layer.body.append('label="Visible Units"')

        g.subgraph(vLayer)
        g.subgraph(h1Layer)
        g.subgraph(h2Layer)
        g.subgraph(h3Layer)

        self.add_edges(g, [('h11', 'v1'), ('h11', 'v2'), ('h12', 'v1'), ('h12', 'v2'),
                           ('h21', 'h11'), ('h21', 'h12'), ('h22', 'h11'), ('h22', 'h12'),
                            ])

        styles = {
            'edge':{
                'dir': 'none'
            }
        }
        # self.add_styles(g, styles)
        self.add_edges(g, [(('h31', 'h21'), {'dir': 'none'}), (('h31', 'h22'), {'dir': 'none'}),
                           (('h32', 'h21'), {'dir': 'none'}), (('h32', 'h22'), {'dir': 'none'}),])

        print(g.source)
        g.view()


if __name__ == '__main__':
    dbn = DBN(3, 4)
    dbn.plot()
