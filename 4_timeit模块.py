# Time: 2021/11/9  15:57
import timeit


'''
第1 个参数是要为之计时的Python 语句
第2 个参数是建立测试的语句。timeit 模块会统计多次执行语句要用多久
默认情况下，timeit 会执行100 万次语句，并在完成后返回一个浮点数格式的秒数
'''
x = list(range(2000000))
pop_zero = timeit.Timer(stmt='x.pop(0)', setup='from __main__ import x')
print(pop_zero.timeit(number=1000))    # 2.0548364

pop_one = timeit.Timer(stmt='x.pop()', setup='from __main__ import x')
print(pop_one.timeit(number=1000))    # 4.2000000000097515e-05
