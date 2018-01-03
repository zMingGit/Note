# Add operation without +

solution:  
- 取原码
- 转补码[为了负数能够运算]
- 相加[利用^保存不进位的数据，用&保存进位数据，用<<来进位，然后重复运算]
 转补码[为了识别负数]

code:

```
def main(a=-100, b=100):
  if a < 0:
    a = abs(a) + 2147483648
  if b < 0:
    b = abs(b) + 2147483648
  print a,b
  a = get_complement(a)
  b = get_complement(b)
  print a,b
  sum =  get_sum(a, b)
  print '-sum'
  print sum
  sum = get_complement(sum)
  print sum
  if sum > 2147483648:
    return -(sum - 2147483648)
  else:
    return sum
    
  

def get_complement(x):
  if x > 2147483648:
    res = x ^ 2147483647
    res += 0b1
    return res
  else:
    return x

def get_sum(a, b):
  sum = a ^ b
  t = (a & b) << 1
  while t:
    temp = sum
    sum ^= t
    t = (temp & t) << 1
    if sum >= 4294967296:
      sum -= 4294967296
  return sum



print main()
```