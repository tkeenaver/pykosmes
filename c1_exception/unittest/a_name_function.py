def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

if __name__ == '__main__':
    print('\n이 파일은 함수 get_formatted_name의 구현 부분이며, 단순 실행코드는 없습니다.\n')
