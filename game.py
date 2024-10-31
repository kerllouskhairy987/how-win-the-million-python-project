QCounter = 0

secret_ans_1 = "cairo"
secret_ans_2 = "air"
secret_ans_3 = "71%"

ans_1 = ""
ans_2 = ""
ans_3 = ""

name = input("ENTER YOUR USERNAME: ")

while QCounter <= 3:
    ans_1 = input("What is the capital of Egypt? ")
    if secret_ans_1 == ans_1:
        ans_2 = input("What do you love? ")
        if secret_ans_2 == ans_2:
            ans_3 = input("What the percentage of water in the world? ")
            if secret_ans_3 == ans_3:
                print("WINNER YA "+name+" ✅")
                break
            else:
                print("TRY AGAIN ❌")
                QCounter += 1
        else:
            print("TRY AGAIN ❌")
            QCounter += 1
    else:
        QCounter += 1
        if QCounter <= 3:
            print("TRY AGAIN ❌")
        else:
            break

if QCounter >= 4:
    print("LOSER YA "+name+" 🤦‍♂️")