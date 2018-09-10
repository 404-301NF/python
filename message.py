#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  database.py
#
#  Copyright 2018 赵东博 <赵东博@DESKTOP-HJ7TRLT>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import sys, shelve


def store_person(db):
    '''
    让用户输入数据并将其存储到shelf对象中
    '''

    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone: ')
    db[pid] = person


def lookup_person(db):
    '''
    让用户输入ID和所需的字段，并从shelf对象中获取相应的数据
    '''
    pid = input('Enter ID number: ')
    field = input('what would you like to know? (name,age,phone) ')
    field = field.strip().lower()

    print(field.capitalize() + ':', db[pid][field])


def print_help():
    print('The available commands are: ')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quiet : Save changes and exit')
    print('? : Prints this message')


def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('G:\\database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()
