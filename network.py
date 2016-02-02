#!usr/bin/env python
#coding:utf-8


class Network:
    def __init__(self):
        pass

    def add_nodes(self, graph, nodes):
        sortNodes = []
        for n in nodes:
            if isinstance(n, tuple):
                graph.node(n[0], **n[1])
                sortNodes.append(n[0])
            else:
                graph.node(n)
                sortNodes.append(n)
        if len(sortNodes) > 1:
            edges = [((sortNodes[i], sortNodes[i+1]), {'style': 'invis'}) for i in range(len(sortNodes)-1)]
            self.add_edges(graph, edges)
        return graph

    def add_edges(self, graph, edges):
        for e in edges:
            if isinstance(e[0], tuple):
                graph.edge(*e[0], **e[1])
            else:
                graph.edge(*e)
        return graph

    def add_styles(self, graph, styles):
        graph.graph_attr.update(
            ('graph' in styles and styles['graph']) or {}
        )
        graph.node_attr.update(
            ('node' in styles and styles['node']) or {}
        )
        graph.edge_attr.update(
            ('edge' in styles and styles['edge']) or {}
        )
        return graph
