from theaters import load_theaters, get_theater

assert get_theater(1) is not None
assert get_theater(999) is None
assert len(load_theaters()) == 5
assert get_theater(1)["name"] == "PVR Vegas Dwarka"   

print("All tests passed")
