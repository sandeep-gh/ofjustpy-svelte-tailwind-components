"""
drop down color not working in firefox
"""

from tailwind_tags import *
import ofjustpy as oj
from addict import Dict
import justpy as jp
from ofjustpy_svelte_tailwind_components.Switch import Switch_
from ofjustpy_svelte_tailwind_components. import Switch_


def on_btn_click(dbref,msg):
    pass


def launcher(request):
    session_manager = oj.get_session_manager(request.session_id)
    with oj.sessionctx(session_manager):
        aswitch_ = Switch_("myswitch", text="something")
        wp_ = oj.WebPage_("oa", cgens =[aswitch_], template_file='svelte.html', title="myoa")
        wp = wp_()
        
    return wp

jp.Route("/", launcher)



app = jp.app
#jp.justpy(launcher, start_server=False)
# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')
