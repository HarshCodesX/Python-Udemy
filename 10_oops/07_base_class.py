class Tea:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# class GingerTea(Tea):
#     def __init__(self, type_, strength, spice_level):
#         Tea.__init__(self, type_, strength)
#         self.spice_level = spice_level

class GingerTea(Tea):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level