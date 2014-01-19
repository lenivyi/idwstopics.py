#!/usr/bin/env python

# menghapus pesan peringatan atau error saat program dijalankan
import logging
logging.getLogger().setLevel(logging.ERROR)

from bs4 import BeautifulSoup
import urllib2
import time

idws = urllib2.urlopen("http://www.indowebster.com/")
soup = BeautifulSoup(idws.read())
tag = soup.find_all('dl')

# fungsi untuk parsing html bagian hot topics
def hot_topics():
    for dl_tag in tag:
        for span_tag in dl_tag.find_all("span", {"class" : "newThreadsBtn"}):
            if span_tag.string == "New Topics":
                print "\t===== " + span_tag.string + " from indowebster =====\n"
                for a_tag in dl_tag.find_all('a', {'class':'threadTitle tooltip-me'}):
                    print "[title] " +a_tag.string
                    print "[link]  " + a_tag.get('href') + "\n"

# fungsi untuk parsing html bagian new topics
def new_topics():
    for dl_tag in tag:
        for span_tag in dl_tag.find_all("span", {"class" : "newThreadsBtn"}):
            if span_tag.string == "Hot Topics":
                print "\t===== " + span_tag.string + " from indowebster =====\n"
                for a_tag in dl_tag.find_all('a', {'class':'threadTitle tooltip-me'}):
                    print "[title] " +a_tag.string
                    print "[link]  " + a_tag.get('href') + "\n"


if __name__ == '__main__':
    hot_topics()
    new_topics()
