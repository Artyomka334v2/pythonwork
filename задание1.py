## -*- coding: utf-8 -*-
duration = int(input())
if duration < 60:
    s = duration
    print(s, "сек")
elif (duration >= 60) and (duration < 60**2):
    m = duration // 60
    s = duration % 60
    print(m, "мин", s, "сек")
elif (duration >= 60**2) and (duration < 24*(60**2)):
    h = duration // 60**2
    m = duration % 60**2 // 60
    s = duration % 60
    print(h, "час", m, "мин", s, "сек")
elif (duration >= 24*(60**2)):
    d = duration // 60**2 // 24
    h = duration // 60**2 % 24
    m = duration % 60**2 // 60
    s = duration % 60    
    print(d, "дн", h, "час", m, "мин", s, "сек")