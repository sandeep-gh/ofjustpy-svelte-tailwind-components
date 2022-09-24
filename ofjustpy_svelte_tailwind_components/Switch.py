from addict import Dict
import justpy as jp
from justpy import JustpyBaseComponent
from justpy import WebPage
from tailwind_tags import *
from dpath.util import get as dget, set as dset

from ofjustpy.htmlcomponents import genStubFunc 



class Switch(JustpyBaseComponent):
    vue_type = 'Switch'
    # chart_types = [] #TODO
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = kwargs.pop('text', None)
        self.initialize(**kwargs)
        
    def react(self, data):
        """
        called every time before object is rendered
        """
        pass
    def __repr__(self):
        return f'{self.__class__.__name__}(id: {self.id}, vue_type: {self.vue_type})'

    def convert_object_to_dict(self):
        d = {}
        d['vue_type'] = self.vue_type
        # Add id if CSS transition is defined
        d['id'] = self.id
        d['text'] = self.text 
        return d
    
Switch_ = genStubFunc(Switch, [])
