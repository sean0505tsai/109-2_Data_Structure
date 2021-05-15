import sys

class Student:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.next = None

ptr = None
current = None
prev = None

head = Student()
head.next = None

def delete_form():
    global head
    global current
    global prev

    delete_name = ""
    if head.next == None:
        print("鏈結是空的")
    else:
        delete_name = input("輸入要刪除學生的姓名:")
        prev = head
        current = head.next
        while current != None and delete_name != current.name:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
            current = None
            print("已刪除學生 %s的資料" % delete_name)
        else:
            print("查無學生 %s的資料" % delete_name)

def insert_form():
    global ptr
    global current
    global prev
    global head

    ptr = Student()
    ptr.next = None
    ptr.name = input("輸入學生姓名 :")
    ptr.score = eval(input("輸入該學生分數:"))
    print()

    prev = head
    current = head.next
    while current != None and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr        
        

def display_form():
    global current
    global head

    count = 0
    if head.next == None:
        print("鏈結是空的")
    else:
        print("%5s %5s" % ("姓名", "分數"))
        for i in range(10):
            print("=", end = "")
        print()
        current = head.next
        while current != None:
            print("%5s %5d" % (current.name, current.score))
            count = count + 1
            current = current.next
        for i in range(10):
            print("=", end = "")
        print()
        print("有 %d 筆資料" % count)

def main():
    option = 0
    while True:
        print("------")
        print("1.新增")
        print("2.刪除")
        print("3.顯示")
        print("4.結束")
        print("------")
        
        try:
            option = int(input("選擇執行項目:"))
        except ValueError:
            print("無此選項")
            print("Please try again.")
            

        print()
        if option == 1:
            insert_form()
        elif option == 2:
            delete_form()
        elif option == 3:
            display_form()
        elif option == 4:
            sys.exit(0)

main()