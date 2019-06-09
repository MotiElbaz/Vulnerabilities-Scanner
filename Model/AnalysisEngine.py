from threading import Lock
import networkx as nx
import Objects.Vulnerability as Vulnerability
import matplotlib.pyplot as plt


class AnalysisEngine(object):
    _instance = None

    def getShortestPath(self, graph, source, target):
        """
        Searching shortest path to target from internet node.
        """
        plt.close()
        try:
            path = nx.shortest_path(graph, source=source, target=target)
        except:
            return "Path not found."
        labels = dict()
        for i in path:
            if isinstance(i, Vulnerability.Vulnerability):
                labels[i] = i.shortDesc
            else:
                labels[i] = i.label
        G = nx.DiGraph()
        path_edges = list(zip(path, path[1:]))
        G.add_nodes_from(path)
        G.add_edges_from(path_edges)
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, labels=labels, with_labels=True)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='b', labels=labels, with_labels=True)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='b', width=5)
        plt.savefig('Images//short.png', format='PNG')

    def getVulnerablePath(self, graph, source, target):
        """
        Searching vulnerable path to target from internet node.
        """
        plt.close()
        try:
            path = nx.dijkstra_path(graph, source=source, target=target, weight='weight')
        except:
            return "Path not found."
        labels = dict()
        for i in path:
            if isinstance(i, Vulnerability.Vulnerability):
                labels[i] = i.shortDesc
            else:
                labels[i] = i.label
        G = nx.DiGraph()
        path_edges = list(zip(path, path[1:]))
        G.add_nodes_from(path)
        G.add_edges_from(path_edges)
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, labels=labels, with_labels=True)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='y', labels=labels, with_labels=True)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='y', width=5)
        plt.savefig('Images//vule.png', format='PNG')

    def getExposeComponent(self, graph):
        """
        Searching expose component to target from internet node.
        """
        plt.close()
        labels = dict()
        G = nx.DiGraph()
        path = sorted(graph.degree(), key=lambda x: x[1], reverse=True)
        node = path[0][0]
        if isinstance(node, Vulnerability.Vulnerability):
            labels[node] = node.shortDesc
        else:
            labels[node] = node.label
        G.add_node(node)
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, labels=labels, with_labels=True)
        plt.savefig('Images//expose.png', format='PNG')

    def __new__(cls, *args, **kwargs):
        if AnalysisEngine._instance is None:
            with Lock():
                if AnalysisEngine._instance is None:
                    AnalysisEngine._instance = super().__new__(cls, *args, **kwargs)

        return AnalysisEngine._instance
