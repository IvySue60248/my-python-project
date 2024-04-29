# my-python-project
# 1, comment
‘#’ 单行注释

‘’‘  ’‘’ 多行注释

“”“ ”“” 多行注释

<img width="545" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/bcbca712-5348-406c-9ab1-dd8e497bf108">

# 2，intendent
类定义 函数定义 流程控制语句以及异常处理语句等行尾的冒号和下一行的缩进表示一个代码块的开始，而缩进结束，表示代码块的结束

通常采用4个空格作为一个缩进量

<img width="436" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/3afb43fb-1d6b-4256-9a38-7ffc3cdc256b">

# 3，String concatation

```
print("1 day is " + str(24) + " hours")
print(f"1 day is {24} hours")
print(f"10 days are {10 * 24 * 60} minutes")
```

# 4，variables
Python is dynamicaly typed

Naming convention: is a convention(generally agreed schema) for naming things.

<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/94869d8d-6e8f-413f-921a-5fbfeae128af">

# 5，functions
## 5.1 define function
A function is defined using the 'def' keyword

def function_name():

<img width="733" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/6362914f-8320-4aa2-8094-da6b19d5f9b3">

function与上边的代码块需要有两个空行，所以报了warning，增加一行空行后，就没有黄线了

<img width="739" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/c9bd4b90-5a7e-431a-9ea6-eae3fde74d93">
<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/c7a0d42e-0572-4c12-8463-a50d9e2a4c44">

调用function和Java一样

## 5.2 parameters
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/3f078571-4188-409a-b574-1e78ebe7b880">
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/681374b8-58f5-4fca-adca-000b52746714">

如果function有parameter，调用的时候不传参会报missing 1 required positional argument

## 5.3 scope
<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/39e82eec-e395-45a5-b9ac-afd8e8370f89">
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d433fa98-d937-497b-8589-350311ca6556">

## 5.4 function return type
也是不需要声明return type，直接return python就可以动态知道return type

```python
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


my_result = days_to_units(10)
print(my_result)
```

<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/b7cb0074-84ff-4295-8c70-a5a082f83881">

## 5.5 input()
x=input('提示文字')

input is a biult-in function

input() always returns a string.

示例:

input输入都作为字符串，如果想获取整数类型，需要使用int()函数转化，但int类型不能使用+在print中输出，需要使用，分隔

<img width="1039" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/21f7d6e1-a080-4035-895a-0e564f1cd7a0">

## 5.6, print()

语法结构：

print(输出内容)

print()函数完整的语法格式

print(value, ..., sep=' ', end=' ', file=sys.stdout, flush=False)

<img width="1046" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/0f5398f6-64c4-4ac2-a3d6-fad178a00174">

示例1，打印字符

print(chr(20145)) 打印出20145 ASCII码对应的字符

print(ord("北")) 打印北对应的ASCII码

示例2，输出内容到文件
<img width="716" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/ed226658-349b-497d-8c4a-44cd4b090732">

## 5.7, int()
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/ac09db54-4796-4c56-818b-04bb8a6da1c7">

如果不cast to int，计算就会不正常，输入被当作string来处理
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d6ad1f8a-e059-4314-8fc8-890b759ea9cf">

## 5.8, Conditionals(if/else) & Boolean Data Type

<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/c6565a0b-2a0e-4b2c-a77d-bd1e33ea2565">
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/696f44fe-a0b1-49cd-b94f-34fee33bee88">
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d8c51a5d-5458-476e-8219-1e52ae7d622c">
<img width="737" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/015df2dd-312c-4475-8727-49f56dfed569">

use type() to get value type

<img width="738" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/701a598a-7560-4c4a-a17a-823ce507538a">

在python中，不是用else if，而是elif


## 5.9, More user input validation
<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/2928ed0f-2f54-4f87-b370-edbcc4bb7b41">
<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/dfa5b446-cd5d-49e2-8d59-53c5ca04569b">
my_input.isdigit() 返回bool类型，判断user input是否是数字类型，如果输入是float类型，这个方法也会返回false，negative number也会返回false
<img width="739" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/3420c986-958a-46ac-a080-72d086c23904">
<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/756013e3-afcb-4ba3-9c67-bf50c060036b">

## 5.10, Clean up our code

将某段可能被重复调用的逻辑抽成function

<img width="738" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/619d27c8-f65e-4cb0-b4f8-9f884c842c60">

## 5.11, Nested if...else
<img width="733" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/06d63122-24df-4961-8931-e7029aa3ff91">

# 6, Error Handling with try/except

<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/601b6954-09e9-4dc3-94d5-118ee6f925f1">

- python中使用try/except，其他语言用try/catch
- 如果不想指定error type，可以直接写except:就会handle所有的异常，虽然会有warning，但是不影响程序


# 7, While loops
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/abfbfdf3-3fdd-4145-a6c2-c1d31fe42028">
注意python中true的关键词首字母要大写

Let user exit the program

<img width="738" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/7de85c73-85ca-49f9-9d20-946c97b38501">

# 8,List & For Loop
不想每次输入一个数字，希望输入一个list，遍历这个list输出结果

<img width="738" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/21058284-846c-4232-aa26-462aa548c01f">

这里有两点需要注意：
1，input返回永远是string，如果要转成list，需要使用.split()函数，可以传入分隔符，默认是空格

2，num_of_days_element是在for loop中声明的，就如同先声明了一个变量num_of_days_element然后将list中的对象赋值给num_of_days_element，所以对validate_and_execute()可见，这是和Java不一样的点


## 8.1, Basic list operations
- Create a list
  ```my_list = ["January", "February", "March"]```
  
- Access items of the list
  ```
  my_list[0]
  my_list[1]
  my_list[2]
  ```
- Add an item to the list
  ```my_list.append("March")```
- Remove an item from the list
  ```
  my_list.remove("Feb")
  ```
- Change items in the list
  ```
  my_list[2]="May"
  ```

# 9, Sets
<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/29dd02fd-ebe0-4d02-a6ea-e23aeb965f5e">
set中不允许包含重复value，python中使用set()将list转为set

## 9.1, Basic set operations
- Create a set
  ```
  my_set = {"a", "b", "c"}
  ```
- Access items only via loop
  ```
  for element in my_set:
      print(element)
  ```
- Add an item to the set
  ```
  my_set.add("d")
  ```
- Remove an item from the set
  ```
  my_set.remove("c")
  ```

<img width="733" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/353d1d1b-7c8a-4985-b844-4b8eb5252603">

## 9.2, differences between set and list
- set 不允许有重复元素
- set是无序的，每次打印出来结果可能都不一样，list是有序的，比如list中有两个相同的元素，用list.remove()方法默认删除第一个


# 10, Built-in functions
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/f62ee2b3-133b-4bbd-a914-e3f5d177191c">
<img width="737" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/80b1572d-e712-4eec-80ce-42c42177d954">
<img width="733" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/a23401d7-a147-45c9-aea3-80225394dba2">
某种数据类型比如String，也有自己的built-in function

# 11, Dictionary Data Type
类似Map

<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/1e9c3ff5-86b8-4a00-bebe-d68d786448d1">
访问dictionary的value，可以用dictionary["key"]

<img width="732" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/69f92f70-f081-43f1-ace7-a0851904d135">
<img width="731" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/c98ec6a7-7641-4878-b627-bbdecac8d54d">
dictionary的type是dict

不同的数据类型
```

message = "some value"
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [10, 20, 30, 10]
list_of_months = ["January", "February", "March"]
set_of_days = {10, 20, 30}
dict_of_days_and_unit = {"days": 20, "unit": "hours"}
```

# 12, Modules
<img width="731" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/9c290174-6ea8-4eae-9cfc-d0684477642b">

Modules: 
1, is just a .py file
2, one module could use another module

## 12.1 Create a Module & import statement
创建module，其实就是创建一个新的py file
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/e7dd646e-ecdb-43af-915d-5e05b132bc0e">

import module
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/3cf9cc7f-88a5-49ea-896d-f99f6d60ac80">
但并不是所有的helper module中的function都会被main.py用到，python和java不同的一点是可以import精确到function
<img width="737" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/c5380092-f72c-4efb-a66e-34868d649bbb">

module中也不是只能定义function，也可以定义variables
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/3e9909e7-1122-4be4-b57c-1c90cc299989">
<img width="738" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/f21c336b-3d95-44cd-80a4-7732164081e1">

如果import后跟的方法或者变量太多，也可以使用from helper import * 
其实功能与import helper没有区别，区别就在于使用上，用import helper的话需要在调用方法或者变量时加上helper. 但是如果用from helper import *就可以直接用方法或者变量

在helper module中定义的function或者variables都叫definitions

## 12.2 rename module
<img width="737" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/61603c52-600a-43fa-8660-69b58b4b3cbf">

## 12.3 Built-in python modules
<img width="733" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/4a71d9b3-73f7-49d4-9db9-c9162f7a860b">
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d3c7d42a-652f-44e1-b1e3-5f9827b9d802">

## 12.4 Built-in module examples
<img width="732" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/087abd86-a94c-4d8a-ac55-592f6f817009">
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d9b80087-07af-4829-9bb7-00b411a99daa">

# 13, Project exercises
<img width="734" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d9c9d98f-109c-4074-91c1-5c73544b4a72">
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/a83550f2-da48-42fb-972a-298518dce814">
也可以省掉module，用from datetime import datetime
<img width="733" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/0c3f369b-2546-497b-bd7f-b93b076b1318">

# 14, Built-In vs. Third-Party
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/cf502590-01be-41da-99f9-e1328bd84f25">

## 14.1, module vs package
PyPI: python package index https://pypi.org/
- module: Any Python file is a module
- package: 
is a collection of Python modules, contains multiple python files

must include an _init_.py file

This _init_.py file distinguishes a package from a directory

<img width="739" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/e45998a9-229d-493d-adf1-5c41ce14ee12">

## 14.2, install package
```
pip install Django
```

<img width="737" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d8b4c5a3-63b1-4c7b-88e5-6e5e5a7492d7">

<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/f9db9269-0f42-4fdf-900b-9a34485aa80a">

在pycharm中执行pip install，可以直接将package导入进项目
如果要移除package，用
```
pip uninstall Django
```

也可以用pycharm自带的package tool window去install package\
<img width="732" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/69ad009a-71d1-4592-87bc-3175e416694a">

# 15, Project introduction
实现一个读取文件并操作文件的项目
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/8459e4aa-b762-424d-b7a7-251a5f111dce">

<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/adb3557c-a875-4178-89d3-de3af6f45078">

可以用built-in io module或者用python package openpyxl
<img width="736" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/1a55ea29-31bc-49d2-a6c5-3412519612c9">

Exercise1:
计算每个公司多少种产品
<img width="735" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/df0d955f-0192-48e9-b8e3-770e58b4b21f">
<img width="738" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/391c84f5-63e5-4948-90e2-fdf0035ef15c">

Exercise2:

计算每个supplier的total value of inventories

Exercise3:

计算inventory少于10的product number

```
import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

product_suppliers = {}
total_value_per_supplier = {}
product_inventory_under_10 = {}

#range：从2到最大行连续的数字list [2,3,4,5,6.....max_row+1],因为是不包含最后一个数字的，所以需要max_row+1
for prod_row in range(2, product_list.max_row + 1):
    #product_list.cell(row_num, column_num)可以定位到一个单元格，.value可以取出其中的内容
    supplier_name = product_list.cell(prod_row, 4).value
    inventory = product_list.cell(prod_row, 2).value
    price = product_list.cell(prod_row, 3).value
    product_number = product_list.cell(prod_row, 1).value

    # calculation number of products per supplier
    if supplier_name in product_suppliers:
        current_num_prod = product_suppliers.get(supplier_name)
        product_suppliers[supplier_name] = current_num_prod + 1
    else:
        product_suppliers[supplier_name] = 1

    # calculation total value of inventories per supplier
    if supplier_name in total_value_per_supplier:
        current_value = total_value_per_supplier.get(supplier_name)
        total_value_per_supplier[supplier_name] = current_value + inventory * price
    else:
        total_value_per_supplier[supplier_name] = inventory * price

    # calculation product number with less than 10 inventory
    if inventory < 10:
        product_inventory_under_10[int(product_number)] = inventory

print(product_suppliers)
print(total_value_per_supplier)
print(product_inventory_under_10)
```

Exercise4:

在excel中增加一列展示total value，最后需要保存文件，save不会直接保存源文件，是会copy出一份，所以需要给个新名字

<img width="1031" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/d2c932f3-5306-4f94-a4ea-2245bc935bc8">

# 16, Classes & Objects
## 16.1, Create a new class
<img width="1207" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/11a2acfa-e970-4f3c-9732-2d33d033c304">
<img width="1209" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/17223814-ffdc-40c6-bdf6-724f5b789317">
<img width="1208" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/da9372d9-886f-4d47-9382-ea236d03b1bc">
<img width="1211" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/328e6351-6afc-4e6e-bba5-f3a524be7cd9">
<img width="1209" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/485a3571-4596-4e4e-b262-8428ee71a929">


## 16.2 Create an object
<img width="1209" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/6bf9443a-2680-4cd1-bbcf-f923cc6cef26">
<img width="1207" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/19bc2e09-b08f-4470-8f78-45464be22b1c">
<img width="1211" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/586c1f6d-68ee-442d-b5a3-dcf93685f17b">

## 16.3 oriented programming
<img width="1210" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/302435fd-6857-418d-ab1d-b4aa1b82d452">

<img width="1211" alt="image" src="https://github.com/IvySue60248/my-python-project/assets/8510927/2e653127-6fd3-4d9d-beae-9388d16f22ec">

# 17, Request API
```
import requests


def get_github_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        return None


username = 'IvySue60248'
repositories = get_github_repositories(username)
if repositories:
    for repo in repositories:
        print(repo['name'])
else:
    print('Failed to fetch repositories')
```

需要安装requests module
```
pip install requests
```





















































