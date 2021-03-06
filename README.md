# MAP-E(v6プラス) CE情報の計算スクリプト

v6プラスでIPv4 over IPv6を構成する際の  
CE(自宅ルーター)とBRが通信する際のCE側のv4アドレス、v6アドレス、利用可能ポートを計算

## 参考にさせて頂いたサイト

[NanoPi NEO2をv6プラスのルーターにする 前編 - がとらぼ](https://gato.intaa.net/archives/13173)


## How to use


```sh
# python >= 3.9

python v6plus.py "<自動で付与されたv6アドレス>/64"

```

### 例

```sh
# 実行例
python v6plus.py "240B:10:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/64"
```


```sh
# Output
CE IPv4: 106.72.x.x
CE IPv6: 240B:10:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
PSID: xx #16進数
Available ports below:
  xxxx-xxxx
  xxxx-xxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx
  xxxxx-xxxxx

```

