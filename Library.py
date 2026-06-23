class Library():
    def Subfields():
        list=["Machine Learning", "Neural Networks", "Vision Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for tem in list:
            print(tem)
            sub=("tem")
        return sub
    def OddEven():
        number=int(input("Enter a number:"))
        if((number%2)==0):
            print(number," is Even number ")
            cate=(number," is Even number ")
        else:
            print(number," is Odd number ")
            cate=(number," is Odd number ")
        return cate
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male" and age<21):
            print("NOT ELIGIBLE")
            Ele=("NOT ELIGIBLE")
        elif(gender=="Female" and age<18):
            print("NOT ELIGIBLE")
            Ele=("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")
            Ele=("ELIGIBLE")
        return Ele
    def percentage():
         sub1=int(input("Subject1="))
         sub2=int(input("Subject2="))
         sub3=int(input("Subject3="))
         sub4=int(input("Subject4="))
         sub5=int(input("Subject5="))
         add=(sub1+sub2+sub3+sub4+sub5)
         print("Total:",add)
         per=("Total:",add)
         add1=5
         result=(add/add1)
         print("Percentage:",result)
         per=("Percentage:",result)
         return per
    def triangle():
        imput1=int(input("Height:"))
        imput2=int(input("Breadth:"))
        mul=(imput1*imput2)
        mul2=2
        mul3=(mul/mul2)
        print("Area of Triangel:",mul3)
        num=("Area of Triangel:",mul3)
        imput3=int(input("Height1:"))
        imput4=int(input("Height2:"))
        imput5=int(input("Breadth:"))
        perimeterformula=(imput3+imput4+imput5)
        print("Perimeter of Triangle:",perimeterformula)
        num=("Perimeter of Triangle:",perimeterformula)
        return num
