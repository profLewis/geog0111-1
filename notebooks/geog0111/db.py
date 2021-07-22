#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
database for URL lookup and other things

This class loads / writes a yaml database file.
It can be quite slow, so dont call unless you need to
'''

__author__ = 'P. Lewis'
__email__ = 'p.lewis@ucl.ac.uk'
__date__ = '28 Aug 2021'
__copyright__ = 'Copyright 2020-2022 P. Lewis'
__license__ = 'GPLv3'

import yaml
from pathlib import Path
import os

class CacheDatabase():

    def __init__(self,*args,dbdir=None,data=None):
        """
        initialise database class.

        :argument args:      str: filename(s) for database
        :param dbdir:         str: cache directory. Get dbdir from dbdir,
                              default '.'
        :param data:          Dict : dataset to be loaded
        """
        #
        self.msgs = []
        self.dbdir = None
        self.write_file = None
        self.db_logic(dbdir)
        self.files = []
        self.data = data or {}
        # sort file names/locations
        for f in args:
            self.files.append(self.locate_file(f))
        self.files = np.array(self.files)

        # resolve directories for files
        not_exists = np.array([not f.exists() for f in self.files])
        for i,f in enumerate(self.files):
            if not_exists[i]:
                try:
                    f.parent.mkdir(parents=True, exist_ok=True)
                    not_exists[i] = False
                except FileNotFoundError as e:
                    # the user has requested a db directory that cant be made
                    self.msg(f"error creating directory {f.parent}: {e}")

        self.files = self.files[np.logical_not(not_exists)]

        # find the first writeable or non-existent file
        for i, f in enumerate(self.files):
            try:
                f.touch(exist_ok=True)
                if not self.write_file and self.writeable(f):
                    self.write_file = f
            except FileNotFoundError:
                pass

        # tidy up self.files for reading
        exists = np.array([f.exists() for f in self.files])
        self.files = self.files[exists]

        # check files are readable
        readable = np.array([self.readable(f) for f in self.files])
        self.files = self.files[readable]

    def locate_file(self,filename):
        """
        make absolute pathname of files. look for
        relative locations in self.dbdir or .

        :argument filename: str: filename for database
        :return:            str: absolute pathname of filename
        """
        filename = Path(filename).expanduser()
        if filename.is_absolute():
            return filename
        if self.dbdir:
            # relative: look in self.dbdir
            if Path(self.dbdir,filename).exists():
                return Path(self.dbdir,filename).resolve()
        if filename.exists():
            # it exists as defined, so use that
            return filename.absolute()
        # doesnt exist, so put in self.dbdir
        if (self.dbdir):
            return Path(self.dbdir,filename).resolve()
        # from .
        return filename.resolve()

    def db_logic(self,dbdir=None):
        """

        :param dbdir:   str: cache directory. default '.'
        :return:
        """
        # default cache location
        if 'CACHE_FILE' in os.environ:
            self.dbdir = os.environ['CACHE_FILE']
        # override with dbdir
        if dbdir != None:
            self.dbdir = dbdir
        if (dbdir == None) and (self.dbdir == None):
            self.dbdir = '.'
        # expand in case of ~
        self.dbdir = Path(self.dbdir).expanduser()
        return self.dbdir

    def write(self):
        """
        write the database in data to yaml file self.write_file
        if self.write_file is set. To set a self.write_file
        you must specify a db location/file that is writeable.

        :return:      True if saved, False if not
        """
        if self.write_file:
            with open(self.write_file , "w") as write_file:
                yaml.safe_dump(self.data, write_file)
                return True
        return False

    def msg(self,msg):
        """
        Print message
        :return: None
        """
        # dont repeat
        if msg not in self.msgs:
            print(f'CacheDatabase: {msg}')
            self.msgs.append(msg)

    def readable(self,f):
        """
        Return True if file is readable

        :param f: str filename
        :return:
        """
        # play around with lstat to get octal permission
        return bin(int(oct(Path(f).lstat().st_mode)[-3]))[-3:][0] == '1'

    def writeable(self, f):
        """
        Return True if file is readable

        :param f: str filename
        :return:
        """
        # play around with lstat to get octal permission
        return bin(int(oct(Path(f).lstat().st_mode)[-3]))[-3:][1] == '1'

    def read(self):
        """
        Read database from self.files

        :return: self
        """
        data = self.data
        for i,f in enumerate(self.files):
            with open(f.as_posix(), "r") as rfile:
                try:
                    this_data = yaml.safe_load(rfile)
                    data.update(this_data)
                except TypeError:
                    self.msg("read warning: failed to read %s as yaml"%f)
                    pass
        return self

def fclean(f):
    """
    delete file f and try to delete directory if empty

    :param f:
    :return: None
    """
    f = Path(f)
    if f.exists():
        f.unlink()
        try:
            f.parent.rmdir()
        except:
            pass

def test1(f = '/tmp/tmp/database.db',dbdir=None):
    '''
    Create a new database with filename given by f
    and make and override an entry. Test that works

    Write the database file to /tmp/tmp/database.db
    and check contents

    :param f: str filename
    :return: True if pass
    '''
    # delete if exists
    fclean(f)

    # create
    db = CacheDatabase(f, dbdir=dbdir)

    # update
    data = {'test': [1, 2, 3], 'test1': 'hello'}
    db.data.update(data)

    # write
    db.write()
    # test
    assert Path(db.write_file).read_text() == \
'''test:
- 1
- 2
- 3
test1: hello
'''
    #
    data = {'test': [4,5,6], 'test1': 'there','test2': 'again'}
    db.data.update(data)
    assert db.data == {'test': [4, 5, 6], 'test1': 'there', 'test2': 'again'},\
        'Failed test 2'

    fclean(f)
    del db
    return True

def test2(f = '/tmp/tmp/database.db',dbdir=None):
    '''
    Create a new database with filename given by f
    and make and override an entry. Test that works

    Write the database file to /tmp/tmp/database.db
    and check contents

    Start a new db and read the previously created db

    :param f: str filename
    :return: True if pass
    '''
    # delete if exists
    fclean(f)

    # create
    db = CacheDatabase(f, dbdir=dbdir)

    # update
    data = {'test': [1, 2, 3], 'test1': 'hello'}
    db.data.update(data)

    # write
    db.write()
    # test
    assert Path(db.write_file).read_text() == \
'''test:
- 1
- 2
- 3
test1: hello
'''
    db = CacheDatabase(f, dbdir=dbdir).read()
    assert db.data == {'test': [1, 2, 3], 'test1': 'hello'}

    fclean(f)
    del db
    return True

def test3():
    """
    load a set of filenames and check files and read_file
    are as expected.

    We create 3 files with different content. Only the first
    2 are readable, and only the 2nd is writable.

    :param f:
    :param dbdir:
    :return:
    """
    # first file is read only
    f1 = Path('tmp/tmp/first.db')
    f1.parent.mkdir(parents=True, exist_ok=True)
    f1.write_text(\
'''test:
- 1
- 2
- 3
test1: hello''')
    f1.chmod(0o444)

    # first file is read & write
    f2 = Path('tmp/tmp/second.db')
    f2.parent.mkdir(parents=True, exist_ok=True)
    f2.write_text(\
'''test:
- 4
- 5
- 6
test2: hello''')
    f2.chmod(0o644)

    # 3rd file is no read or write
    f3 = Path('tmp/tmp/third.db')
    f3.parent.mkdir(parents=True, exist_ok=True)
    f3.write_text(\
'''test:
- 7
- 8
- 9
test3: hello''')
    f3.chmod(0o000)

    db = CacheDatabase(f1,f2,f3).read()
    try:
        assert db.data == {'test': [4,5,6], 'test1': 'hello', 'test2': 'hello'}
    except AssertionError as e:
        db.msg(e)

    for f in [f1,f2,f3]:
        f.chmod(0o755)
        fclean(f)

    return True

def main():
    # absolute and relative pathname tests
    assert test1(f = '/tmp/tmp/database.db') == True
    assert test1(f='tmp/database.db') == True
    assert test1(f='tmp/database.db',dbdir='/tmp') == True

    # same as test 1 but save and load
    assert test2(f='/tmp/tmp/database.db') == True
    assert test2(f='tmp/database.db') == True
    assert test2(f='tmp/database.db', dbdir='/tmp') == True

    # multiple files
    assert test3() == True

if __name__ == "__main__":
    main()