#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time   : 2019/8/7 0007 23:03 
# @Autohor: Sam
# @File   : Phase I project.py



menu = {
    '汽车':{
        '轿车':{
            '奥迪':{
                'ao12A':{},
                'ao23B':{}
            },
            '宝马':{
                'bm45A':{},
                'bm25B':{}
            },
        },
        '公共汽车':{
            '大型公共汽车':{
                'GB6A':{},
                'GB97B':{}
            },
            '小型公共汽车':{
                'GB53A':{},
                'GB97B':{}
            }
        },
        '越野车':{
            '路虎':{
                'LH64A':{},
                'LH63B':{}
            },
            '吉普':{
                'JP23A':{},
                'JP59V':{}
            }
        }
    }
}


layers = [menu, ]
while True:
    if not layers:
        break

    current_layer = layers[-1]
    for key in current_layer:
        print(key)

    choice = input('>>: ').strip()

    if choice == 'b':
        layers.pop()
        continue

    if choice == 'q':
        break

    if choice not in current_layer:
        continue

    layers.append(current_layer[choice])