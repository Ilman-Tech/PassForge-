import random
import time

def main():
    
    """
        صفحه ای ورود.
        1 استارت بازی
        2 توضیحات بازی
        3 خروج از بازی
    """
    while True:
        
        print("""

hi welcome to my game!          
[1] start game.
[2] fqa game.
[3] exit game.
          """)
        try:
            choice = int(input('select a number: '))
        except ValueError:
            print('\nplease enter numeric value.')
            
        # انتخاب 1 تابع استارت گیم رو شروع میکنه
        if choice == 1:
            start_game()
        # انتخاب 2 تابع توضیحات
        elif choice == 2:
            fag_game()
        else:
            print('ok bye🎈') 
            exit()
        
def start_game():

    # اول یک عدد بین 1 تا 100 انتخاب میکنی
    guess = random.randint(1, 100)
    # تعداد تلاش
    attempts = 0
    # جون کاربر
    max_attempts = 5

    print('lest go game')
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print('\nGame is start good luck😉')
    
    while True:
        try:
            choice = int(input('guess number: '))
        except ValueError:
            print('please enter numeric value!')
        
        # اکر انتخاب عدد کوچکتر از یک بود دوباره بیا ازش حدس رو بپرس
        if choice < 1:
            print('please select guess number  < 1.')
            continue
        # و همچنان اگر عدد کاربر بزرگتر از 100 بود بیاد دوباره ازش حدس عددش رو بگیره
        elif choice > 100:
            print('please select guees number > 100.')
            continue
            
        # توی انتهاب هر عدد تعداد تلاش یدونه زیاد میشه و از جون کاربر کم میشه 
        attempts += 1
        result_atp = max_attempts - attempts
    
        # اگر گیس بزرگتر از عدد انتخابی بود بیا بگو بیشتر   
        if guess > choice:
            print(f'Heal : {result_atp}, cursor: Hight!')
        # اکر عدد انتخابی بزرگتر از گیس بود بیا بگو گمتر
        elif guess < choice:
            print(f'Heal : {result_atp}, cursor: Lower!')
        # اگر مساوی شد کاربر برنده بازی میشه
        else:
            print(f'''
hey you WIN😍
your attempts: [{attempts}].
        ''')
            # وقتی برنده بشه تابع اصلی دوباره اجرا میشه
            main()

        # اینجا جون کاربر تموم بشه میبازه و ازش میپرسه دوباره میخوای بازی کنی یا نه 
        if result_atp == 0:
            print('''
ho sorry you lose😥.
[1] play again.
[2] give up.
''')
            try:
                selct = int(input('choice number: '))
            except ValueError:
                print('please enter numeric value!')
                
            if selct == 1:
                start_game()
            else:
                while True:
                    # ازش میپرسبم واقعا میخوای از بازی لفت بدی
                    jadi = input('you verle left is game your screen [y/n]? ').lower().strip()

                    if jadi == 'y':
                        print('ok men you screen😒\n')
                        exit()
                    elif jadi == 'n':
                        print('i belive you good luck😍')
                        start_game()
                    else:
                        print('wtf men not hrad type y or n...')
                    
                        
def fag_game():
    """
        این تابع فقط نقشش اینه توضیحات بازی رو به کاربر نشون بده
    """
    print("""
im select a number between 1 and 100, you guess my number! 
you in the game heal 5. if your heal equel 0 you lose game.
Good luck.\n
          """)
    
    main()

if __name__ == "__main__":
    main()