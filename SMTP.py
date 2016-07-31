#!/usr/bin/env python

# -*- coding: utf-8 -*-

import smtplib

from email.MIMEMultipart import MIMEMultipart

from email.MIMEText import MIMEText

def checkConnection(server, port, tls, user, passwd):

    try:

        connect = smtplib.SMTP(server, port)

        connect.ehlo()

        if tls:

          connect.starttls()

          connect.ehlo()

        connect.login(user, passwd)
        
        return connect

    except:

        return False

def inboxEmail(server, port, tls, user, passwd, maillist, From, subject, mailtext):

    smtpConnect = checkConnection(server, port, tls, user, passwd)

    emails = len(maillist)

    for success, sendto in enumerate(maillist):

        content = MIMEMultipart()

        content['From'] = From

        content['To'] = sendto.rstrip()

        content['Subject'] = subject

        htmlscript = mailtext.rstrip()

        content.attach(MIMEText(htmlscript, 'html'))

        print('Pr0 SMTP Email Sender >>> You are going to send to '+sendto.rstrip())

        smtpConnect.sendmail(From, sendto.rstrip(), content.as_string())

    smtpConnect.quit()

    print('\nBastians Email Sender >>> Email to '+str(success+1)+'/'+str(emails)+' Adresses sended!\n')

print"""

______     _____   _____           ______ _____      

| ___ \   |  _  | /  ___|          |  _  \____ |     

| |_/ / __| |/' | \ `--.  ___ _ __ | | | |   / /_ __ 

|  __/ '__|  /| |  `--. \/ _ \ '_ \| | | |   \ \ '__|

| |  | |  \ |_/ / /\__/ /  __/ | | | |/ /.___/ / |   

\_|  |_|   \___/  \____/ \___|_| |_|___/ \____/|_|      

                                  Version v1.0 By WhoAmi 

                                         CLAY TeaM                    

                                                          """

print('# GreeTz To : All My Friends & CLAY Members & FsocietyTN Members')

print('')

smtpServer = raw_input('\nPlease enter the SMTP Server (Hostname or IP Adress): ')

smtpPort = input('Please enter the SMTP Port : ')

smtpTLS = input('Secure the Email with TLS ? (Yes [1] or No [0]): ')

smtpUser = raw_input('Enter the SMTP Username: ')

smtpPass = raw_input('Enter the SMTP Password: ')

if checkConnection(smtpServer, smtpPort, smtpTLS, smtpUser, smtpPass,):

    print('\nPr0 SMTP Email Sender >>> SMTP Status // Connected!')

    sendFrom = raw_input('\nEnter the Receiver: ')

    sendSubj = raw_input('Enter the Subject: ')

    userlist = raw_input('Enter the Path of the Email List: ')

    try:

        maillist = open(userlist).readlines()

        print('\n Pr0 SMTP Email Sender >>> I found currently '+str(len(maillist))+' Email Adresses.')

        htmlscript = raw_input('\nEnter here the Path to your HTML Script: ')

        try:

            html = open(htmlscript).read()

            raw_input('ENTER, to send the HTML Script to '+str(len(maillist))+' ...\n')

            try:

                inboxEmail(smtpServer, smtpPort, smtpTLS, smtpUser, smtpPass, maillist, sendFrom, sendSubj, html)

            except:

                print('ERROR: I CANT USE THE EMAIL!')

        except:

            print('The HTML File cannot get readed yet or is empty.')

    except:

        print('The .txt File cannot get readed or is empty.')

else:

    print('I cant connect to the Server :/')
