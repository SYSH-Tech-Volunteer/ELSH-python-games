---
marp: true
theme: uncover
paginate: true
backgroundColor: #4C7F99
color: #fff
---
<style>
  :root{
      --color-background-code: #222222;
      --color-foreground: #FFF;
    }
  marp-pre,.language-python{
    border-radius: .5em;
    color:#FFF;
   padding: 1.2em!important;
  } 
  code{
    border-radius: 7px;
}
</style>

<!-- _backgroundImage: #000 -->

# Python基礎語法

![bg left 50%](img/python.png)

---

# Python 簡介

* 直譯式程式語言
* 易於學習、閱讀和維護
* 廣泛應用於AI領域
* **做遊戲**

---

# 變數

* 儲存資料
* 數字不可用於開頭字元。
* 可以使用英文字元、數字或下底線(_)命名。ex : number_id
* 英文大小寫是有差異的。
* 名稱不可使用python語言保留字詞。ex : int
* python會自己判斷資料型態
  
```python
x = "我是變數"
```

---

## 輸入

```python
x = input("Hello world")
```
## 輸出


```python
print("Hello world")
```



---

# 實作時間
### 題目:"輸出"一個叫做"x"的"變數"
### 輸出結果會是"Hello World"  
* 在Hello World前後要加上'' or ""
(表示是字元或是字串)

---

# 解答

```python
x = input("Hello World")
print(x)
```

---

![bg fit](img/keyword.jpg)

---

# 資料型態
* 數值型態(Numeric type) - int, float, bool
* 字串型態(String type) - str
* 容器型態(Container type) - list, set, dict, tuple
* 用type()查看資料型態

---

# 數值型態

* int 
  * 整數
* float
  * 浮點數(有小數點)
* bool
  * ture
  * faulse

---

# 字串型態
* str(string)
* 字串
* 用''或""包住
* 可用+連接
* len()查看長度

---

# 容器型態之一:list

* 放多個資料的地方
* 由**中**括號組成並以逗號隔開不同資料(型態可不同)
* 索引值從0開始

```python
i_am_list = []# 宣告一個變數叫i_am_list
```

---

# 容器型態之二:tuple

* 放多個資料的地方
* 由**小**括號組成並以逗號隔開不同資料(型態可不同)
* 索引值從0開始
* 建立時就必須決定初執
* 建立後就只能讀取值，不能再修改

---

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # 可以是巢狀的:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # 不能更改:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # 但是可以包含list:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

---

# 運算子

## 算術運算子

* `+`加  
* `-`減
* `*`乘
* `/`除
* `%`取餘數
* `**`指數


---

# 簡寫
### `x+=1`表示 `x=x+1`
### `x-=1`表示 `x=x-1`

---
## 關係運算子

<	小於
\>	大於
<=	小於等於
\>=	大於等於
==	相等
!=	不相等

---

# 練習時間

題目:咖啡一杯50元，現在商店有特價活動，咖啡第二杯只要20元，假設今天小白要買x杯，算出他最少只要付多少元
* 請輸出:最少只要付多少?元

提示:設x變數並且input 


---

# code

```python
x = int(input())
print(x/2*70+x%2*50)
```

---

## 邏輯運算子
* `「and:且」`
全都正確才正確  
* `「or:或」` 
一個正確才正確
* `「not:非」`
對-->錯;錯-->對

---

## if

判斷條件 
* 對-->執行if中的程式  
* 錯-->跳出if往下執行，執行else

---

<!-- _backgroundImage: #000 -->

## else-if

* 用於多的條件時
* if執行時會跳過elif和else
* if是錯的-->判斷else-if，都錯-->執行else

![bg right 90%](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlRt7WwPTGLYcUCpLr2Nx-2GYsRcvbEj_A4g&s)

---

```python
x = True
y = False
if y:               # False
  print("No way")
elif x and y:       # True and False
  print("come on!")
elif not x:         # not True
  print("please")
else                # do this
  print("嗨壓")
```

---

# 成績問題
輸入分數
如果考`90-100` 輸出`A`
如果考`80-89` 輸出`B`
如果考`70-79`輸出`C`
如果考`60-69` 輸出`D`
如果低於`60分` 輸出``
* 請輸出:(成績)
提示:設score變數並且input 使用if else if...
---

# 解答
```python
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("完蛋被當了")


```

---

# 迴圈

重複執行類似的事

![bg right:60%](img/loop.gif)

---

# for 
可以透過Python迴圈來讀取串列中的每一個元素
較適用於「已知迴圈數」的問題
格式：

```python
for x in range(1, 10, 2):
   # 放要執行的東西
```

range(起始值,結束值,間距值)

---

# while

較適用於「無法預知迴圈數」的問題
格式：

```python
while 條件:   # 條件成立
    # 放要執行的東西
```

---

# break

強制跳出整個迴圈

```python
for i in range(1,5):
  if(i == 3):
    break
print(i) # 所以結果會列出3
```

---

## continue

強制跳出這過迴圈

```python
for i in range(1,5):
  if(i == 3):
    continue
print(i) # 會列出5
```

---

# 練習時間

* 輸入為一個整數 
* 大於 0、整數2的k次方(k為整數)、小於 ，請輸出所有可能的數字。

---

# 解答
```python
x=int(input())
n=2
while n<x:
  print(n)
  n=n*2
```
---
# 函式

讓你的程式碼被重複的使用，並且提高維護性及可讀性

用法：

def 函式名稱(參數):
    函式主體

```python
def greet(name):
    """這個函式用於問候"""
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!
```

---

# class

可以想成是自訂的資料型態，由變數和函式組成

```python
class Student:                               # 建立一個較Student的類別，開頭習慣大寫
    def __init__(self, number, name, score): # 初始化函式，宣告物件就會執行的函式
        self.number = number                 # self代表物件本身，所有類別裡的函式都要有
        self.name = name                     # 把自己的number name score 設成宣告時指定的
        self.score = score

    def get_number(self):                    # 自訂的函式
        return self.number                   # 回傳自己的座號

    def get_score(self):                     # 自訂的函式
        return self.score                    # 回傳自己的分數

Student st1(100, "abc",50)
Student st2(99, "def",60)
print(st1.get_number(), st1.get_score())
```

---

# pygame

---

# 安裝pygame

1. Window鍵
2. cmd
3. pip install pygame

---

# 基本架構

![bg pygame.png](img/pygame.png)

---

# 座標

數學的原點是在中心點。往右x增加，往上y增加。


但是在程式裡面 原點是在「左上角」，且往下y增加。

![bg position.gif](img/position.gif)

---

# 初始化

```python
pygame.init()
# 設定視窗大小，可以改變參數設定成喜歡的大小
display = pygame.display.set_mode((800,600))
# 設定標題
pygame.display.set_caption("HELLO")
# 這邊會顯示黑色，可以透過修改參數的方式改成自己喜歡的顏色
display.fill((0,0,0))
```

---

# 事件(pygame.event)

* 退出
  * `pygame.QUIT`若使用者按下了右上角的叉叉
* 滑鼠
  * `pygame.MOUSEBUTTONDOWN`按下滑鼠按鍵
  * `pygame.MOUSEMOTION`移動滑鼠
  * `pygame.mouse.get_pos()`抓取滑鼠的位置

---

* 鍵盤
  * `pygame.KEYDOWN`按下鍵盤按鍵
  * `pygame.K_UP`上
  * `pygame.K_DOWN`下
  * `pygame.K_W`W鍵

---

# 圖形

* 線段
* 多邊形
* 方形
* 圓形
* 匯入圖片

---

## 線段

```python
pygame.draw.line( surface, color, ( x1, y1 ), ( x2, y2 ), width = 0 )
'''
surface : 想畫在哪個平面(剛剛的display)
color : 顏色
x1 跟 y1 : 起始位置的 x 和 y 座標
x2 跟 y2 : 終點位置的 x 和 y 座標
width : 粗度
'''
```

---

# 多邊形

```python
pygame.draw.polygon( surface, color, points, width=0 )
'''
points : 點座標集合，點越多就可以畫出越多邊 像是 [ ( 146, 0 ), ( 291, 106 ), ( 236, 277 ), ( 56, 277 ), ( 0, 106 ) ] 就可以畫出一個五邊形。
width : ( 可以不用加，預設是0 ) 增加多邊形的粗度。
width > 0 : 空心的多邊形，線段會因為 width 增加而加粗。
width = 0 : 填滿的多邊形。
width < 0 : 什麼都沒有，什麼都看不到。
'''
```

---

# 方形

```python
pygame.draw.rect(surface, color, rect)
'''
rect : Rect物件，可以直接寫( x, y, width, height )
x : 方形左上角的x座標
y : 方形左上角的y座標
width : 方形的長
height : 方形的寬
'''
```

---

# 圓形

```python
pygame.draw.circle( surface, color, center_point, radius, width )
'''
center_point : 中心點
radius : 半徑
width : 請參考多邊形的width
'''
```

---

# 資料來源

* [https://hackmd.io/@andy010629/r103KC6Iv](https://hackmd.io/@andy010629/r103KC6Iv)
* [https://hackmd.io/@Derek46518/HyZHsD0Qo](https://hackmd.io/@Derek46518/HyZHsD0Qo)
