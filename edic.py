# coding=utf-8-sig

#--------------------------------------------------------------------------------

import os
import re
import sqlite3
import sys

#--------------------------------------------------------------------------------

dicDB = r'edic.sqlite'

#-----------------------------

bCls   = False
bColor = True

bWt    = False
bWin   = False
bExit  = False

nTmpCls = 10

#-----------------------------

if sys.platform == 'win32':
    bWin = True

if os.environ.get('WT_SESSION'):
    bWt = True

#-----------------------------

msgCls = 'clear'

if bWin:
    msgCls = 'cls'
    if not bWt:
        bColor = False

#-----------------------------

input_words = []

nEnd = len(sys.argv[1:])
n = 0

while n < nEnd:
    n += 1
    i = sys.argv[n]
    if i in ['--cls']:
        bCls = True
        continue
    if i in ['--no-cls']:
        bCls = False
        continue
    if i in ['--color']:
        bColor = True
        continue
    if i in ['--no-color']:
        bColor = False
        continue
    if i[:1] in ['-','/']:
        continue;
    i2 = i.strip()
    if i2:
        input_words.append(i2)

if input_words:
    bCls = False

#--------------------------------------------------------------------------------

def dic():
    global bCls, bColor, bExit

    # ------------------------------

    conn = sqlite3.connect(dicDB)
    cur  = conn.cursor()

    # ------------------------------

    pat_sql = re.compile(r'["\'`+\-_,.]')

    # ------------------------------

    sql_nm_name = 'select __name, __meaning from {} where __name like "{}"'
    sql_n_nick  = 'select __name            from {} where __nick like "{}"'
    sql_nm_nick = 'select __name, __meaning from {} where __nick like "{}"'

    # ------------------------------

    msgDic1c = '\x1b[33;92m{}\x1b[0m  \x1b[33;33m-->\x1b[0m  {}'
    msgDic1n = '{}  -->  {}'

    msgDic2c = '\x1b[33;92m{:12}\x1b[0m  \x1b[33;33m-->\x1b[0m  {}'
    msgDic2n = '{:12}  -->  {}'

    msgDic3c = '\x1b[33;92m{}\x1b[0m'
    msgDic3n = '{}'

    msgDic1 = msgDic1c if bColor else msgDic1n
    msgDic2 = msgDic2c if bColor else msgDic2n
    msgDic3 = msgDic3c if bColor else msgDic3n

    msgDic  = msgDic1

    # ------------------------------

    prompt1c = '\x1b[33;96m[E]$\x1b[0m '
    prompt1n = '[E]$ '

    prompt1 = prompt1c if bColor else prompt1n
    prompt2 = '\n' + prompt1

    prompt  = prompt1

    # ------------------------------

    bPrompt2 = False

    bVocaOnly = False

    # ------------------------------

    xns = []

    sql = ''

    # ------------------------------

    while True:
        if input_words:
            iWord = input_words.pop(0)
            if not input_words:
                bExit = True
        else:
            if bPrompt2:
                prompt = prompt2
            else:
                prompt = prompt1
            bPrompt2 = True

            print(prompt, end='', flush=True)

            while True:
                iWord = input('').strip()
                if iWord[:1]==':':
                    ws = iWord[1:]
                    if ws in ['c', 'cls', 'clear']:
                        os.system(msgCls)
                    elif ws in ['cls-yes', 'clear-yes']:
                        bCls = True
                    elif ws in ['cls-no', 'clear-no']:
                        bCls = False
                    elif ws in ['color-yes', 'clear-yes']:
                        bColor = True
                        msgDic1 = msgDic1c
                        msgDic2 = msgDic2c
                        prompt1 = prompt1c
                        prompt2 = '\n' + prompt1
                    elif ws in ['color-no', 'clear-no']:
                        bColor = False
                        msgDic1 = msgDic1n
                        msgDic2 = msgDic2n
                        prompt1 = prompt1n
                        prompt2 = '\n' + prompt1
                    elif ws in ['q', 'x', 'exit']:
                        sys.exit()
                elif iWord in ['cls']:
                    os.system(msgCls)
                elif len(iWord):
                    break
                print(prompt1, end='', flush=True)

        if not iWord:
            bPrompt2 = False
            xns = []
            continue

        iWord = pat_sql.sub('', iWord)

        if 1 + iWord.find('#'):
            iWord = iWord.replace('#','').replace('*','%').replace(' ','')
            sql = sql_nm_name
            msgDic = msgDic1
            bVocaOnly = False
        elif 1 + iWord.find('$'):
            iWord = iWord.replace('$','').replace('*','%').replace(' ','')
            sql = sql_n_nick
            msgDic = msgDic2
            bVocaOnly = True
        elif 1 + iWord.find('*'):
            iWord = iWord.replace('*','%').replace(' ','')
            sql = sql_nm_nick
            msgDic = msgDic2
            bVocaOnly = False
        else:
            iWord = iWord.replace(' ','')
            sql = sql_nm_nick
            msgDic = msgDic1
            bVocaOnly = False

        if not iWord:
            bPrompt2 = False
            continue

        # ------------------------------

        xns  = []
        cur.execute(sql.format('en', iWord))
        xns = cur.fetchall()

        # ------------------------------

        xns_len = len(xns)
        bTmpCls = True if xns_len > nTmpCls else False

        # ------------------------------

        if xns:
            buf = []
            if bCls or bTmpCls:
                os.system(msgCls)
                buf.append('-' * 60 + ' ({})'.format(xns_len) + '\n')
            if bVocaOnly:
                for xn in xns:
                    buf.append(msgDic3.format(xn[0]))
            else:
                for xn in xns:
                    buf.append(msgDic.format(xn[0], xn[1]))
            print('\n'.join(buf))

        if bExit:
            break;

        # ------------------------------

    conn.close()

#--------------------------------------------------------------------------------

if __name__ == '__main__':
    dic()

#--------------------------------------------------------------------------------
