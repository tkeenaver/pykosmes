my_list = [1, 2, 3]
try:
    print("my_list = [1, 2, 3]")
    index = int(input("첨자를 입력하세요: "))
    #print(my_list[index]/0)
    for i in range(100000):
        print(i, end=' ')
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("잘못된 첨자입니다.")
except ValueError:
    print("숫자를 입력하세요")
except KeyboardInterrupt:
    print("KeyboardInterrupt!")
'''