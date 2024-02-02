friends = ["Jared", "Joseph", "John", "Jeremy"]
family = ["Manuel", "Martha", "Megan", "Miga"]


while True:
    answer = input("Who is in your friends list: ")
    if answer in friends:
        print("Yes, that person is in your friends list.")
    else:
        print("No, that person is not in your friends list.")

    cont = input("Print do you wish to proceed? yes/no? ")
    if cont.lower() != "yes":
        break
