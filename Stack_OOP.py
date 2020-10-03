class Stack:

    def __init__(self):

        print("append is using for entering the value in list")
        print("pop is use to del the value in the list from the end")

    def enter_fruit(self):
        self.L_list = []
        x = 0
        temp = 0
        while x <= 4:
            temp = input("enter the value" + str(x + 1) +" "+ "L_list"+" "+":")
            self.L_list.append(temp)
            print(self.L_list)
            x = x + 1

        return self.L_list

    def remove_fruit(self):
        i = 0
        x = 5
        while i <= 4:
            print("del value at end " +" "+ "L_list"+ ":")
            self.L_list.pop()
            print(self.L_list)
            i = i + 1
        return self.L_list


s1 = Stack()
print("append the values into the list :",s1.enter_fruit())
print("pop the values into the list :", s1.remove_fruit())