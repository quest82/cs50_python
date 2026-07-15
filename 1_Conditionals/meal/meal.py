
def main():
    time = input("What time is it? ")
    total_time = convert(time)

    if total_time >= 7 and total_time <= 8:
        print('breakfast time')
    elif total_time >= 12 and total_time <= 13:
        print('lunch time')
    elif total_time >= 18 and total_time <= 19:
        print('dinner time')


def convert(x):
    hours, minutes = x.split(':')
    if int(minutes) > 59 :
        print("Minutes should range from 0 - 59")
    
    converted_time = round((int(minutes) / 60) + int(hours), 2)
    return converted_time

    
    


# def convert(x):
#     if x.startswith('0'):
#         if x[1] == '7' or (x[1] == '8' and x[2] == '0' and x[3] == '0'):
#             print('breakfast time')
#     elif x.startswith('12') or (x.startswith('13') and x[2] == '0' and x[3] == '0'):
#         print('lunch time')
#     elif x.startswith('18') or (x.startswith('19') and x[2] == '0' and x[3] == '0'):
#         print('lunch time')




if __name__ == "__main__":
    main()