import view as v
import module as m


def create_contact():
    return m.create(v.add_new())

def find_contact():
    return m.find(v.find_phone())

def export_contact():
    return m.export()
