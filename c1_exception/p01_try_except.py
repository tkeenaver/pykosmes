import sys
import traceback

try:
    print(1/0)
#except ZeroDivisionError:
#    print("ZeroDivisionError 예외가 발생했습니다.")
#except ArithmeticError:
#    print("ArithmeticError 예외가 발생했습니다.")
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("예외 종류:", exc_type.__name__)
    print(f'{exc_type=}')
    print(f'{exc_value=}')
    print(f'{exc_traceback=}')
    traceback.print_tb(exc_traceback)
print("Hello")
