"""
drop down color not working in firefox
"""

from tailwind_tags import *
import ofjustpy as oj
from addict import Dict
import justpy as jp
from ofjustpy_svelte_tailwind_components.ChartJS import  ChartJS_
import ofjustpy_react as ojr
app = jp.build_app()

def on_btn_click(dbref,msg):
    pass


def launcher(request):
    session_manager = oj.get_session_manager(request.session_id)
    with oj.sessionctx(session_manager):
        #achartjs_ = ChartJS_("achartjs", text="something")
        cjs_ = ChartJS_("mychart",
                chart_name = "Pop chart",
                reactctx = [ojr.Ctx("/options/scales/x/title/text",
                                    lambda x: True,
                                    ojr.UIOps.UPDATE_CHART
                                    )
                            ]
                )
        chart_cbox_ = oj.Div_("cbox", cgens=[cjs_], pcp = [ppos.relative])
        def on_btn_click(dbref, msg):
            print('btn clicked')
            #cjs_.target.update_chart("/scales/x/title/text", "new_value")
            
        update_btn_ = oj.Button_("abtn", text="Update Chart").event_handle(oj.click, on_btn_click)
        colorselector_ = oj.ColorSelector_(
            "colorselector").event_handle(
                        oj.click, on_btn_click)
                
        #cbox_ = chart_in_box()
        wp_ = oj.WebPage_("oa", cgens =[chart_cbox_,
                                        update_btn_,
                                        colorselector_], template_file='svelte.html', title="myoa")
        wp = wp_()
    return wp


app.add_jproute("/", launcher)



#jp.justpy(launcher, start_server=False)
# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')
