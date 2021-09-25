# https://www.acmicpc.net/problem/1673

while True:
    try:
        coupon, stamp = map(int, input().split())
        res = coupon

        while coupon // stamp:
            res += coupon // stamp
            coupon = coupon // stamp + coupon % stamp
        
        print(res)
        
    except:
        break