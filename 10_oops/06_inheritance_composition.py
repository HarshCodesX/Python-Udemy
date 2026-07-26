class BaseTea:
    temperature = "hot"
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} Tea!")

class GingerTea(BaseTea):
    def add_spices(self):
        print(f"Adding cardamom, ginger and cloves")

# spcl_tea = GingerTea("Lemon")
# spcl_tea.prepare()
# spcl_tea.add_spices()

class TeaShop:
    tea_cls = BaseTea
    def __init__(self):
        self.tea = self.tea_cls("Regular")

    def serve(self):
        print(f"Serving {self.tea.type} tea")
        self.tea.prepare()

class FancyTeaShop(TeaShop):
    tea_cls = GingerTea

shop = TeaShop()
fancy = FancyTeaShop()

shop.serve()
fancy.serve()
fancy.tea.add_spices()