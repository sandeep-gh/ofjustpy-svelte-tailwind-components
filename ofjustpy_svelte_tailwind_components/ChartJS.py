from addict import Dict
import justpy as jp
from justpy import JustpyBaseComponent
from justpy import WebPage
from tailwind_tags import *
from dpath.util import get as dget, set as dset
import hjson
from ofjustpy.htmlcomponents import genStubFunc 
import ofjustpy  as oj

# Dict(hjson.loads("""
#        {
#         "responsive": true,
#         "aspectRatio": 2,
#         "resizeDelay": 4,
#         "devicePixelRatio": 1,
#         "parsing": false,
#         "plugins": {
#           "legend": {
#             "position": "top"
#           },
#           "title": {
#             "display": true,
#             "text": "plot_title"
#           }
#         },
#         "elements": {
#           "line": {
#             "tension": 0,
#             "backgroundColor": null,
#             "borderWidth": 2,
#             "borderColor": null,
#             "capBezierPoints": true
#           }
#         },
#         "scales": {
#           "xAxis": {
#             "grid": {
#               "display": true
#             }
#           }
#         }
#       }
# """.encode("ascii", "ignore")))


# Dict(hjson.loads("""
#         {
#          "dataset": [
#       {
#         "label": "ds1",
#         "data": [
#           {
#             "x": 1,
#             "y": 3
#           },
#           {
#             "x": 5,
#             "y": 5
#           }
#         ],
#         "line": {
#           "borderColor": "#25be45",
#           "backgroundColor": "#25be45"
#         }
#       },
#       {
#         "label": "ds2",
#         "data": [
#           {
#             "x": 1,
#             "y": 7
#           },
#           {
#             "x": 5,
#             "y": 2
#           }
#         ],
#         "borderColor": "#996742",
#         "backgroundColor": "#996742"
#       },
#       {
#         "label": "ds3",
#         "data": [
#           {
#             "x": 1,
#             "y": 0
#           },
#           {
#             "x": 5,
#             "y": 8
#           }
#         ],
#         "borderColor": "#a7826e",
#         "backgroundColor": "#a7826e"
#       },
#       {
#         "label": "ds4",
#         "data": [
#           {
#             "x": 1,
#             "y": 13
#           },
#           {
#             "x": 5,
#             "y": 2
#           }
#         ],
#         "borderColor": "#a98b87",
#         "backgroundColor": "#a98b87"
#       },
#       {
#         "label": "ds5",
#         "data": [
#           {
#             "x": 1,
#             "y": 2
#           },
#           {
#             "x": 5,
#             "y": 6
#           }
#         ],
#         "borderColor": "#9d8291",
#         "backgroundColor": "#9d8291"
#       }
#     ],
#     "labels": "[1,2,4,5]"
#   }

# """))

# chart_options = Dict(hjson.loads("""
# {
# title: {
# display: true,
# text: 'World population per region (in millions)'
# }
# options: {
# scales: {
# x: { title: { text: "xlabel", display: true}
# }
# }
# }
# }
                           
# """))
# chart_options = Dict(hjson.loads("""

# {
#     title: {
#       display: true,
#       text: 'World population per region (in millions)'
#     },
#     scales : {
#       x: {  title: { text: "hello", display: true}}
#     }
    
#   }"""
# ))

# We need options to be part of json.
# to handle updates coming from chartjs-customizer
chart_options = Dict(hjson.loads("""
{options: {
    title: {
      display: true,
      text: 'World population per region (in millions)'
    },
    scales : {
      x: {  title: { text: "hello", display: true}}
    }
    
  }
}"""
))      
      
#                )
# chart_options = Dict(hjson.loads("""
# {'title': {'display': True, 'text': 'World population per region (in millions)'}, 'options': {'scales': {'x': {'axis': 'new-axis-boos'}}}}"""
#                                  )
#                      )


chart_data = Dict(hjson.loads(
"""
{
                               labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
                               datasets: [{ 
                                 data: [86,114,106,106,107,111,133,221,783,2478],
                                 label: "Africa",
                                 borderColor: "#3e95cd",
                                 fill: false
                               }, { 
                                 data: [282,350,411,502,635,809,947,1402,3700,5267],
                                 label: "Asia",
                                 borderColor: "#8e5ea2",
                                 fill: false
                               }, { 
                                 data: [168,170,178,190,203,276,408,547,675,734],
                                 label: "Europe",
                                 borderColor: "#3cba9f",
                                 fill: false
                               }, { 
                                 data: [40,20,10,16,24,38,74,167,508,784],
                                 label: "Latin America",
                                 borderColor: "#e8c3b9",
                                 fill: false
                               }, { 
                                 data: [6,3,2,2,7,26,82,172,312,433],
                                 label: "North America",
                                 borderColor: "#c45850",
                                 fill: false
                               }
                                         ]
                             }
"""
    ))


class ChartJS(JustpyBaseComponent):
    vue_type = 'ChartJS'
    # chart_types = [] #TODO
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize(**kwargs)
        self.chart_name = kwargs.pop('chart_name')
        # TODO: the refactoring in htmlcomponents for classes is little off 
        self.twsty_tags = kwargs.get('twsty_tags', [])
        if not self.twsty_tags:
            self.classes = ""
        else:
            self.classes = tstr(*self.twsty_tags)

        #TODO: should derive from base component 
        self.style = ""
    def react(self, data):
        """
        called every time before object is rendered
        """
        pass
    def __repr__(self):
        return f'{self.__class__.__name__}( vue_type: {self.vue_type})'


    def update_chart(self, spath, value):
        try:
            oj.dupdate(chart_options, spath, value)
        except Exception as e:
            # uvicorn runtime without Crash can eat up exception
            print ("exception in chart_update ", e)
            raise e
                                 
        
    def convert_object_to_dict(self):
        print ("chartJS: convert_object_to_dict: ",  chart_options)
        d = {}
        d['vue_type'] = self.vue_type
        # Add id if CSS transition is defined
        d['id'] = self.id

        d['chart_type'] = 'line'
        
        d['chart_options'] = chart_options.options
        
        d['chart_data'] =  chart_data

        d['chart_name'] = self.chart_name

        d['canvas_id'] = "canvas_" + self.chart_name
        d['show'] = True

        d['events'] = self.events

        d['classes'] = self.classes
        d['style'] = self.style
        
        
        return d
    
ChartJS_ = genStubFunc(ChartJS, [])

# def chart_in_box():
#     cjs_ = ChartJS_("mychart", chart_name = "Pop chart")
#     chart_cbox_ = oj.Div_("cbox", cgens=[cjs_], pcp = [ppos.relative])
#     return chart_cbox_
