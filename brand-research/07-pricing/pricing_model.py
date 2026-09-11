FX = 7.10  # RMB per USD

def model(name, retail, cogs_rmb, pack, ship, cac, ret_rate=0.06, pay_pct=0.029, pay_fix=0.30, fixed=1.50):
    cogs = cogs_rmb / FX
    pay = retail * pay_pct + pay_fix
    # returns: lose shipping + packaging + a share of goods, plus refund the retail
    ret_cost = ret_rate * (retail * pay_pct + ship + pack + cogs * 0.35)
    total = cogs + pack + ship + cac + pay + ret_cost + fixed
    gp = retail - total
    print(f"{name:<22} retail ${retail:>6.0f} | COGS {cogs:5.2f} pack {pack:4.2f} ship {ship:5.2f} CAC {cac:5.2f} pay {pay:5.2f} ret {ret_cost:5.2f} fix {fixed:4.2f} | cost {total:6.2f} | GP ${gp:6.2f} ({gp/retail*100:5.1f}%)")
    return gp

print("=== 成本固定，测不同零售价 (COGS 100rmb, 品牌包装 $5, 国际专线 $7, CAC $25) ===")
for r in (49, 69, 89, 109, 129, 149):
    model(f"零售 ${r}", r, 100, 5.0, 7.0, 25.0)

print()
print("=== CAC 敏感性 (零售 $109) ===")
for c in (10, 20, 30, 45, 60):
    model(f"CAC ${c}", 109, 100, 5.0, 7.0, c)

print()
print("=== 三条路线 ===")
model("A 中端走量 $49", 49, 100, 2.5, 5.0, 12.0)
model("B 中高端 $109", 109, 100, 5.0, 7.0, 25.0)
model("C 高端限量 $149", 149, 130, 9.0, 9.0, 30.0)
