class Compound:
    def __init__(self, name, xrefs):
        self.name = name
        self.xrefs = set(xrefs)

    def merge(self, other):
        # TODO: name
        self.xrefs.update(other.xrefs)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return any([x in other.xrefs for x in self.xrefs])

    def __str__(self):
        return '%s {name: \'%s\', xrefs: %s}' % (type(self).__name__, self.name, sorted(self.xrefs))
