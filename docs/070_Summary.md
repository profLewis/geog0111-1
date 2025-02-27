# 070 Summary

## Introduction

We have now reached the end of the course material, but hopefully not the end of your learning to code and to manipulate geospatial data. At the start of the course, we assumed you had never done any programming. Now, if you have been through the material and able to complete most of the exercises, formative assessments and coursework, you should be a competent (or better!) coder. We use this final section just to reiterate to you what you have learned. You will see that it a vast amount! We hope you will use this basis as a foundation to go further with your coding, to enable you to get the computer to do what you want, to test out your ideas, rather than being limited by what is currently available. If you need to learn a new some new languages such as javascript or matlab, you will find them very similar to Python. The same will apply to learning any other coding language: once you have a good grasp of the basics and what you can do in programming, you are in control. 

We know that there is often a steep learning curve for people new to coding, but we trust you have been able to deal with that and put the effective learning time in to make best use of the course. We also hope that the support from the course tutors and supporting doctoral students has been effective. We hope that you have found the experience enabling.

## Recap

As a brief recap on what you have learned:

### Course Basics

####  001 Using Notebooks

[001 Using Notebooks](001_Notebook_use.md): 
    Use of Jupyter notebooks; code and maskdown cells; use of markdown;  
    
#### 002 Unix

[002 Unix](002_Unix.md): Bash commands in notebooks; bash cells; Unix commands:


| cmd  |  meaning  | example use | 
|---|---|--|
| `~`  |  twiddle / tilde -  home | `cd ~/geog0111` |
| `.`  |  dot  - current directory | `cd .` |
| `..`  |  dot dot  - one level up directory | `cd ..` |
| `*`  | wildcard   | `ls R*` |
| `cd`  | change directory   | `cd ~/geog0111` |
| `pwd`  | print working directory | `pwd` |
| `ls`  | list | `ls README.md` |
| `ls -l`  | long list | `ls -l README.md` |
| `ls -lh`  | human-readable long list |`ls -lh README.md` |
| `chmod`  | change mode (permissions) | `chmod 644 README.md` |
| `rm` | remove | `rm work/n*` |
| `755` | `rwxr-xr-x` | `chmod 755 bin/*` |
| `644` | `rw-r--r--` | `chmod 644 README.md` |    

#### 003 Getting help

[003 Getting help](003_Help.md): How to get and read help document strings; the importance of documentation for methods; some examples of Python, mainly with the type `list`:


|  command | purpose  |   
|---|---|
| `help(m)`  |  print document string for method `m` |  
| `m?`  |  print short document string for method `m` |  
| `list`  |  Python data type for lists |  
| `list.append()`  | append item to list  |   
| `list.clear()`  | clear item from list  |  
| `list.sort`  | in-line list sort  |  
| `range(start,stop,step)`  | list-like generator for integers from `start` to (but not including) `stop` in steps of `step`  |      


#### 004 Accounts

[004 Accounts](004_Accounts.md): Storing / resetting and testing NASA Earthdata login.
    
|  command | purpose  |   
|---|---|
| `l = Cylog(sites); test = l.login()`  |  set / run login for list of URLs `sites` |  
| `cy = Cylog(sites,force=True); test = l.login()`  | reset / run login for list of URLs `sites` |
| `test_login(True)`  |  test the login by pulling a dataset from the NASA site|  


#### 005 Packages

[005 Packages](005_Packages.md); import packages using `import` and `from`.
    
|  command | purpose  |   
|---|---|
| `import yaml` | import the package `yaml`|
| `from pathlib import Path`  |  import the method/ class `Path` from the package `pathlib` |  



### Core Concepts


#### 010 Variables, comments and print
[010 Variables, comments and print()](010_Python_Introduction.md)


Rules and conventions for symbol names.

|  command | purpose  |   
|-|---|
| `#` | hash symbol, followed by comments|
| `print()` | print function|
| `\n` | newline character|
| `\t` | tab character|
| `varname = value` | set variable `varname` to `value`|
|`__doc__, __main__` | special method names |

Variables start with a lower case character and classes start with capitals

Reserved keywords:

                False      class      finally    is         return
                None       continue   for        lambda     try
                True       def        from       nonlocal   while
                and        del        global     not        with
                as         elif       if         or         yield
                assert     else       import     pass
                break      except     in         raise



#### 011 Data types

[011 Data types](011_Python_data_types.md) 


|core data types| example |
|---|-|
|`int`| `x = 10`|
|`float`| `x = 10.0`|
|`str`| `x = "hello world"`|
|`bool`| `x = False` |

    and how to convert ('cast') between then, where this is feasible:

| cast functions |
|---|
|`int()`|
|`float()`|
|`str()`|
|`bool()`|

    Other functions:

|  command | purpose  |   
|-|---|
| `type(v)` | data type of object `v`|
| `len(v)` | length of object `v` (e.g. `str`) |

    We have learned truth tables to list logical operations:


| A  | B  | A and B  | 
|:---:|:---:|:---:|
|  T |  T |  T | 
|  T |  F |  F | 
|  F |  T |  F | 
|  F |  F |  F | 



| A  | B  | A or B  | 
|:---:|:---:|:---:|
|  T |  T |  T | 
|  T |  F |  T | 
|  F |  T |  T | 
|  F |  F |  F | 

| A  | not A  | 
|:---:|:---:|
|  T | F | 
|   F |  T | 
    
#### 012 String formatting
    
[012 String formatting](012_Python_strings.md)

| item | description |
|---|-|
| `"'"` | single quote as a string |
| `'"'` | double quote as a string |
| `"\\"` | backslash as a string (escaped) in string|
| ''' ... ''' | multiple line string |
| `*` | string multiplication e.g. `"0"*2` -> `"00"` |
| `+` | string addition e.g. `"0" + "1"` -> `"01"`|
| `str.format()` | insert items in string e.g. `"{x}".format(x=1)` -> "1"|
| `f"..."`| f-string, e.g. `x=1`, `f"{x}"` -> `"1"|

#### 013 Python string methods

[013 String methods](013_Python_string_methods.md)


| item | description |
|---| -|
| `str.replace(a,b)` | replace occurrences of `a` with `b` in `str` |
| `str.strip(a)` | strip off any occurrences of `a` on left or right ends of `str` (also `lstrip`,`rstrip`)|
| `str.split(a)` | split `str` into list, using `a` as the separator, e.g. `"1:2".split(":")` -> `["1","2"]`
| `a.join(l)` | join the string items in list `l` into a string with `a` as the separator, e.g. `"x".join(["1","2"])` -> `"1x2"` |
| `str[start:stop:step]` | slice `str` and return characters `start` to (but not including) `stop` skipping `step` values, e.g. `"hello"[1:2]` -> `e`|



#### 104 Groups

[014 Python groups](014_Python_groups.md)

| symbol | description | example| access example |
| ---|---|---|---|
| `()` | `tuple`: low level group of items accessed by index. Cannot change once set| `(1,2,3)` | `(1,2)[1]` -> `[2]`|
| `[]`| `list`: group of items accessed by index with range of methods. Can change, sort etc. | `[1,2,3]`| `[1,2][1]` -> `[2]` |
| `{}` | `dict`: dictionary, a group of items accessed by key | `{"a" : 1}` | `{"a" : 1}["a"]` -> `1`|
| `[[],[]]` | hierarchical (multi-dimensional) list | 
| `[{},{}]` | list of dictionaries |
| `{"a":[],"b":[]}` | dictionary of lists|

List methods:

| method | description | example | result |
|---|---|---|---|
|`list.index(i)`|find index of value `i` in `list` |`[9,10,11].index(10)`| `1`|
| `list.extend(l)` | in-place extend `list` with list `l` | `x = [9,10,11]; x.extend([12,13])`| `x` -> `[9,10,11,12,13]`|
| `list.append(l)` | in-place append `list` with list `l` | `x = [9,10,11]; x.append([12,13])`| `x` -> `[9,10,11,[12,13]]`|
| `list.sort(l)` | in-place sort `list`  | `x = [10,9,11]; x.sort()`| `x` -> `[9,10,11]`|


Dictionary methods:

| method | description | example | result |
|---|---|---|---|
| `a.keys()` | keys in dictionary `a` | `d={"a":1,"b":2};d.keys()` | `['a', 'b']`|
| `a.values()` | values in dictionary `a` | `d={"a":1,"b":2};d.values()` | `[1, 2]`|
| `a.items()` | items `(key,value)` in dictionary `a` | `d={"a":1,"b":2};d.items()` | `[('a', 1), ('b', 2)])`|
| `dict(zip(a,b))` | form a dictionary from keys in list `a` and items in list `b` | `dict(zip(["a","b"],[1,2]))` | `{'a': 1, 'b': 2}`|
| `a.update(d)` | update dictionary `a` with dictionary `d`| `a={"a":1};d={"b":2};a.update(d)` | `a` -> `{'a': 1, 'b': 2}`|

#### 015 Python control

[015_Python_control](015_Python_control.md)

Comparison operators:

|symbol| meaning|
|:---:|:---:|
| == | is equivalent to |
| != | is not equivalent to |
| > | greater than |
|>= | greater than or equal to|
|<  | less than|
|<=  | less than or equal to    |


`If ... elif ... else`:


        if condition1:
            # do this 1
            doit1()
            ...
        elif condition2:
            # do this 2
            doit2()
            ...
        else:
            # do this 3
            doit3()
            ...


#### 016  `for ... in ...`

[016 for](016_Python_for.md)


| Command | Comment | Example | Result| 
|---|---|---|---|
|  `for item in list:` | loop, setting `item` to each value in `list` sequentially| see Example 1|
| `for key,value in list_of_tuples:`|loop, setting `a,b` to each value in list of tuples | See Example 2: `list({"a":7,"b":3}.items())` | `[('a', 7), ('b', 3)]`|
| `range(start,stop,step)` | index iterator from `start` to `stop` in steps of `step`| `list(range(1,6,2))`| `[1, 3, 5]` |
|`enumerate(list)`| provide index of `list` | `list(enumerate(['a','b','c']))` | `[(0, 'a'), (1, 'b'), (2, 'c')]`|
| `assert condition` | test that condition is `True`, exit otherwise | `assert True` ||
| `[f(x) for x in alist]` | list comprehension, applying `f(x)` to each item `x` in `alist` | `[i*i for i in range(3)]` | `[0, 1, 4]`
|`[af(x) for x in alist if ca(x)]` | list comprehension with conditional statement, applying `af(x)` to each element `x` in `alist` if `ca(x)` is `True`| `[i for i in range(11) if i%2]` | `[1, 3, 5, 7, 9]`
|`[af(x) if ca(x) else bf(x) for x in alist]` | list comprehension with conditional statement, applying `af(x)` to each element `x` in `alist` if `ca(x)` is `True`, otherwise applying `bf(x)` | `[i if i%2 else 0 for i in range(4)]` | `[0, 1, 0, 3]`


**Example 1:**

        for item in [1,2,3]:
            # print item in loop
            print(item)
    
Result:

        1
        2
        3


**Example 2:**

        for key,value in {"a":7,"b":3}.items():
            print(f'key is {key}, value is {value}')
            
Result:

        key is a, value is 7
        key is b, value is 3
        
#### 017 Functions

[017 Functions](017_Functions.md)

Anatomy of a function:

        def my_function(arg1,arg2,...,kw0=...,kw1=...):
          '''
          Document string 
          '''

          # comments

          retval =  ... 

          # return
          return retval


Also written as:

        def my_function(*args,**kwargs):
        
We have also seen `lambda` functions, used for short functions:

        function_name = lambda args : function_code


#### 018 Python codes

[018 Python codes](018_Running_Python.md)


|Command| Comment| Example| Result|
|---|---|---|---|
|`!unix_cmd` | Run unix command `unix_cmd` from Jupyter code cell | `!geog0111/helloWorld.py`| `hello world`|
|| | `!ls -l geog0111/helloWorld.py`| `-rwxr-xr-x 1 ucfalew ucfa 514 Oct  1 13:10 geog0111/helloWorld.py`|
|`%%bash` | Turn Jupyter Python code cell into `bash` cell | `%%bash` | | 
| | | `chmod 755 geog0111/helloWorld.py`
| | |`ls -l geog0111/helloWorld.py` | `-rwxr-xr-x 1 ucfalew ucfa 514 Oct  1 13:10 geog0111/helloWorld.py`|
| `%run script.py` | Run Python script `script.py` from Jupyter code cell| `%run geog0111/helloWorld.py` | `hello world`|
|     `cat << XX > YY; XX` | Put  marker `XX` in bash script and send text up to `XX` into file `YY` | `cat << EOF > work/file.py` |
|||    `hello world` | `cat work/file.py`
|||    `EOF` | `hello world`|


Form of a Python script:


            #!/usr/bin/env python
            # -*- coding: utf-8 -*- 

            '''
            helloWorld

            Purpose:

              function print the string 'hello world'

            '''

            __author__    = "P Lewis"
            __copyright__ = "Copyright 2020 P Lewis"
            __license__   = "GPLv3"
            __email__     = "p.lewis@ucl.ac.uk"

            def helloWorld():
                '''
                function to print the string 'hello world'

                '''
                print('hello world')


            # example calling the function
            def main():
                helloWorld()

            if __name__ == "__main__":
                # execute only if run as a script
                main()



### Data basics

#### 020 Files

* [020_Python_files](020_Python_files.md)


            from pathlib import Path

Common `Path` methods:



|command| unix-equivalent | purpose|
|---|---|---|
|`Path.cwd()`| `pwd` |Return path object representing the current working directory|
|`Path.home()`| `~`| Return path object representing the home directory|
|`Path.stat()`| `ls -l`* | return info about the path. File size is `Path.stat().st_size` |
|`Path.chmod()`| `chmod` | change file mode and permissions|
|`Path.glob(pattern)`| `ls *` | Glob the pattern given in the directory that is represented by the path, yielding matching files of any kind|
|`Path.mkdir()`| `mkdir` | to create a new directory at the given path|
|`Path.rename()`| `mv` | Rename a file or directory to the given target|
|`Path.rmdir()`| `rmdir` | Remove the empty directory|
|`Path.unlink()`| `rm` | Remove the file or symbolic link|

`*` Really, `Path.stat()` equates to the `unix` command `stat`, but this contains the information we access using `ls -l`.


            from geog0111.gurlpath import URL
            
Common `URL` methods:


|function| purpose|
|---|---|
|`URL.name`|  filename |
|`URL.parent`|  parent |
|`URL.parts`|  parts |
|`URL.stat()`| return info about the file. N.B. Only `URL.stat().st_size` is used for remote files|
|`URL.glob(pattern)`| Glob the pattern given in the URL directory, yielding matching files of any kind| 
|`URL.exists()`|  test to see if a url is accessible |
            

#### 021 Streams

* [021 Streams](021_Streams.md)


            from pathlib import Path

Common `Path` methods:


|command|  purpose|
|---|---|
|`Path.open()`| open a file and return a file descriptor|
|`Path.read_text()`|  read text|
|`Path.write_text()`| write text|
|`Path.read_bytes()`| read byte data|
|`Path.write_bytes()`| write byte data|

            from geog0111.gurlpath import URL

Common `URL` methods:

|command|  purpose|
|---|---|
|`URL.open()`| open a file descriptor with data from a URL|
|`URL.read_text()`|  read text from URL|
|`URL.write_text()`| write text to file|
|`URL.read_bytes()`| read byte data from URL|
|`URL.write_bytes()`| write byte data to file|

Notice that the `write` functions (and `open` when used for write) write to local files, not to the URL. 


Other methods and syntax:

| Command | Comment | 
| --:|---|
| `with Path(filename).open('r') as f:` | Open file `filename` for reading with file descriptor set to `f`|


`pandas`:

| Command | Comment | 
| --:|---|
|`pd.read_csv(f)`| Read CSV data from file or URL `f`|
|`pd.read_table(f)`| Read table data from file or URL `f`|
| `skiprows=N` | Keyword to skip `N` rows in reading for `pd.read_table`|
| `na_values=[-99.9]` | Keyword to set list of values to ignore (`-99.9` here) |
| `sep` | Keyword to define field separator |
| `engine='python'` or `engine='C'` | Keyword to set reading engine. `python` is more flexible, but `C` is faster. |
|`df.transpose()` | Transpose (rows->columns, columns->rows) pandas dataframe `df`|
|`df.head(N)` | first `N` lines of data (default 5) |
|`df.columns` | list-like object of column headings |
|`df[cname]` | Select column with name `cname`|
|`df[[c1,c2,c3]]` | Select columns with names `c1`, `c2` and `c3`|
| `pd.DataFrame(list,columns=cnames)` | Create `pandas` dataframe from information in list-like structures `list` with names from list `cnames`|
|`pd.to_datetime(str_list)` | convert list of date strings (e.g. of form `YYYY-MM-DD`) to `datetime` representation |
| `df[datetimes].dt.month` | month from `datetime` field fromn `datetime`-format column with name `datetimes`|
| `df[datetimes].dt.year` | year from `datetime` field fromn `datetime`-format column with name `datetimes`|
| `df[datetimes].dt.day` | day from `datetime` field fromn `datetime`-format column with name `datetimes`|
|`df.to_csv(filename,index=False)` |Write dataframe `df` to CSV format file, with no index column|

#### 022 Read and write files

* [022 Read write files](022_Read_write_files.md)

Modis library

            from  geog0111.modis import Modis
            modis = Modis(**kwargs)
            

            get_url(**kwargs) method of geog0111.modis.Modis instance
                Get URL object list for NASA MODIS products
                for the specified product, tile, year, month, day

                Keyword Arguments:

                verbose:  bool
                site    : str 
                product : str e.g. 'MCD15A3H'
                tile    : str e.g. 'h08v06'
                year    : str valid 2000-present
                month   : str 01-12
                day     : str 01-(28,29,30,31)

`gdal`

| Command | Comment |
|---|---|
|`g = gdal.Open(filename)` | Open geospatial file `filename` and return `gdal` object `g` (`None` if file not opened correctly)|
|`g.GetSubDatasets()` | Get list of sub-datasets from `gdal` object `g`| 
|`g.ReadAsArray()` | Read dataset from `gdal` object `g` into array |


#### 023  Plotting Graphs

* [023 Plotting](023_Plotting.md)

            import matplotlib.pyplot as plt
            import matplotlib.dates as mdates


| Function | Comment | Keywords |
|---|---|---|
|`fig, axs = plt.subplots(xshape,yshape)` | set up new figure as array of sub-plots `xshape` by `yshape` and return `fig` object for figure and `axs` object for subplots. `axs` is array of objects shape `(xshape,yshape)`, or single object if `(1,1)`. We often use `axs = axs.flatten()` to flatten the `axs` array to 1D.|`figsize=(sx,sy)` : set figure size `sx` by `sy`|
| `plt.savefig("ofile.png")` | Save plot to file `"ofile.png"` | 
| `fig.suptitle(name)` | set title `name` at top of figure `fig`
| `im = axs.plot(xdata,ydata,cs)` | plot line graph with `ydata` as a function of `xdata` and return plot object `im`. If argument `cs` is given, this is a colour/symbol e.g. `k+` for black crosses. | `label=str` : set `str` as label for this line. For use with `legend`| 
| `im = plt.errorbar(xdata,ydata)` | Error bar plot for `ydata` as a function of `xdata`. Needs kwarg | `yerr=yerr` : set y-error bar to values in array `yerr` |
| `axs.set_xlim(x0,x1)` | Set plot x-extent to from `x0` to `x1` |
| `axs.set_ylim(y0,y1)` | Set plot x-extent to from `y0` to `y1` |
| `axs.set_title(name)` | set sub-plot `axs` title to `name` |
| `axs.set_xlabel(xlab)` | set x-axis label to `xlab` |
| `axs.set_ylabel(ylab)` | set y-axis label to `ylab` |1
| `axs.legend()` | set legend in plot | `loc='best'` : best location, otherwise `top left` etc. |
| `mdates.MonthLocator()` | `MonthLocator` object of month locators, e.g. `months = mdates.MonthLocator()` |
| `axs.xaxis.set_major_locator(months)` | set major ticks on x-axis to `Locator` object of `months`|


Some colours and symbols:

| symbol/colour | name |
|---|---|
|'k+' | black plus |
|'r.' | red dot  |
|'go' | green circle  |
|'b-' | blue line  |
|'c--' | cyan dashed line  |
|'y-o' | yellow  line with circles  |


`datetime`

            from datetime import datetime
            
            
| function | comment |
|---|---|
|`datetime.now()` | date and time for now |
|`datetime(year, month, day, hour, minute, second, millisecond)` | return `datatime` object for time/date specified. Not all fields need be given. Can also use keywords but `year`, `month` and `day` must be given e.g.: `datetime(2020,day=1,month=2,hour=12)`|
| `datetime.day` | day etc. |
| `timedelta` | subtract two `datetime`s to get a `timedelta`|
|`timedelta.days` | number of days in `timedelta` |
| `dt.strftime("%H:%M:%S")` | represent `datetime` object `dt` as `hour:minute:second`|
| `dt.strftime("%m/%d/%Y")` | represent `datetime` object `dt` as `month/day/year`|
| `datetime.strptime(str,format)` | load string `str` into `datetime` object interpreting as format `format`, e.g. `datetime.strptime("11 November, 1918", "%d %B, %Y")` -> `1918-11-11 00:00:00`; e.g. `datetime.strptime("2020-06-20", "%Y-%m-%d")` -> `2020-06-20 00:00:00`|

#### Image Display

* [024_Image_display](024_Image_display.md)


            import matplotlib
            import matplotlib.pyplot as plt

            
|function|comment|  keywords|
|---|---|:--|
| `im = axs.imshow(data2D)` | Display image of 2D data array `data2D` on sub-plot axis `axs` and return display object `im` | `vmin=` : minimum threshold for image display |
| | | `vmax=` : maximum threshold for image display |
| | | `interpolation=` : interpolation style (e.g. `'nearest'` |
| `fig.colorbar(im)` | Set colour bar for image plot object `im` | `ax=axs` plot on sub-plot `axs` |
| `im.set_cmap(c)` | set colourmap `c` for image object `im` | 
| | Examples being `['Greys','gray','inferno_r','seismic']`|
| `cmap = matplotlib.colors.ListedColormap(list_of_colours)` | set `cmap` to `Colormap` object from list of colours `list_of_colours` |
|`norm = matplotlib.colors.BoundaryNorm(list, nbound)` | set `BoundaryNorm` object `norm` to boundaries of values from `list` with `nbound` values |
|`matplotlib.patches.Patch(color=c, label=l)`| Set patches for legend with colours from list `c` and labedl from list `l`|  
| `plt.legend(handles=patches)` | set figure legend using `patches` |`bbox_to_anchor=(1.4, 1)` : shift of legend|
| | | `facecolor="white"` : facecolourt of legend (white here) |
        

Modis library: 

            from  geog0111.modis import Modis
            modis = Modis(**kwargs)
            

            kwargs = {
                'tile'      :    ['h17v03'],
                'product'   :    'MCD15A3H',
                'sds'       :    'Lai_500m',
            }


| function|comment|example|
|---|---|---|
| `modis.get_data(year,doy)` | Dictionary of 2D data arrays by SDS key for MODIS product | `Modis(product='MCD15A3H',tile=['h17v03']).get_data(2019,41)`|

            

### Array data


#### 030 NASA MODIS Earthdata

[030_NASA_MODIS_Earthdata](030_NASA_MODIS_Earthdata.md)

[NASA Earthdata](https://urs.earthdata.nasa.gov/)

Some MODIS datasets


![MODIS tiles](https://www.researchgate.net/profile/J_Townshend/publication/220473201/figure/fig5/AS:277546596880390@1443183673583/The-global-MODIS-Sinusoidal-tile-grid.png)



* [`MCD15A3H` LAI/fAPAR](https://lpdaac.usgs.gov/products/mcd15a3hv006/)
* [`MCD64A1` Burned Area](https://lpdaac.usgs.gov/products/mcd64a1v006/)1
* [`MOD10A1 / MYD10A1 Snow Products`](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD10A1#bands)
* [`Land Cover dataset MCD12Q1`](https://lpdaac.usgs.gov/products/mcd12q1v006/)

#### 031 Manipulating data: `numpy`

[031_Numpy](031_Numpy.md)


            import numpy as np
            
 | Function | description   | keywords | 
 |---|---|---|
 |`np.array(x)` | convert `x` (e.g. list) to `numpy` array | `dtype=` : specify data type, e.g. `np.float`, `np.bool`, `np.int` |
 |`np.ones(s)` | generate array of values `1` of shape `s` |  `dtype=` 
  |`np.zeros(s)` | generate array of values `0` of shape `s` |  `dtype=` 
  |`np.linspace(start,stop,nsamp)` | generate array of `nsamp` values from `start` to `stop` |  `dtype=` |
| `np.arange(start,stop,step)` | generate array of numbers from `start` to (but not including) `stop` in steps of `step` | `dtype=` |
| `p0,p1 = np.mgrid[p0min:p0max:p0step,p1min:p1max:p1step]` | generate grids `p0`, `p1` of combinations of samples from `p0min` to (but not including) `p0max` in steps of `p0step` and `p1min` to (but not including) `p1max` in steps of `p1step`|
  | `a.astype(dtype)` | convert array `a` to data type `dtype` ||
  | a * b | multiply array `a` element-wise by array `b` , etc. for arithmetic|
 | `a.shape` | tuple giving shape of array `a` | 
 | `a.ndim` | tuple giving number of dimensions  of array `a` | 
 | `a.size` | tuple giving total number of elements in array `a` | 
 | `a[start:stop:step]` | array indexing for slice from `start` to `stop` in steps of `step` e.g. `np.array([2,5,3])[2:3])`|
 | `a[index]` | array indexing by explicit index tuple or tuple list e.g. `np.array([2,5,3])[(1,)]` |
 | `a.min()` | minimum value in array `a` | `axis=N` : value taken over axis `N` |
 | `a.max()` | maximum value in array `a` | `axis=N` : value taken over axis `N` |
 | `a.mean()` | mean value in array `a` | `axis=N` : value taken over axis `N` |
 | `a.std()` | standard deviation of values in array `a` | `axis=N` : value taken over axis `N` |
 | `a.var()` | variance of values in array `a` | `axis=N` : value taken over axis `N` |
 | `a.sum()` | sum of values in array `a` | `axis=N` : value taken over axis `N` |
 | `a.prod()` | product of values in array `a` | `axis=N` : value taken over axis `N` |
 |`np.median(a)` | median of values in array `a`, assumed `a` values in radians |`axis=N` : value taken over axis `N` |
 |`np.sqrt(a)` | square root of values in array `a` ||
  |`np.sin(a)` | sine of values in array `a`, assumed `a` values in radians etc.|
    |`np.exp(a)` | exponential of values in array `a`|
    
#### 031 More `numpy`

[032_More_numpy](032_More_numpy.md)


| Function | description   | keywords | 
 |---|---|---|
 | `np.loadtxt(f)` | Load datra from file `f` into numpy array ||
 | x[start:stop:step] | 1-D slice of array `x` ||
 | `slice(start:stop:step)` | function to apply to slice e.g. `x[slice(start:stop:step)]`|
 | `np.argmin(x)` | return 1D index of minimum value in array (/axis) |  `axis=N` : value taken over axis `N` |
 | `np.argmax(x)` | return 1D index of maximum value in array (/axis) |  `axis=N` : value taken over axis `N` |
 | `x > 1` | logical operator resulting in boolean array e.g. to use for masks |
 | `np.logical_not(x)` | element-wise not over array |
 | `np.logical_or(x,y)` | element-wise `a` or `b`  over array |
 | `np.logical_and(x,y)` | element-wise `a` and `b`  over array |
 | `np.where(x)` |  list of indices where `x` is `True` |
 | `x.flatten()` | convert copy of ND array `x` into 1D array |
  | `x.ravel()` | convert ND array `x` into 1D array |
| `x.reshape(shape)` | apply shape `shape` to array `x` |
| `np.unravel_index(indices,shape)` | unravel 1D indices `indices` to ND defined by `shape` |
| `np.newaxis` | add a new axis to array for reconciling multiple dimensions making a copy. Effectively makes new dimension of size `(1,)` |


### Geospatial data

#### 040 GDAL: mosaicing and masking

[040_GDAL_mosaicing_and_masking](040_GDAL_mosaicing_and_masking.md)


Modis library: 

            from  geog0111.modis import Modis
            modis = Modis(**kwargs)
            

            kwargs = {
                'tile'      :    ['h17v03'],
                'product'   :    'MCD15A3H',
                'sds'       :    'Lai_500m',
            }


| function|comment|example|
|---|---|---|
| `modis.get_data(year,doy)` | Dictionary of 2D data arrays by SDS key for MODIS product for year `year` and day of year `doy` | `idict = modis.get_data(2019,41)`|
|`modis.get_files(year,doy)`| Filename and SDS list of MODIS product for year `year` and day of year `doy` | `files, sds = modis.get_data(2019,41)`|
|`modis.get_modis(year,doy,warp_args=warp_args)` | Dictionary of 2D/3D data arrays by SDS key for MODIS product for year `year` and day of year `doy`, warped by `warp_args` (see `gdal.Warp()`). Note that `doy` can be list of `doys` or wildcard. If > 1 band, then dataset is 3D and key `bandnames` included |
            
`gdal`:


|function|comment|example and keywords|
|---|---|---|
|`g = gdal.Open(filename)` | Open geospatial file `filename` and return `gdal` object `g` (`None` if file not opened correctly)|
|`g.GetSubDatasets()` | Get list of sub-datasets from `gdal` object `g`| 
|`g.ReadAsArray(c0,r0,nc,nr)` | Read dataset from `gdal` object `g` into array. Form `c0` for `nc` columns and `r0` for `nr` rows. Set as `None` for defaults or don't give.|
|`gdal.BuildVRT(ofile, sds)` | create `gdal` VRT (wrapper) file called `ofile` for SDS/file `sds` | `files,sds = modis.get_files(year,doy)`|
||| `separate=True` for separate bands |
||| `ofile = f"work/stitch_full_{year}_{doy:03d}.vrt"`|
|||`stitch_vrt = gdal.BuildVRT(ofile, sds[0])`|
|`gdal.Info(f)` | Print information about geospatial file `f` ||
| `gdal.Warp(ofile,ifile)` | Warp `ifile` to `ofile` with keyword parameters | Keywords: 
|||`format = 'MEM'` or `format = 'GTiff'` : output format|
||| `options=['COMPRESS=LZW']` : compression option for GTiff etc.
||| `dstNodata=255`: no data value |
||| `cropToCutline = True` : whether to crop to cutline or bounds |
||| `cutlineDSName = 'data/TM_WORLD_BORDERS-0.3.shp'` : vector dataset for cutline|
||| `cutlineWhere = "FIPS='UK'"` : identifier information for cutline 
|`g.FlushCache()` | flush open `gdal` object `g` (force write to file) |

#### 041 GDAL: mosaicing and masking

[041_GDAL timeseries](041_GDAL_timeseries.md)




```python
from geog0111.modis_annual import modis_annual_dataset
help(modis_annual_dataset)
```

    Help on function modis_annual_dataset in module geog0111.modis_annual:
    
    modis_annual_dataset(year, tile, product, step=1, verbose=False)
    



```python
from geog0111.modis_annual import get_modis_annual
help(get_modis_annual)
```

    Help on function get_modis_annual in module geog0111.modis_annual:
    
    get_modis_annual(ifiles, sds=None, warp_args={})
    



```python
from geog0111.modis_annual import modis_annual
help(modis_annual)
```

    Help on function modis_annual in module geog0111.modis_annual:
    
    modis_annual(year, tile, product, step=1, sds=None, warp_args={}, verbose=False)
    



```python
from geog0111.get_lai_data import get_lai_data
help(get_lai_data)
```

    Help on function get_lai_data in module geog0111.get_lai_data:
    
    get_lai_data(year, tile, fips)
        Get the annual LAI dataset for fips, tile and year
        and return lai,std,doy
    


#### 043 Weighted interpolation

[043_Weighted_interpolation](043_Weighted_interpolation.md)

|function|comment|
|---|---|
|`scipy.ndimage.filters` | `scipy` filters |
|`zscipy.ndimage.filters.convolve1d(data,filter)` | 1D convolution of `filter` with `data`. Keywords : `axis=0,mode='wrap'`|


```python
from geog0111 import regularise
help(regularise)
```

    Help on module geog0111.regularise in geog0111:
    
    NAME
        geog0111.regularise
    
    FUNCTIONS
        regularise(lai, weight, sigma)
            takes as argument:
            
                lai     : MODIS LAI dataset:     shape (Nt,Nx,Ny)
                weight  : MODIS LAI weight:      shape (Nt,Nx,Ny)
                sigma   : Gaussian filter width: float
                
            returns an array the same shape as 
            lai of regularised LAI. Regularisation takes place along
            axis 0 (the time axis)
    
    FILE
        /nfs/cfs/home3/Uucfa6/ucfalew/geog0111/notebooks/geog0111/regularise.py
    
    

