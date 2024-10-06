def palindromic_finder(s, length, count, length_count, list):
    while length_count != 0:   
        for i in range(length):
            sub_s = s[count:length_count]
            print(sub_s)
            count += 1
            if count == length:
                length_count -= 1
                count = 0
                print(length_count)
            if (len(sub_s) >= 2) & (sub_s[::-1] == sub_s):
                list.append(sub_s)

    print("Here is your list: ")
    print(list)


s = input("Enter a random string of letters to find the palinromic substrings: ")

length = len(s)
count = 0
rev_string = s[::-1]
length_count = length
list = []

palindromic_finder(s, length, count, length_count, list)