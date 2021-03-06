# MAP-E(v6プラス) CE情報の計算スクリプト

## How to use

```sh
# python >= 3.9

python v6plus.py "<自動で付与されたv6アドレス>/64"

```


```
# 実行例
python v6plus.py "240B:10:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/64"

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

