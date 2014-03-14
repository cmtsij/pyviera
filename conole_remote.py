#!/usr/bin/env python
from pyviera import VieraFinder
import time
import curses


key_nrc_map={
    'P':('NRC_POWER-ONOFF','power off'),
    'i':('NRC_CHG_INPUT-ONOFF','input source'),
    'd':('NRC_DISP_MODE-ONOFF','display mode'),
    'h':('NRC_HOLD-ONOFF','hold'),
    'I':('NRC_INFO-ONOFF','info'),
    'r':('NRC_RETURN-ONOFF','return'),
    'S':('NRC_STTL-ONOFF','sub titile'),
    't':('NRC_TV-ONOFF','tv'),
    'KEY_BACKSPACE':('NRC_CANCEL-ONOFF','cancel'),

    'l':('NRC_R_TUNE-ONOFF','last view'),
    ']':('NRC_CH_UP-ONOFF','channel up'),
    '[':('NRC_CH_DOWN-ONOFF','channel down'),

    '}':('NRC_VOLUP-ONOFF','volume up'),
    '{':('NRC_VOLDOWN-ONOFF','volume down'),
    'M':('NRC_MUTE-ONOFF','mute'),

    '0':('NRC_D0-ONOFF',"0"),
    '1':('NRC_D1-ONOFF','1'),
    '2':('NRC_D2-ONOFF','2'),
    '3':('NRC_D3-ONOFF','3'),
    '4':('NRC_D4-ONOFF','4'),
    '5':('NRC_D5-ONOFF','5'),
    '6':('NRC_D6-ONOFF','6'),
    '7':('NRC_D7-ONOFF','7'),
    '8':('NRC_D8-ONOFF','8'),
    '9':('NRC_D9-ONOFF','9'),

    'm':('NRC_MENU-ONOFF','menu'),
    's':('NRC_SUBMENU-ONOFF','sub menu'),
    'KEY_UP':('NRC_UP-ONOFF','up'), #shift + up
    'KEY_DOWN':('NRC_DOWN-ONOFF','down'), #shift + down
    'KEY_LEFT':('NRC_LEFT-ONOFF','left'), #shift + left
    'KEY_RIGHT':('NRC_RIGHT-ONOFF','right'), #shift + right
    '^J':('NRC_ENTER-ONOFF','enter'), #enter
}




def key_event(stdscr):
    curses.curs_set(1)
    stdscr.scrollok(True)
    while True:
        c = stdscr.getch()
        key_name=curses.keyname(c)
        if key_name in key_nrc_map:
            stdscr.addstr(key_nrc_map[key_name][1]+'\n')
            tv.nrc(key_nrc_map[key_name][0])
        elif key_name == 'H':
            for key,(nrc,description) in sorted(key_nrc_map.iteritems()):
                stdscr.addstr(key+'::::'+description+'\n')
                
        else:
            stdscr.addstr(key_name+'\n')

        ## prevent to fast
        time.sleep(0.05)
        ## clean input buffer
        curses.flushinp()

'''
    while True:
        cmd=raw_input()
        tv.nrc(cmd)
'''

if __name__ == '__main__':
    vf = VieraFinder()
    tv = vf.get_viera()
    
    
    
    curses.wrapper(key_event)
