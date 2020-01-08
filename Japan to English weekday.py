print("-------------------------------------")
print("English to Japan translator(Weekdays)") #title
print("-------------------------------------")
a = input("What day do you want to translate?:")

def main():
    if a == "monday":
        print("月曜日")
    elif a == "tuesday":
        print("火曜日")
    elif a == "wednesday":
        print("水曜日")
    elif a == "thursday":
        print("木曜日")
    elif a == "friday":
        print("金曜日")
    elif a == "saturday":
        print("土曜日")
    elif a == "sunday":
        print("日曜日")
    else:
        print("That is not a weekday.")


if __name__ == "__main__":
	main()        

    
    
    
