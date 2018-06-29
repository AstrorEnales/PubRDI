import json
import io

from compound import Compound
from drug import Drug
from enzyme import Enzyme
from reference import Reference
from remedy import Remedy
from transporter import Transporter


class PublicationDataFile:
    def __init__(self, filepath):
        with io.open(filepath, 'r', encoding='utf-8') as f:
            self.raw = json.load(f)
        self.compounds = [Compound(x['name'], x['xrefs']) for x in self.raw['compounds']]
        self.remedies = [Remedy(x['name'], x['xrefs']) for x in self.raw['remedies']]
        self.enzymes = [Enzyme(x['name'], x['xrefs']) for x in self.raw['enzymes']]
        self.transporter = [Transporter(x['name'], x['xrefs']) for x in self.raw['transporter']]
        self.drugs = [Drug(x['name'], x['xrefs']) for x in self.raw['drugs']]
        self.publication = Reference(self.raw['publication']['pmid'], self.raw['publication']['doi'],
                                     self.raw['publication']['citation'])
