#!/bin/bash

# after the first comment 

# as soon as something crashes the script stops
set -e

echo Running commands

# create users
./social_network.py createuser 'user1@example.com' --phone_number '123-456-7890' --birthday '1990-01-15'
./social_network.py createuser 'user2@example.com' --phone_number '987-654-3210' --birthday '1985-05-22'
./social_network.py createuser 'user3@example.com' --phone_number '555-123-4567' --birthday '1992-11-08'
./social_network.py createuser 'user4@example.com' --phone_number '333-999-8888' --birthday '1988-03-30'
./social_network.py createuser 'user5@example.com' --phone_number '777-888-9999' --birthday '1995-09-18'
./social_network.py createuser 'user6@example.com' --phone_number '111-222-3333' --birthday '1983-07-02'
./social_network.py createuser 'user7@example.com' --phone_number '444-555-6666' --birthday '1998-12-25'
./social_network.py createuser 'user8@example.com' --phone_number '666-333-2222' --birthday '1987-04-14'
./social_network.py createuser 'user9@example.com' --phone_number '999-777-5555' --birthday '1991-06-10'
./social_network.py createuser 'user10@example.com' --phone_number '222-444-8888' --birthday '1989-08-20'
./social_network.py createuser 'user11@example.com' --phone_number '888-111-7777' --birthday '1996-02-03'
./social_network.py createuser 'user12@example.com' --phone_number '444-888-5555' --birthday '1986-10-12'
./social_network.py createuser 'user13@example.com' --phone_number '555-999-7777' --birthday '1993-04-07'
./social_network.py createuser 'user14@example.com' --phone_number '777-666-3333' --birthday '1997-11-29'
./social_network.py createuser 'user15@example.com' --phone_number '333-222-9999' --birthday '1984-01-17'
./social_network.py createuser 'user16@example.com' --birthday '1994-06-22'
./social_network.py createuser 'user17@example.com' --birthday '1982-09-05'
./social_network.py createuser 'user18@example.com' --birthday '1999-03-12'
./social_network.py createuser 'user19@example.com' --birthday '1981-12-01'
./social_network.py createuser 'user20@example.com' --birthday '1997-08-14'
./social_network.py createuser 'user21@example.com'
./social_network.py createuser 'user22@example.com'
./social_network.py createuser 'user23@example.com'
./social_network.py createuser 'user24@example.com'
./social_network.py createuser 'user25@example.com'
./social_network.py createuser 'user26@example.com'
./social_network.py createuser 'user27@example.com'
./social_network.py createuser 'user28@example.com'
./social_network.py createuser 'user29@example.com'
./social_network.py createuser 'user30@example.com'

# create accounts
./social_network.py createaccount 'user1@example.com' 'user1' --privacy 'private'
./social_network.py createaccount 'user2@example.com' 'user2'
./social_network.py createaccount 'user3@example.com' 'user3' --privacy 'private'
./social_network.py createaccount 'user4@example.com' 'user4'
./social_network.py createaccount 'user5@example.com' 'user5'
./social_network.py createaccount 'user6@example.com' 'user6' --privacy 'private'
./social_network.py createaccount 'user7@example.com' 'user7'
./social_network.py createaccount 'user8@example.com' 'user8'
./social_network.py createaccount 'user9@example.com' 'user9' --privacy 'private'
./social_network.py createaccount 'user10@example.com' 'user10'
./social_network.py createaccount 'user11@example.com' 'user11'
./social_network.py createaccount 'user12@example.com' 'user12' --privacy 'private'
./social_network.py createaccount 'user13@example.com' 'user13'
./social_network.py createaccount 'user14@example.com' 'user14'
./social_network.py createaccount 'user15@example.com' 'user15'
./social_network.py createaccount 'user16@example.com' 'user16'
./social_network.py createaccount 'user17@example.com' 'user17' --privacy 'private'
./social_network.py createaccount 'user18@example.com' 'user18'
./social_network.py createaccount 'user19@example.com' 'user19'
./social_network.py createaccount 'user20@example.com' 'user20' --privacy 'private'
./social_network.py createaccount 'user21@example.com' 'user21'
./social_network.py createaccount 'user22@example.com' 'user22'
./social_network.py createaccount 'user23@example.com' 'user23'
./social_network.py createaccount 'user24@example.com' 'user24'
./social_network.py createaccount 'user25@example.com' 'user25' --privacy 'private'
./social_network.py createaccount 'user26@example.com' 'user26'
./social_network.py createaccount 'user27@example.com' 'user27'
./social_network.py createaccount 'user28@example.com' 'user28' --privacy 'private'
./social_network.py createaccount 'user29@example.com' 'user29'
./social_network.py createaccount 'user30@example.com' 'user30'

# follow
./social_network.py follow 'user1' 'user2'
./social_network.py follow 'user1' 'user3'
./social_network.py follow 'user1' 'user4'
./social_network.py follow 'user1' 'user5'

./social_network.py follow 'user2' 'user1'
./social_network.py follow 'user2' 'user3'
./social_network.py follow 'user2' 'user6'
./social_network.py follow 'user2' 'user7'

./social_network.py follow 'user3' 'user1'
./social_network.py follow 'user3' 'user2'
./social_network.py follow 'user3' 'user8'
./social_network.py follow 'user3' 'user9'

./social_network.py follow 'user4' 'user1'
./social_network.py follow 'user4' 'user10'
./social_network.py follow 'user4' 'user11'
./social_network.py follow 'user4' 'user12'

./social_network.py follow 'user5' 'user1'
./social_network.py follow 'user5' 'user13'
./social_network.py follow 'user5' 'user14'
./social_network.py follow 'user5' 'user15'

./social_network.py follow 'user6' 'user2'
./social_network.py follow 'user6' 'user16'
./social_network.py follow 'user6' 'user17'
./social_network.py follow 'user6' 'user18'

./social_network.py follow 'user7' 'user2'
./social_network.py follow 'user7' 'user19'
./social_network.py follow 'user7' 'user20'
./social_network.py follow 'user7' 'user21'

./social_network.py follow 'user8' 'user3'
./social_network.py follow 'user8' 'user22'
./social_network.py follow 'user8' 'user23'
./social_network.py follow 'user8' 'user24'

./social_network.py follow 'user9' 'user3'
./social_network.py follow 'user9' 'user25'
./social_network.py follow 'user9' 'user26'
./social_network.py follow 'user9' 'user27'

./social_network.py follow 'user10' 'user4'
./social_network.py follow 'user10' 'user28'
./social_network.py follow 'user10' 'user29'
./social_network.py follow 'user10' 'user30'

./social_network.py follow 'user11' 'user4'
./social_network.py follow 'user11' 'user30'
./social_network.py follow 'user11' 'user28'
./social_network.py follow 'user11' 'user9'

./social_network.py follow 'user12' 'user4'
./social_network.py follow 'user12' 'user27'
./social_network.py follow 'user12' 'user26'
./social_network.py follow 'user12' 'user25'

./social_network.py follow 'user13' 'user5'
./social_network.py follow 'user13' 'user24'
./social_network.py follow 'user13' 'user23'
./social_network.py follow 'user13' 'user22'

./social_network.py follow 'user14' 'user5'
./social_network.py follow 'user14' 'user21'
./social_network.py follow 'user14' 'user20'
./social_network.py follow 'user14' 'user19'

./social_network.py follow 'user15' 'user5'
./social_network.py follow 'user15' 'user18'
./social_network.py follow 'user15' 'user17'
./social_network.py follow 'user15' 'user16'

./social_network.py follow 'user16' 'user6'
./social_network.py follow 'user16' 'user5'
./social_network.py follow 'user16' 'user4'
./social_network.py follow 'user16' 'user3'

./social_network.py follow 'user17' 'user6'
./social_network.py follow 'user17' 'user5'
./social_network.py follow 'user17' 'user4'
./social_network.py follow 'user17' 'user3'

./social_network.py follow 'user18' 'user6'
./social_network.py follow 'user18' 'user5'
./social_network.py follow 'user18' 'user4'
./social_network.py follow 'user18' 'user3'

./social_network.py follow 'user19' 'user7'
./social_network.py follow 'user19' 'user6'
./social_network.py follow 'user19' 'user5'
./social_network.py follow 'user19' 'user4'

./social_network.py follow 'user20' 'user7'
./social_network.py follow 'user20' 'user6'
./social_network.py follow 'user20' 'user5'
./social_network.py follow 'user20' 'user4'

./social_network.py follow 'user21' 'user7'
./social_network.py follow 'user21' 'user6'
./social_network.py follow 'user21' 'user5'
./social_network.py follow 'user21' 'user4'

./social_network.py follow 'user22' 'user8'
./social_network.py follow 'user22' 'user7'
./social_network.py follow 'user22' 'user6'
./social_network.py follow 'user22' 'user5'

./social_network.py follow 'user23' 'user8'
./social_network.py follow 'user23' 'user7'
./social_network.py follow 'user23' 'user6'
./social_network.py follow 'user23' 'user5'

./social_network.py follow 'user24' 'user8'
./social_network.py follow 'user24' 'user7'
./social_network.py follow 'user24' 'user6'
./social_network.py follow 'user24' 'user5'

./social_network.py follow 'user25' 'user9'
./social_network.py follow 'user25' 'user8'
./social_network.py follow 'user25' 'user7'
./social_network.py follow 'user25' 'user6'

./social_network.py follow 'user26' 'user9'
./social_network.py follow 'user26' 'user8'
./social_network.py follow 'user26' 'user7'
./social_network.py follow 'user26' 'user6'

./social_network.py follow 'user27' 'user9'
./social_network.py follow 'user27' 'user8'
./social_network.py follow 'user27' 'user7'
./social_network.py follow 'user27' 'user6'

./social_network.py follow 'user28' 'user10'
./social_network.py follow 'user28' 'user9'
./social_network.py follow 'user28' 'user8'
./social_network.py follow 'user28' 'user7'

./social_network.py follow 'user29' 'user10'
./social_network.py follow 'user29' 'user9'
./social_network.py follow 'user29' 'user8'
./social_network.py follow 'user29' 'user7'

./social_network.py follow 'user30' 'user10'
./social_network.py follow 'user30' 'user9'
./social_network.py follow 'user30' 'user8'
./social_network.py follow 'user30' 'user7'

# post

./social_network.py post 'user1' 'Post 1 from user1'
./social_network.py post 'user1' 'Post 2 from user1'
./social_network.py post 'user1' 'Post 3 from user1'

./social_network.py post 'user2' 'Post 1 from user2'
./social_network.py post 'user2' 'Post 2 from user2'
./social_network.py post 'user2' 'Post 3 from user2'

./social_network.py post 'user3' 'Post 1 from user3'
./social_network.py post 'user3' 'Post 2 from user3'
./social_network.py post 'user3' 'Post 3 from user3'

./social_network.py post 'user4' 'Post 1 from user4'
./social_network.py post 'user4' 'Post 2 from user4'
./social_network.py post 'user4' 'Post 3 from user4'

./social_network.py post 'user5' 'Post 1 from user5'
./social_network.py post 'user5' 'Post 2 from user5'
./social_network.py post 'user5' 'Post 3 from user5'

./social_network.py post 'user6' 'Post 1 from user6'
./social_network.py post 'user6' 'Post 2 from user6'
./social_network.py post 'user6' 'Post 3 from user6'

./social_network.py post 'user7' 'Post 1 from user7'
./social_network.py post 'user7' 'Post 2 from user7'
./social_network.py post 'user7' 'Post 3 from user7'

./social_network.py post 'user8' 'Post 1 from user8'
./social_network.py post 'user8' 'Post 2 from user8'
./social_network.py post 'user8' 'Post 3 from user8'

./social_network.py post 'user9' 'Post 1 from user9'
./social_network.py post 'user9' 'Post 2 from user9'
./social_network.py post 'user9' 'Post 3 from user9'

./social_network.py post 'user10' 'Post 1 from user10'
./social_network.py post 'user10' 'Post 2 from user10'
./social_network.py post 'user10' 'Post 3 from user10'

./social_network.py post 'user11' 'Post 1 from user11'
./social_network.py post 'user11' 'Post 2 from user11'
./social_network.py post 'user11' 'Post 3 from user11'

./social_network.py post 'user12' 'Post 1 from user12'
./social_network.py post 'user12' 'Post 2 from user12'
./social_network.py post 'user12' 'Post 3 from user12'

./social_network.py post 'user13' 'Post 1 from user13'
./social_network.py post 'user13' 'Post 2 from user13'
./social_network.py post 'user13' 'Post 3 from user13'

./social_network.py post 'user14' 'Post 1 from user14'
./social_network.py post 'user14' 'Post 2 from user14'
./social_network.py post 'user14' 'Post 3 from user14'

./social_network.py post 'user15' 'Post 1 from user15'
./social_network.py post 'user15' 'Post 2 from user15'
./social_network.py post 'user15' 'Post 3 from user15'

./social_network.py post 'user16' 'Post 1 from user16'
./social_network.py post 'user16' 'Post 2 from user16'
./social_network.py post 'user16' 'Post 3 from user16'

./social_network.py post 'user17' 'Post 1 from user17'
./social_network.py post 'user17' 'Post 2 from user17'
./social_network.py post 'user17' 'Post 3 from user17'

./social_network.py post 'user18' 'Post 1 from user18'
./social_network.py post 'user18' 'Post 2 from user18'
./social_network.py post 'user18' 'Post 3 from user18'

./social_network.py post 'user19' 'Post 1 from user19'
./social_network.py post 'user19' 'Post 2 from user19'
./social_network.py post 'user19' 'Post 3 from user19'

./social_network.py post 'user20' 'Post 1 from user20'
./social_network.py post 'user20' 'Post 2 from user20'
./social_network.py post 'user20' 'Post 3 from user20'

./social_network.py post 'user21' 'Post 1 from user21'
./social_network.py post 'user21' 'Post 2 from user21'
./social_network.py post 'user21' 'Post 3 from user21'

./social_network.py post 'user22' 'Post 1 from user22'
./social_network.py post 'user22' 'Post 2 from user22'
./social_network.py post 'user22' 'Post 3 from user22'

./social_network.py post 'user23' 'Post 1 from user23'
./social_network.py post 'user23' 'Post 2 from user23'
./social_network.py post 'user23' 'Post 3 from user23'

./social_network.py post 'user24' 'Post 1 from user24'
./social_network.py post 'user24' 'Post 2 from user24'
./social_network.py post 'user24' 'Post 3 from user24'

./social_network.py post 'user25' 'Post 1 from user25'
./social_network.py post 'user25' 'Post 2 from user25'
./social_network.py post 'user25' 'Post 3 from user25'

./social_network.py post 'user26' 'Post 1 from user26'
./social_network.py post 'user26' 'Post 2 from user26'
./social_network.py post 'user26' 'Post 3 from user26'

./social_network.py post 'user27' 'Post 1 from user27'
./social_network.py post 'user27' 'Post 2 from user27'
./social_network.py post 'user27' 'Post 3 from user27'

./social_network.py post 'user28' 'Post 1 from user28'
./social_network.py post 'user28' 'Post 2 from user28'
./social_network.py post 'user28' 'Post 3 from user28'

./social_network.py post 'user29' 'Post 1 from user29'
./social_network.py post 'user29' 'Post 2 from user29'
./social_network.py post 'user29' 'Post 3 from user29'

./social_network.py post 'user30' 'Post 1 from user30'
./social_network.py post 'user30' 'Post 2 from user30'
./social_network.py post 'user30' 'Post 3 from user30'

# likes
./social_network.py like 'user1' 'user5' 13
./social_network.py like 'user1' 'user3' 7

./social_network.py like 'user2' 'user1' 1
./social_network.py like 'user2' 'user6' 16

./social_network.py like 'user3' 'user8' 22
./social_network.py like 'user3' 'user9' 25

./social_network.py like 'user4' 'user12' 34
./social_network.py like 'user4' 'user10' 28

./social_network.py like 'user5' 'user14' 40
./social_network.py like 'user5' 'user13' 45

./social_network.py like 'user6' 'user17' 49
./social_network.py like 'user6' 'user16' 48

./social_network.py like 'user7' 'user20' 60
./social_network.py like 'user7' 'user21' 61

./social_network.py like 'user8' 'user23' 67
./social_network.py like 'user8' 'user24' 70

./social_network.py like 'user9' 'user3' 7
./social_network.py like 'user9' 'user27' 81

./social_network.py like 'user10' 'user4' 10
./social_network.py like 'user10' 'user30' 90

# comments
./social_network.py comment 'user1' 'user5' 13 'Great post!'
./social_network.py comment 'user1' 'user3' 7 'Nice photo!'

./social_network.py comment 'user2' 'user1' 1 'Interesting thoughts.'
./social_network.py comment 'user2' 'user6' 16 'Love your content!'

./social_network.py comment 'user3' 'user8' 22 'Well said!'
./social_network.py comment 'user3' 'user9' 25 'Agree with you!'

./social_network.py comment 'user4' 'user12' 34 'Awesome video!'
./social_network.py comment 'user4' 'user10' 28 'Great insights.'

./social_network.py comment 'user5' 'user14' 40 'This is amazing!'
./social_network.py comment 'user5' 'user13' 45 'Totally agree!'

./social_network.py comment 'user6' 'user17' 49 'Keep it up!'
./social_network.py comment 'user6' 'user16' 48 'Impressive work.'

./social_network.py comment 'user7' 'user20' 60 'Inspirational!'
./social_network.py comment 'user7' 'user21' 61 'You nailed it!'

./social_network.py comment 'user8' 'user23' 67 'Fantastic post!'
./social_network.py comment 'user8' 'user24' 70 'Well written.'

./social_network.py comment 'user9' 'user3' 7 'Interesting perspective.'
./social_network.py comment 'user9' 'user27' 81 'Loving your content!'

./social_network.py comment 'user10' 'user4' 10 'Insightful thoughts.'
./social_network.py comment 'user10' 'user30' 90 'Your posts are always great!'

