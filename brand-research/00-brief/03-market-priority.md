# 市场优先级与进入顺序

> v0.1。依据 `07-pricing/01-cost-and-pricing-model.md` 的测算与清关/平台结构调研。

## 结论：**日本 → 新马 → 韩国 → 东南亚其余（推迟）**

| 排序 | 市场 | 定价 | 毛利率 | 进入难度 | 判断 |
|---|---|---|---|---|---|
| **1** | **日本** | ¥15,800 | **54.8%** | 中 | ✅ **首发**。品类文化母国，IG 渗透率高，免税线内，客单接受度最好 |
| 2 | 新加坡 / 马来西亚 | $105 | ~53% | 低 | ✅ 同期开放。英语、购买力接近、物流便利、无需额外本地化 |
| 3 | 韩国 | ₩137,000 | 46.6% | **高** | ⚠️ 第 2–3 季再进。PCCC + 支付通道是硬工程 |
| 4 | 泰/越/印尼/菲 | — | — | 高 | ❌ 第 1 年不做，见下 |

---

## 为什么首发选日本

1. **品类文化母国**。女仆 / 量産型 / 地雷系审美的原产地，不需要教育市场"这是什么"
2. **免税线恰好容得下我们的定价**。¥15,800 完税价 ¥9,480，在 ¥10,000 线内 → 客户无额外税费摩擦
3. **Instagram 在 20–30 岁日本女性中渗透率极高**，且日本 IG 用户有强烈的"保存/收藏"行为 → 有利于视觉驱动的品牌
4. **物流最便宜**（<500g 约 $4.5），且中日专线时效稳定（3–6 天）
5. **支付基础设施成熟**：Shopify 原生支持日本，PayPay / コンビニ払い / JCB 可接

### 日本市场的两个必须做对的事

- **尺码表本地化**。日式罩杯体系（B70/C75…）≠ 欧美（32B/34C）。必须给日式标注 + 实测三围 cm + 面料弹性说明。尺码不清在日本 = 不下单
- **文案必须是母语级日语**。机翻日语在日本是致命的信任崩塌。这一项不能省钱

---

## 为什么韩国排在日本之后（而不是同步）

韩国的审美契合度其实很高，但**进入成本是工程性的**：

| 障碍 | 说明 |
|---|---|
| **PCCC 个人通关码** | 海关强制，13 位 P 开头；2025 年 1 月起护照号不再被接受。结账必须加字段。这是韩国跨境电商第一大弃单原因 |
| **支付通道** | Shopify Payments 不支持韩国本地支付，需另接 KakaoPay / Naver Pay 网关 |
| **流量结构** | Meta 在韩国弱于日本，主战场是 Naver Blog / KakaoTalk / 올리브영 生态，需要另一套打法 |
| **CAC 更高** | 测算按 $30，高于日本的 $25 |

→ **不是不做，是不同步做**。先在日本跑通产品和内容，再把成熟素材本地化到韩国。

---

## 为什么东南亚第 1 年不做

**① 平台垄断 99%**
Shopee + TikTok Shop + Lazada 合计约占东南亚平台电商 GMV 的 99%。
独立站在该区域不被搜索、不被信任、不被行业数据追踪。**用 Shopify 打东南亚是逆水行舟。**

**② 免税额正在被集体取消（2025–2026 年这一波）**
- 泰国：2026 年 1 月起完全取消 de minimis，所有进口件征税
- 越南：2025 年 2 月起取消约 $40 的免税额
- 马来西亚：10% 低价值商品税
- 新加坡：S$400 以下由卖家在销售时代收 GST

**③ 客单价撑不住 $105**
印尼、越南、菲律宾、泰国的可支配收入无法支撑主力价格带。
降到 $59 虽仍有 47% 毛利，但**那是另一个品牌定位**——
和日韩的高端叙事共用一个店，会直接摧毁溢价能力。

### 东南亚的正确进法（第 2 年）

开 **Shopee / TikTok Shop 独立店铺**，用**副线品牌 + 副线 SKU（$49–69）**，
与主品牌**价格带隔离**。新加坡、马来西亚是例外，可并入第 1 年 DTC。

---

## 对后续工作的影响

| 影响到 | 怎么改 |
|---|---|
| 阶段 2 竞品调研 | **权重：日本 50% / 韩国 25% / 欧美(作为审美参照) 25%**；东南亚只做背景扫描 |
| 阶段 3 KOC 名单 | 优先抓日本 IG / X 账号；韩国次之 |
| 阶段 5 建站 | **首发只做日语 + 英语双语**，韩语第 2 季再加 |
| 阶段 6 内容 | 以日语内容为第一优先，英语为溢出 |

## 资料来源

- [Japan Customs — 1006 Duty exemption for goods at a total customs value of 10,000 yen or less](https://www.customs.go.jp/english/c-answer_e/imtsukan/1006_e.htm)
- [Zonos — A cross-border guide to ecommerce in Japan](https://zonos.com/docs/guides/country-guides/japan)
- [Zonos — Country-specific de minimis values](https://zonos.com/docs/guides/de-minimis-values)
- [Hinrich Foundation — The twilight of de minimis](https://www.hinrichfoundation.com/research/article/trade-governance/twilight-of-de-minimis)
- [Thailand Reshapes E-Commerce Landscape by Imposing Duties on All Low-Value Imports (US-ASEAN Business Council)](https://www.usasean.org/article/thailand-reshapes-e-commerce-landscape-imposing-duties-all-low-value-imports)
- [Momentum Works — Southeast Asia's platform ecommerce reaches US$157.6B](https://thelowdown.momentum.asia/new-report-southeast-asias-platform-ecommerce-reaches-us157-6b-in-2025-with-top-platforms-expanding-share-to-98-8/)
- [Cube.asia — Shopee, Lazada, and TikTok Shop in Southeast Asia: What the Data Shows in 2026](https://cube.asia/shopee-lazada-and-tiktok-shop-in-southeast-asia-what-the-data-shows-in-2026/)
- [Worldshopping — Is Korean PCCC required when ordering?](https://help.worldshopping.global/hc/en-us/articles/4830455037982-Is-Korean-PCCC-Personal-Customs-Clearance-Code-required-when-ordering)
