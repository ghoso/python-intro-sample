#
# generator.py
#
while True:
    key_in = input("(“[偶数を出力: 1, 奇数を出力:2,終了:q] ")
    if key_in == 'q':
        break
        
    for i in range(0,20,3):
        if key_in == '1':
            if  i % 2 == 0:
                print(i)
        elif key_in == '2':
            if i % 2 != 0:
                print(i)