from nose.tools import *
from app import app

app.config["TESTING"] = True
web = app.test_client()

def test_route8():
    rv = web.get("/", follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)

    data = {"action": "*"}
    rv = web.post("/game", follow_redirects=True, data=data)
    assert_in(b"Central Corridor", rv.data)