import package._xmath as _xmath
print('# import xmath')
print(_xmath.pi)
print(_xmath.max(10, 5))
print(_xmath.sum(1, 2, 3, 4, 5))

print('# import xmath as math')
import package._xmath as math # 為 xmath 模組取別名為 math
print(math.e)

print('# from xmath import min')
from package._xmath import min  # 將 min 複製至目前模組，不建議 from modu import *，易造>成名稱衝突
print(min(10, 5))