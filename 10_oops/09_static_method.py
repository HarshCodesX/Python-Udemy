class TeaUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

raw = " water , milk , ginger  ,   honey  "
# obj = TeaUtils()
# print(obj.clean_ingredients(raw))
print(TeaUtils.clean_ingredients(raw))