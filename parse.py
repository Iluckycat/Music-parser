from selenium import webdriver
import time
import os
try:
    browser = webdriver.Chrome()
    link = 'https://www.energyfm.ru'
    browser.get(link)
    file = open('parse.txt', 'w')
    Name_singer_old = ''
    Name_song_old = ''
    time.sleep(5)
    btn = browser.find_element_by_xpath('//*[@id="notMoscow"]')
    btn.click()
    btn1 = browser.find_element_by_xpath('//*[@id="mplayer_wraper_efir_player"]/div[1]/a')
    btn1.click()
    Name_singer = browser.find_element_by_xpath('//*[@id="on-air_now2"]/b').text
    Name_song = browser.find_element_by_xpath('//*[@id="on-air_now2"]/span[3]').text
    attr = btn1.get_attribute('class')
    p = len('toggleplayer noajax left ')
    attr2 = attr[p:p+5:1]
    fl = attr2.find('play')
    while fl == -1:
        Name_singer = ''
        Name_song = ''
        Name_singer = browser.find_element_by_xpath('//*[@id="on-air_now2"]/b').text
        Name_song = browser.find_element_by_xpath('//*[@id="on-air_now2"]/span[3]').text
        attr = btn1.get_attribute('class')
        attr2 = attr[p:p + 5:1]
        fl = attr2.find('play')
        str_ = ''
        str_ = Name_singer + ' - ' + Name_song + '\n'
        print("\033[31m", str_)
        if Name_singer != 'Energy FM' and Name_singer != 'Реклама' and (Name_song != Name_song_old or Name_singer != Name_singer_old):
            str_tmp = ''
            str_tmp = Name_singer + ' - ' + Name_song + '\n'
            print("\033[32m",str_tmp)
            file.write(str_tmp)
            Name_singer_old = ''
            Name_song_old = ''
            Name_singer_old = Name_singer
            Name_song_old = Name_song
        time.sleep(100)

finally:
    time.sleep(10)
    file.close()
    browser.quit()
