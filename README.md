# find_who_opened_your_pc
The script focuses on capturing the pic of the person who opened your laptop and mails you back the picture of the person.

You need to generate app password go to https://myaccount.google.com/apppasswords (select app as mail and device as your preferred machine) copy the 16 digit code provided and paste in app_password in py script

replace email_sender and email_receiver by your mail id


edit the bat file with the location of .py script


create a new text doc with content as: 

Set WshShell = CreateObject("WScript.Shell") 

WshShell.Run chr(34) & "C:\Users\user\Favorites\laptop_start\laptop_start.bat" & Chr(34), 0

Set WshShell = Nothing       


properly edit the location of .bat file and save this doc file as run_bat.vbs

place this .vbs file in startup folder of machine 

NOTE: the time delay is 10 mins i.e 600 seconds assuming logged in user takes atmost 10 mins to connect to internet.
