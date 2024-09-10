def solution(phone_number):
    star_len = len(phone_number)-4
    answer = "".join(["*" for _ in range(star_len)]) + phone_number[-4:]
    return answer