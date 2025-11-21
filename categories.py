class CategoryManager:
    def __init__(self):
        self.categories = []

    def add_category(self, name):
        self.categories.append(name)
        print(f"Категория '{name}' добавлена!")

    def list_categories(self):
        print("Доступные категории:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}, {category}")

"""Some new changes in main"""
