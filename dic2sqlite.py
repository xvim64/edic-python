# coding=utf-8-sig

import os
import sqlite3
import re
import sys
import gzip
import glob

pat11 = re.compile(r'^([a-z]+)[1-3]$')

adv = r'conj|xint|ints|pron|xprep|prep|adv|suf|int|pl|vi|vt|pt|ad|an|as|A|J|N|X|a|n|x|v|z|ㅁㅇ|ㅁ|ㅌ|ㅜ'
pat21 = re.compile(r'('        + adv + r')\s*[,.)]\s+')
pat22 = re.compile(r'^([,.:;]+|' + adv + r')\s+')
pat23 = re.compile(r'^([,.:;]+|' + adv + r')\s*=+')
pat24 = re.compile(r'\d\)')
pat25 = re.compile(r'\s{2,}')

pat31 = re.compile(r'\W')

def create():
    with sqlite3.connect('edic.sqlite') as conn:
        cur = conn.cursor()
        cur.execute("""create table {} (
                        __id integer not null primary key autoincrement unique,
                        __nick text not null,
                        __name text not null,
                        __meaning text not null);""".format('en'))

def insert():
    txts = glob.glob('utf-8' + os.sep + '*.txt')
    dics = glob.glob('utf-8' + os.sep + '*.dic')
    gzs  = glob.glob('utf-8' + os.sep + '*.gz')

    errors = []
    warnings = []

    if len(txts):
        pass
    elif len(dics):
        txts = dics
    elif len(gzs):
        for gz in gzs:
            with gzip.open(gz, 'rb') as f_in:
                with open(gz.replace('.gz',''), 'wb') as f_out:
                    f_out.write(f_in.read())
        txts = glob.glob('utf-8' + os.sep + '*.dic')
    else:
        print('ERROR: no "utf-8' + os.sep + '*.dic/gz/txt files')
        sys.exit(1)

    create()

    with sqlite3.connect('edic.sqlite') as conn:
        cur = conn.cursor()
        for txt in txts:
            with open(txt, 'rt', encoding='utf-8') as f:
                x = f.read().splitlines()
                for i in x:
                    if not (1 + i.find(':')):
                        if 1 + i.find('['):
                            warnings.append(i)
                            i = i.replace('[',':')

                    if 1 + i.find(':'):
                        x1, x2 = i.split(':',1)
                        
                        x1 = x1.strip()
                        x2 = x2.strip()
                        x2t = x2

                        x2 = x2.replace('"', '""')
                        x2 = pat21.sub('',x2)
                        x2 = pat22.sub('', x2)
                        x2 = pat23.sub('=', x2)
                        x2 = pat24.sub('', x2)
                        x2 = pat25.sub(' ', x2)
                        x2 = x2.strip()
                        if not x2:
                            x2 = x2t
                        
                        x1 = x1.replace('"', '""')
                        x1 = x1.strip()
                        x1 = pat11.sub('\g<1>', x1)

                        x3 = pat31.sub('', x1)
                        if not x3:
                            x3 = x1
                            print(x1, x2)
                        x3 = x3.lower()

                        cur.execute('insert into {} (__nick, __name, __meaning) values ("{}", "{}", "{}")'.format('en', x3, x1, x2))
                    else:
                        errors.append(i)
        conn.commit()
    if errors or warnings:
        with open('log-build-sql.txt','wt',encoding='utf-8') as f:
            logs = '\n'.join(['-'*80,'WARNING ( [ --> : )','-'*80] + warnings + ['','-'*80,'ERROR','-'*80] + errors)
            f.write(logs)
            print(logs)

if __name__ == '__main__':
    insert()



