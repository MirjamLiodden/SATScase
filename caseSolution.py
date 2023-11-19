"""
File: caseSolution.py
Author: Mirjam Liodden
Date: 18.11.2023

"""

import json

def OrganizedBooking():


    with open('response.json', 'r') as f:                     
        data = json.loads(f.read())
        f.close()

    class_data = data['results']

    for i, element in enumerate(class_data):

#Class information
        id = element['id']
        durationInMinutes = element['durationInMinutes']
        instructor = element['instructor']
        clubName = element['clubName']
        name = element['name']

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

        print(f'Class: {name}\n'
              f'Instructor: {instructor}\n'
              f'Id: {id}\n'
              f'Duration: {durationInMinutes}\n'
              f'Club: {clubName}\n\n'
              f'Booking Information:\n'
              f'Booked: {bookedCount}/{capacity}')
        if waitingList != '--':
            print(f'Waiting list: {waitingList}')
        if 'participationProbability' in element:
            print(f'Participation Probability: {element['participationProbability']}')
        print(f'Booking state: {bookingState}')
        if waitingListPosition != '--' and waitingListPosition != '0':
            print(f'Waiting list position: {waitingListPosition}')
        print(f'\n------------------------------------------------\n')

#Independent member information 
    followingBookingCount = element['followingBookingCount']
    followingBookings = element['followingBookings']
    
    print(f'Member booking information:\n'
        f'FollowingBookingCount: {followingBookingCount}\n'
        f'FollowingBookings: {followingBookings}')

if __name__ == '__main__':
    OrganizedBooking()