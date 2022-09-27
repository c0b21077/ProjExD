import random
import time

all_alphabet = 26
alpha_TAISHOU = 10
alpha_KESSON = 2
try_number = 2

def shutudai(alphabet):

    print("対象文字：")
    taishou = random.sample(alphabet, alpha_TAISHOU)
    for t in sorted(taishou):
        print(t, end = " ")
    print()
    
    print("表示文字：")
    kesson = random.sample(taishou, alpha_KESSON)
    for k in taishou:
        if k not in kesson:
            print(k, end = " ")
    print()
    return kesson
    
def kaito(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？："))
    if num == alpha_KESSON:
        print("正解です。\nそれでは、具体的に欠損文字を一つずつ入力してください。")
        for i in range(num):
            moji = input(f"{i + 1}つ目の文字を入力してください：")

            if moji not in seikai:

                print("不正解です。またチャレンジしてください。")
                return False
            else:
                seikai.remove(moji)
        else:
            print("完全正解です！！！")
            return True
    else:
        print("不正解です。")
    
    return False

if __name__ == "__main__":
    start_time = time.time()
    alphabet = [chr(i + 65) for i in range(all_alphabet)]

    for _ in range(try_number):
        abs_char = shutudai(alphabet)  
        ret = kaito(abs_char)
        if ret:
            break
        else:
            print("-"*20)
    end_time = time.time()
    print(f"[経過時間：{(end_time - start_time):.2f}秒]")
