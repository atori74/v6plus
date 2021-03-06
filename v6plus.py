import argparse
from ipaddress import (
        ip_address,
        ip_network,
        ip_interface
        )


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('ipv6_addr', help='given ipv6 address with CIDR.')
    args = parser.parse_args()

    return args

def v4map(prefix6):
    return {
            '240b:10::': '106.72.0.0',
            '240b:11::': '106.73.0.0',
            '240b:12::': '14.8.0.0',
            '240b:250::': '14.10.0.0',
            '240b:251::': '14.11.0.0',
            '240b:252::': '14.12.0.0',
            '240b:253::': '14.13.0.0',
            }[prefix6]

def port_list(psid):
    if int(psid[0], 16) > 15 or int(psid[1], 16) > 15:
        return
    
    ports = []
    for i in range(1,16):
        _from = int(f'{i:x}{psid}0', 16)
        _to = int(f'{i:x}{psid}F', 16)
        ports.append(f'{_from}-{_to}')

    return ports

def portset_ID(addr6):
    ip6 = ip_interface(addr6)
    seg4 = ip6.ip.exploded.split(':')[3]

    return seg4[:2]

def CE_ipv6(addr6):
    # ce_ip6 = prefix6:xy:x00:v:wx:y00:z00
    prefix6 = ip_interface(addr6).network
    ip4 = CE_ipv4(addr6)
    v, w, x, y = [int(seg) for seg in ip4.split('.')]
    z = int(portset_ID(addr6), 16)

    ip6 = ip_address(
        int(
            f'{prefix6.network_address:b}'[:32] +
            f'{x:08b}{y:08b}{z:08b}{0:08b}{v:016b}{w:08b}{x:08b}{y:08b}{0:08b}{z:08b}{0:08b}',
            2
            )
        )

    return str(ip6)

def CE_ipv4(addr6):
    ip6 = ip_interface(addr6)
    # get v6 prefix
    prefix6 = ip6.network
    # get v4prefix
    prefix4 = ip_network(v4map(str(prefix6.supernet(new_prefix=32).network_address)) + '/16')
    # v6の第三セグからv4の3,4セグを取得
    ip6_seg3 = ip6.ip.exploded.split(':')[2]
    ip4_seg3 = int(ip6_seg3[:2], 16)
    ip4_seg4 = int(ip6_seg3[2:], 16)
    # v4prefixと3,4セグを合わせる
    ip4 = ip_address(int(f'{prefix4.network_address:b}'[:16] + f'{ip4_seg3:08b}{ip4_seg4:08b}', 2))

    return str(ip4)


if __name__ == '__main__':
    args = get_args()
    prefix6 = args.ipv6_addr
    
    ip4 = CE_ipv4(prefix6)
    ip6 = CE_ipv6(prefix6)
    psid = portset_ID(prefix6)
    ports = port_list(psid)

    print(f'CE IPv4: {ip4}')
    print(f'CE IPv6: {ip6}')
    print(f'PSID: {psid}')
    print('Available ports below:')
    for p in ports:
        print(f'  {p}')


