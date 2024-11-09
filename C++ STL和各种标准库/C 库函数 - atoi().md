# C 库函数 - atoi()

[![C 标准库 - ](https://www.runoob.com/images/up.gif) C 标准库 - ](https://www.runoob.com/cprogramming/c-standard-library-stdlib-h.html)

## 描述

C 库函数 **int atoi(const char \*str)** 把参数 **str** 所指向的字符串转换为一个整数（类型为 int 型）。

## 声明

下面是 atoi() 函数的声明。

```
int atoi(const char *str)
```

## 参数

- **str** -- 要转换为整数的字符串。

## 返回值

该函数返回转换后的长整数，如果没有执行有效的转换，则返回零。

## 实例

下面的实例演示了 atoi() 函数的用法。

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   int val;
   char str[20];
   
   strcpy(str, "98993489");
   val = atoi(str);
   printf("字符串值 = %s, 整型值 = %d\n", str, val);

   strcpy(str, "runoob.com");
   val = atoi(str);
   printf("字符串值 = %s, 整型值 = %d\n", str, val);

   return(0);
}
```

让我们编译并运行上面的程序，这将产生以下结果：

```
字符串值 = 98993489, 整型值 = 98993489
字符串值 = runoob.com, 整型值 = 0
```