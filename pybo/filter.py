def format_datetime(value, fmt='%Y년 %m월 %d일 %H:%M'): # fmt가 따로 전달되지 않을 경우 저 값을 디폴트로 쓰겠다는 의미
    return value.strftime(fmt)