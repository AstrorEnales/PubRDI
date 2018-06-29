class Reference:
    def __init__(self, pmid, doi, citation):
        self.pmid = pmid
        self.doi = doi
        self.citation = citation

    def __hash__(self):
        return hash((self.pmid, self.doi, self.citation))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.pmid == other.pmid or self.doi == other.doi or self.citation == other.citation

    def __str__(self):
        return '%s {pmid: \'%s\', doi: \'%s\', citation: \'%s\'}' % (
            type(self).__name__, self.pmid, self.doi, self.citation)
