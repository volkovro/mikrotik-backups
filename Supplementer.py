#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import fileinput
import os

# We determine the serial number of the next router
openfile = open('Mikrotik_backuper.sh')
readfile = openfile.read()
pattern = 'router\\d+'
all_router = re.findall(pattern, readfile)
numbers = list(map(lambda x: x[6:], all_router))
tru_numbers = list(set(list(map(int, numbers))))
a = str(max(tru_numbers) + 1)
openfile.close()
# This is where the data is received
ipset = str(input('Enter Ip ->: '))
ippasswd = str(input('Enter password ->: '))
ipname = str(input('Enter router name ->: '))
# Next comes the template, which is passed to the main script
tamplate_stat = str('=$(netcat -w3 -z ' + '$IP' + a + ' $PRT && echo success || echo fail)')
tamplate_name = '  router' + a + '\n' + '# NEWNAME'
tamplate_variable = (
                            'IP' +
                            a +
                            '=' +
                            ipset
                    ) + \
                    '\r' + \
                    (
                            'PASS' +
                            a +
                            '=' +
                            ippasswd
                    ) + \
                    '\r' + \
                    (
                            'NAME' +
                            a +
                            '=' +
                            ipname
                    ) + \
                    '\r' + \
                    (
                            'status' +
                            a +
                            tamplate_stat
                    ) + \
                    '\r' + \
                    )
                            '#'
                    ) + \
                    '\r' +\
                    (
                            '#NEWVARIABLE'
                    )
tamplate_func = (
                        'function router' + a + ' {' + '\r'
                ) + \
                (
                        'echo "  ___________________________________________________' + ' \r'
                ) + \
                (
                        '  Start $IP' + a + ' ($NAME' + a + ')..."' + '\r'
                ) + \
                (
                        'if [ $status' + a + ' = $gg ]' + '\r'
                ) + \
                (
                        'then' + '\r'
                ) + \
                (
                        '  echo "' + '\r'
                ) + \
                (
                        '  Status $IP' + a + ' - OK, create backup:' + '\r'
                ) + \
                (
                        '  "' + '\r'
                ) + \
                (
                        '  sshpass -p $PASS' + a + ' ssh -T -p $PRT $LGIN@$IP' + a + ' << EOF' + '\r'
                ) + \
                (
                        'export file=$IP' + a + '$NAME' + a + '\r'
                ) + \
                (
                        'system backup save name=$IP' + a + '$NAME' + a + '\r'
                ) + \
                (
                        'quit' + '\r'
                ) + \
                (
                        'EOF' + '\r'
                ) + \
                (
                        'echo "' + '\r'
                ) + \
                (
                        "  Lockal save backup's..." + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'sshpass -p $PASS' + a + ' scp -P $PRT ' + '$LGIN@$IP' + a + '":/$IP' + a + '$NAME' + a + '.rsc" $DIR' + '\r'
                ) + \
                (
                        'sshpass -p $PASS' + a + ' scp -P $PRT $LGIN@$IP' + a + '":/$IP' + a + '$NAME' + a + '.backup"' + ' $DIR' + '\r'
                ) + \
                (
                        'echo "' + '\r'
                ) + \
                (
                        '  Cleaning router directory...' + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'sshpass -p $PASS' + a + ' ssh -T -p $PRT $LGIN@$IP' + a + ' << EOF' + '\r'
                ) + \
                (
                        'file remove "$IP' + a + '$NAME' + a + '.rsc"' + '\r'
                ) + \
                (
                        'file remove "$IP' + a + '$NAME' + a + '.backup"' + '\r'
                ) + \
                (
                        'quit' + '\r'
                ) + \
                (
                        'EOF' + '\r'
                ) + \
                (
                        'echo "' + '\r'
                ) + \
                (
                        '$IP' + a + ' END' + '\r'
                ) + \
                (
                        '  ___________________________________________________' + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'else' + '\r'
                ) + \
                (
                        '  echo "' + '\r'
                ) + \
                (
                        '  ...................................................' + '\r'
                ) + \
                (
                        '  ERROR $IP' + a + ' ($NAME' + a + '),' + '\r'
                ) + \
                (
                        "  backup can't create and save" + '\r'
                ) + \
                (
                        '  ...................................................' + '\r'
                ) + \
                (
                        '  ___________________________________________________' + '\r'
                ) + \
                (
                        '"' + '\r'
                ) + \
                (
                        'fi' + '\r'
                ) + \
                (
                        '}' + '\r'
                ) + \
                (
                    '#' + '\r'
                ) + \
                (
                    '#NEWFUNK'
                )
# The code below actually changes the main script ('.backup' is added to the original file)
with fileinput.FileInput('Mikrotik_backuper.sh', inplace=True, backup='.backup') as file:
    for line in file:
        line = line.rstrip()
        print(tamplate_variable if line == '#NEWVARIABLE' else line)
with fileinput.FileInput('Mikrotik_backuper.sh', inplace=True, backup='.backup2') as file:
    for line in file:
        line = line.rstrip()
        print(tamplate_func if line == '#NEWFUNK' else line)
os.unlink('Mikrotik_backuper.sh' + '.backup2')
with fileinput.FileInput('Mikrotik_backuper.sh', inplace=True, backup='.backup3') as file:
    for line in file:
        line = line.rstrip()
        print(tamplate_name if line == '# NEWNAME' else line)
os.unlink('Mikrotik_backuper.sh' + '.backup3')
