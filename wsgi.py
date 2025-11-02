
import importlib.util, os

here = os.path.dirname(__file__)
app_py = os.path.join(here, "app.py")

if os.path.isfile(app_py):
    spec = importlib.util.spec_from_file_location("app_file", app_py)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    app = mod.app          
else:
    from app import app
