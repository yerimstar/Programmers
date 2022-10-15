def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        if len(phone_book[i-1]) < len(phone_book[i]) and phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            return False
    return True
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#     print(phoneBook[1:])
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
#
# print(solution(["119", "97674223", "1195524421"]))