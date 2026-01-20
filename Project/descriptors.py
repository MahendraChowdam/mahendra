class MarksDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if all(0 <= m <= 100 for m in value):
            obj.__dict__[self.name] = value
        else:
            raise ValueError("Marks should be between 0 and 100")


class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj.__dict__["_salary"] = value
