class CustomSet:
    def __init__(self):
        self.items = []

    def add(self, item: any):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item: any):
        if item in self.items:
            self.items.remove(item)
        else:
            raise KeyError(f"{item} is not in the set")

    def as_list(self):
        return self.items

    def clear(self):
        self.items = []

def main():
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    my_set.clear()

    my_set.add("item 5")
    my_set.add("item 6")
    my_set.add("item 7")
    try:
        my_set.remove("item 4")
    except KeyError:
        print("item not removed moving forward")
    print(my_set.as_list())
main()
