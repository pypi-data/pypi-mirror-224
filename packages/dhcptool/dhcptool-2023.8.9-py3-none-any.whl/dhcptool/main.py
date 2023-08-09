# -*- coding: utf-8 -*-
# @Time    : 2022/10/23 16:33
# @Author  : mf.liang
# @File    : main.py
# @Software: PyCharm
# @desc    : dhcp 命令行接受，本工具为循环发包，未考虑实现并发
import argparse

from dhcptool.dhcp4_controller import Dhcp4Controller
from dhcptool.dhcp6_controller import Dhcp6Controller
from dhcptool.env_args import logs, global_var
from dhcptool.extend_tools_controller import ExtendToolsController
from dhcptool.tools import Tools


def parse_cmd_args_common(subparsers):
    """
    DHCPv4和DHCPv6公共解析参数
    :param subparsers: 
    :return: 
    """
    # DHCP分配
    subparsers.add_argument("--ip_src", "-src", help='dhcptool [v4|v6] -s [ipv4|ipv6] -src [ipv4|ipv6]')
    subparsers.add_argument("--dhcp_server", "-s", help="dhcptool [v4|v6] -s [ipv4|ipv6]")
    subparsers.add_argument("--relay_forward", "-rf", type=str,
                            default=Tools.get_local_ipv4() if "v4" in subparsers.prog else Tools.get_local_ipv6(),
                            help='dhcptool [v4|v6] -f [ipv4|ipv6] -rf [ipv4|ipv6]')
    subparsers.add_argument("--iface", "-i", help='dhcptool [v4|v6] -s [ipv4|ipv6] -i eth0')
    subparsers.add_argument("--single", "-single", action='store_true',
                            help='dhcptool [v4|v6] -s [ipv4|ipv6] -mt inform -single -o 50=[ipv4]')
    subparsers.add_argument("--renew", "-renew", action='store_true', help='dhcptool [v4|v6] -f [ipv4|ipv6] -renew')
    subparsers.add_argument("--release", "-release", action='store_true', help='发起release请求')
    subparsers.add_argument("--decline", "-decline", action='store_true', help='发起decline请求')
    subparsers.add_argument("--filter", "-f", default=None, help='使用广播发包,用来过滤监听的返回结果')
    subparsers.add_argument("--mac", "-mac", default=None, help='指定用户mac')
    subparsers.add_argument("--debug", "-debug", action='store_true', help='debug模式，能查看更详细的报文内容')
    subparsers.add_argument("--num", "-n", type=int, default=1, help="发送报文数量")
    subparsers.add_argument("--fixe", "-fixe", action='store_true', help="固定mac值进行发包")
    subparsers.add_argument("--sleep_time", "-st", type=int, default=0, help='发包过程中等待时间')
    subparsers.add_argument("--options", "-o", default=None,
                            help='dhcptool [v4|v6] -f [ipv4|ipv6] -o [code]=[value]&[code]=[value] [dhcptool v4 -s 192.168.31.134 -o [16=1f3……&14=''][18="eth 2/1/4:114.14 ZTEOLT001/1/1/5/0/1/000000000000001111111154 XE"][60=60:000023493534453……][6=12,7][50=192.168.31.199]')


def parse_cmd_args_dhcp4():
    """
    # 解析dhcp4参数
    :return:
    """
    parse_cmd_args_common(subparsers_4)
    subparsers_4.add_argument("--discover", "-discover", action='store_true', help='发起discover请求')
    subparsers_4.add_argument("--request", "-request", action='store_true', help='发起request请求')
    subparsers_4.add_argument("--inform", "-inform", action='store_true', help='发起inform请求')
    subparsers_4.add_argument("--nak", "-nak", action='store_true', help='模拟异常报文以返回nak响应报文')


def parse_cmd_args_dhcp6():
    """
    解析dhcp6参数
    :return:
    """
    parse_cmd_args_common(subparsers_6)
    subparsers_6.add_argument("--na", "-na", action='store_true', help='dhcptool v6 -f ipv6 -na')
    subparsers_6.add_argument("--pd", "-pd", action='store_true', help='dhcptool v6 -f ipv6 -pd')
    subparsers_6.add_argument("--solicit", "-solicit", action='store_true', help='发起solicit请求')


def parse_cmd_args_tools():
    """
    解析tools参数
    :return:
    """
    parse_cmd_args_common(subparsers_tools)
    subparsers_tools.add_argument("--generate_mac", "-gm", choices=["random", "asc", "desc"], help='dhcptool tools -gm ["random", "asc", "desc"]')
    subparsers_tools.add_argument("--na", "-na", help='dhcptool [v4|v6] -na [ipv4/ipv6]/24')
    subparsers_tools.add_argument("--pd", "-pd", type=int, help='dhcptool [v4|v6] -pd 64')


def exec_dhcp4(args):
    """
    DHCPv4发包
    :param args:
    :return:
    """
    dhcp4_controller = Dhcp4Controller(args)
    dhcp4_controller.run()


def exec_dhcp6(args):
    """
    DHCPv6发包
    :param args:
    :return:
    """

    dhcp6_controller = Dhcp6Controller(args)
    dhcp6_controller.run()


def exec_tools(args):
    """
    执行 tools中的功能
    :param args:
    :return:
    """
    extend_tool_controller = ExtendToolsController(args)
    if args.na:
        extend_tool_controller.calculate_address_range()
    else:
        extend_tool_controller.generate_print_mac()


parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument("--version", "-v", help="查看dhcptool版本信息", action='version', version=Tools.get_version_desc())
subparsers = parser.add_subparsers(
    help='[s|f] [debug] [single] [renew|release|decline|inform|nak] [mac] [o] [n] [st] [np]')
subparsers_4 = subparsers.add_parser('v4', help="DHCPv6 发包帮助信息")
subparsers_4.set_defaults(func=exec_dhcp4)
subparsers_6 = subparsers.add_parser('v6', help='DHCPv6 发包帮助信息')
subparsers_6.set_defaults(func=exec_dhcp6)
subparsers_tools = subparsers.add_parser('tools', help='扩展工具')
subparsers_tools.set_defaults(func=exec_tools)
parse_cmd_args_dhcp4()
parse_cmd_args_dhcp6()
parse_cmd_args_tools()


def dhcp_main():
    """
    dhcp执行函数入口
    :return:  v6 -s 1000:0:0:31::11 -n 5
    """
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict:
        str_args_dict = str(args_dict).replace('{', '').replace('}', '').replace("'", '')
        if args.debug:
            logs.info(f"args: {str_args_dict}")
        global_var.update(args_dict)
        # 开启执行
        args.func(args)
    else:
        while True:
            argv_cmd = input('dhcptool:\t')
            argv_list = argv_cmd.split(' ')
            args = parser.parse_args(argv_list)
            # 开启执行
            args.func(args)


if __name__ == '__main__':
    dhcp_main()
