# необходимое число парт для учащихся трех классов
# input 20, 21, 22
# oytpyt 32
ClassA = int(input("Введите число" ))
ClassB = int(input("Введите число" ))
ClassC = int(input("Введите число" ))

if ClassA% 2 == 0:
    PartClassA = ClassA // 2
else: 
    PartClassA= (ClassA % 2)+ (ClassA // 2)

if ClassB % 2 == 0:
    PartClassB = ClassB // 2
else: 
    PartClassB = (ClassB % 2)+ (ClassB // 2)

if ClassC % 2 == 0:
    PartClassC = ClassC // 2
else: 
    PartClassC = (ClassC % 2)+ (ClassC // 2)
    
print(PartClassA + PartClassB + PartClassC)