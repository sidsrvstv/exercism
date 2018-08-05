NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if len(data) > 0:
            self.checkData(data)
            for d in data:
                if d[0] == 0:
                    node = Node(d[1], d[2])
                    self.nodes.append(node)
                elif d[0] == 1:
                    edge = Edge(d[1], d[2], d[3])
                    self.edges.append(edge)
                elif d[0] == 2:
                    self.attrs[d[1]] = d[2]
                    

    def checkData(self, data):
        for i in data:
            if not isinstance(i, tuple):
                raise Exception("Expected type tuple")
            if len(i) != 3 or len(i) != 4:
                raise Exception("Length of tuple is improper")
            if i[0] not in {"NODE", "ATTR", "EDGE"}:
                raise Exception("Type (Node, Edge, Attr) not specified")
            if i[0] == "NODE":
                if len(i) != 3:
                    raise Exception("Node type should have a tuple of lenght 3")
                if not isinstance(i[1], str):
                    raise Exception("Node name should be a string")
                if not isinstance(i[2], dict):
                    raise Exception("Node attributes should be dict type")
            elif i[0] == "EDGE":
                if len(i) != 4:
                    raise Exception("Edge type should have a tuple of lenght 4")
                if not isinstance(i[1], str):
                    raise Exception("Edge vertex should be a string")
                if not isinstance(i[2], str):
                    raise Exception("Edge vertex should be a string")
                if not isinstance(i[3], dict):
                    raise Exception("Edge attributes should be dict type")
            elif i[0] == "ATTR":
                if len(i) != 3:
                    raise Exception("Attr type should have a tuple of lenght 3")
                if not isinstance(i[1], str):
                    raise Exception("Attr name in index 1 should be a string")
                if not isinstance(i[2], str):
                    raise Exception("Attr name in index 2 should be a string")

                
        
