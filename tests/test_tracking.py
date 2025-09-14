import os, sqlite3, subprocess, sys, pathlib, importlib.util

def setup_db(tmp_path):
    db = tmp_path/"orders.sqlite"; env = os.environ.copy(); env["DB_PATH"]=str(db)
    subprocess.check_call([sys.executable,"simulation.py"], cwd=str(pathlib.Path(__file__).parent.parent), env=env)
    return db

def test_on_time_percentage(tmp_path):
    db = setup_db(tmp_path)
    spec = importlib.util.spec_from_file_location("analysis", str(pathlib.Path(__file__).parent.parent/"analysis.py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    conn = sqlite3.connect(db); pct = mod.on_time_percentage(conn)
    assert 0 <= pct <= 100
