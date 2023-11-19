"""
File: caseSolution.py
Author: Mirjam Liodden
Date: 18.11.2023

"""

import json

def strToTime(class_data):
    tid = []
    for i in class_data:
        time = i['zonedStartTime']['dateTime']
        tid.append(time[-9:-4])
    return tid

def OrganizedBooking():

    with open('response.json', 'r') as f:                     
        data = json.loads(f.read())
        f.close()

    class_data = data['results']

    participationId = input('Please write your participation Id: ')
    print(f'\nWelcome {participationId}\n'
          f'Here is all GX classes for the evening:\n'
          f'-----------------------------------------------\n')

    for i, element in enumerate(class_data):

#Class information
        id = element['id']
        durationInMinutes = str(element['durationInMinutes'])
        instructor = element['instructor']
        clubName = element['clubName']
        name = element['name']
        zonedStartTime = strToTime(class_data)[i]

#Bookinginfo
        capacity = str(element['bookingInfo']['capacity'])
        bookedCount = str(element['bookingInfo']['bookedCount'])
        if capacity == bookedCount:
            waitingList = str(element['bookingInfo']['waitingListCount'])
        else:
            waitingList = '--'

#MemberBookingInfo
        bookingState = element['bookingInfo']['memberBookingInfo']['bookingState']
        
        if bookingState == "Booked":
            waitingListPosition = str(element['bookingInfo']['memberBookingInfo']['waitingListPosition'])
        else:
            waitingListPosition = '--'

        print(f'\033[1;97;40mClass: {name.rjust(40)}\033[0m\n'
              f'Instructor: {instructor.rjust(35)}\n'
              f'Id: {id.rjust(43)}\n'
              f'Start time: {zonedStartTime.rjust(35)}\n'
              f'Duration: {durationInMinutes.rjust(37)}\n'
              f'Club: {clubName.rjust(41)}\n\n'
              f'\033[1;37mBooking Information:\033[0m\n'
              f'Booked: {bookedCount.rjust(36)}/{capacity}')
        if waitingList != '--':
            print(f'Waiting list: {waitingList.rjust(33)}')
        if 'participationProbability' in element:
            print(f'Participation Probability: {element['participationProbability'].rjust(20)}')
        print(f'Booking state: {bookingState.rjust(32)}')
        if waitingListPosition != '--' and waitingListPosition != '0':
            print(f'Waiting list position: {waitingListPosition.rjust(23)}')
        print(f'\n-----------------------------------------------\n')

#Independent member information 
    followingBookingCount = element['followingBookingCount']
    followingBookings = element['followingBookings']
    
    print(f'\033[1;37mMember booking information for {participationId}:\033[0m\n'
        f'FollowingBookingCount: {followingBookingCount}\n'
        f'FollowingBookings: {followingBookings}\n\n')

if __name__ == '__main__':
    OrganizedBooking()