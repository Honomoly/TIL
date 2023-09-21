# 가변길이 매개변수 (Variadic Arguments : *players)
# 리스트 형식을 따름

def show_players(*players):
    for player in players:
        print(player, end=' ')
    print()

show_players('홍길동')
show_players('홍길동', '이몽룡')
show_players('홍길동', '이몽룡', '성춘향')