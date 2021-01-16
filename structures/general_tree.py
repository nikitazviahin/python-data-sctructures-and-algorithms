class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def spacer(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        return prefix

    def print_tree(self, variant):
        if variant == 'first':
            prefix = self.spacer()
            print(prefix + self.data[0])
            if self.children:
                for child in self.children:
                    child.print_tree(variant)

        if variant == 'second':
            prefix = self.spacer()
            print(prefix + self.data[1])
            if self.children:
                for child in self.children:
                    child.print_tree(variant)

        if variant == 'both':
            sprefix = self.spacer()
            print(prefix + self.data[0] + ' (' + self.data[1] + ')')
            if self.children:
                for child in self.children:
                    child.print_tree(variant)



def build_product_tree():
    root = TreeNode(["Electronics", 'Second param'])

    laptop = TreeNode(["Laptop",'Second param'] )
    laptop.add_child(TreeNode(["mac", 'Second param']))
    laptop.add_child(TreeNode(["thinkpad", 'Second param']))
    laptop.add_child(TreeNode(["Surface", 'Second param']))

    cellphone = TreeNode(["Cell Phone",'Second param'])
    cellphone.add_child(TreeNode(["iPhone", 'Second param']))
    cellphone.add_child(TreeNode(["Google pixel",'Second param']))
    cellphone.add_child(TreeNode(["Vivo",'Second param']))

    root.add_child(laptop)
    root.add_child(cellphone)
    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree('first')
    root.print_tree('second')
    root.print_tree('both')