__author__ = 'N05F3R4TU'

class TempAdd(object):
    """
    The purpose of this object is to add targets as Templates/Scripts to the database so Nimbus has a target to scan
    """
    def __init__(self):
        self.temp_id = ""
        self.temp_name = ""

    def create(self):
        pass

class TempExport(object):
    """
    This class is for export al
    """

    def __init__(self, id=None, name=None):
        self.export_by_id = id
        self.export_by_name = name

    # if name or id; then export(__args, __kwargs)

    def export(self, id=None, name=None):
        pass

class TempDelete(object):
    """
    This class is for Deleting Templates
    """

    def __init__(self, id=None, name=None):
        self.del_by_id = id
        self.del_by_name = name

    # if name or id; then export(__args, __kwargs)

    def delete_template(self, id=None, name=None):
        pass

