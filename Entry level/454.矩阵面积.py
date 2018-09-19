# 题目描述：
# 实现一个矩阵类Rectangle
# 包含：
# 公有的成员变量width和height，分别代表宽度和高度
# 构造函数，接受两个参数width和height，设定矩阵的宽度和高度
# 成员函数getArea，返回这个矩阵的面积
# 输入：width，height
# 输出：矩阵的面积
# 样例：3，4 --> 12
############
# 题目分析：考察Python面向对象编程
############
# 知识点：
# 1. 创建类：使用class语句加类名的方式
# 2. __init__()：Python类的特殊方法名称，对目标对象进行初始化操作
# 3. self：类方法的特定参数，引用的是对象本身，必须写在类方法的参数列表开头
class Rectangle:
    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here
    def __init__(self, width, height):
        self.width = width
        self.height = height
    '''
     * Define a public method `getArea` which can calculate the area of the rectangle and return.
    '''
    # write your code here
    def getArea(self):
        return self.width * self.height
if __name__ == '__main__':
    w = int(input('Enter a rectangle width:'))
    h = int(input('Enter a rectangle height:'))
    rec = Rectangle(w, h)
    print(rec.getArea())
