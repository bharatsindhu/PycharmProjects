'''tuna = input("whats your fav. number !!!")

print(tuna)'''


while True:
    try:
        num = int(input("whats your favourite num!!! \n"))

        print(18/num)
        break
    except ValueError:
        print("enter number only")
    except ZeroDivisionError:
        print("not divisible by zero")
    except:
        break
    finally:
        print("complete")