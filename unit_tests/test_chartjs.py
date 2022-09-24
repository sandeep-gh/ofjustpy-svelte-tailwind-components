"""
drop down color not working in firefox
"""

from tailwind_tags import *
import ofjustpy as oj
from addict import Dict
import justpy as jp
from ofjustpy_svelte_tailwind_components.ChartJS import  ChartJS_, chart_in_box



def on_btn_click(dbref,msg):
    pass


def launcher(request):
    session_manager = oj.get_session_manager(request.session_id)
    with oj.sessionctx(session_manager):
        #achartjs_ = ChartJS_("achartjs", text="something")
        cbox_ = chart_in_box()
        wp_ = oj.WebPage_("oa", cgens =[cbox_], template_file='svelte.html', title="myoa")
        wp = wp_()
        print (cbox_.target.components)
    return wp

jp.Route("/", launcher)



app = jp.app
#jp.justpy(launcher, start_server=False)
# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')
