#!/usr/bin/env python3
"""Éperdue 成本/定价模型 — 日韩东南亚版。改参数重跑即可。"""

FX_RMB = 7.10      # RMB per USD
FX_JPY = 150.0     # JPY per USD
FX_KRW = 1380.0    # KRW per USD

COGS_RMB = 55.0    # 裸价 ¥50-60 取中值

def unit(retail, cogs_rmb=COGS_RMB, pack=4.0, ship=5.0, cac=25.0,
         ret_rate=0.06, pay_pct=0.034, pay_fix=0.30, fixed=1.50, label=""):
    """pay_pct 默认 3.4%：跨境卡 + 本地支付方式通道费普遍高于美国本土 2.9%"""
    cogs = cogs_rmb / FX_RMB
    pay = retail * pay_pct + pay_fix
    ret_cost = ret_rate * (retail * pay_pct + ship + pack + cogs * 0.35)
    total = cogs + pack + ship + cac + pay + ret_cost + fixed
    gp = retail - total
    print(f"{label:<26} ${retail:>6.1f} | COGS {cogs:5.2f} pack {pack:4.1f} "
          f"ship {ship:4.1f} CAC {cac:5.1f} pay {pay:5.2f} ret {ret_cost:4.2f} "
          f"fix {fixed:4.1f} | cost {total:6.2f} | GP ${gp:6.2f} ({gp/retail*100:5.1f}%)")
    return gp

print("=== 1. 零售价扫描（日本线：包装$4 运费$5 CAC$25）===")
for r in (39, 49, 59, 79, 99, 105, 119):
    unit(r, label=f"零售 ${r}")

print("\n=== 2. 三个市场（各自真实参数）===")
unit(105, pack=4.0, ship=4.5,  cac=25.0, label="JP  ¥15,800")
unit(99,  pack=4.0, ship=5.0,  cac=30.0, label="KR  ₩137,000")
unit(59,  pack=2.5, ship=6.0,  cac=10.0, ret_rate=0.08, label="SEA $59 (DTC)")
unit(59,  pack=2.5, ship=6.0,  cac=4.0,  ret_rate=0.10,
     pay_pct=0.12, pay_fix=0.0, label="SEA $59 (Shopee抽佣~12%)")

print("\n=== 3. CAC 敏感性（零售 $105）===")
for c in (10, 20, 30, 40, 55):
    unit(105, ship=4.5, cac=c, label=f"CAC ${c}")

print("\n=== 4. 日本免税天花板 ===")
ceil_jpy = 10000 / 0.6
print(f"  个人进口完税价 = 零售 x 60%；完税价 <= ¥10,000 免关税+消费税")
print(f"  => 零售价上限 ¥{ceil_jpy:,.0f}  (约 ${ceil_jpy/FX_JPY:.0f} USD)")
print(f"  建议定价 ¥15,800 = ${15800/FX_JPY:.0f}，完税价 ¥{15800*0.6:,.0f} ✅ 安全裕度 5%")

print("\n=== 5. 韩国免税天花板 ===")
print(f"  非美产地 de minimis = $150（不含运费）")
print(f"  建议定价 ₩137,000 = ${137000/FX_KRW:.0f} ✅ 远低于门槛")
