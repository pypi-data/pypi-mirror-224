# -*- coding: utf-8 -*-
# @Time    : 2022/10/23 19:33
# @Author  : mf.liang
# @File    : options.py
# @Software: PyCharm
# @desc    :
import binascii
from typing import Text

from scapy.layers.dhcp6 import DHCP6OptVendorClass, VENDOR_CLASS_DATA, DHCP6OptIfaceId, DHCP6OptStatusCode, DHCP6OptRapidCommit, DHCP6OptOptReq, \
    DHCP6OptIAAddress, DHCP6OptIAPrefix, DHCP6OptClientFQDN
from dhcptool.env_args import logs


class Options:
    def __init__(self, args):
        self.args = args

    def parse_dhcp4_options(self):
        options_list = self.args.options
        if options_list == None:
            return None
        else:
            options_list = [i.split('=') for i in options_list.split('&')]
            return options_list

    def parse_dhcp6_options(self):
        options_list = self.args.options
        if options_list is None:
            return None
        else:
            options_list = [i.split('=') for i in options_list.split('&')]
            return options_list


class Dhcp4Options(Options):

    def __init__(self, args):
        self.args = args
        super(Dhcp4Options, self).__init__(args=self.args)

    def make_options_list(self) -> list:
        """
        制作 options
        :return:
        """
        options,op_82_sub_key = [], 0
        options_list = self.parse_dhcp4_options()
        if options_list is not None:
            for index, i in enumerate(options_list):
                if int(i[0]) == 12:
                    options.append(self.option_12(hostname=i[1]))
                if int(i[0]) == 7:
                    options.append(self.option_7(log_server=i[1]))
                if int(i[0]) == 60:
                    options.append(self.option_60(vendor_class_id=i[1]))
                if int(i[0]) == 82:
                    op_82_sub_key +=1
                    options.append(self.option_82(i[1], str(op_82_sub_key).rjust(2, '0')))
                if int(i[0]) == 55:
                    options.append(self.option_55(param_req_list=i[1]))
                if int(i[0]) == 50:
                    options.append(self.option_50(requested_addr=i[1]))
                if int(i[0]) == 51:
                    options.append(self.option_51(lease_time=i[1]))
                if int(i[0]) == 2:
                    options.append(self.option_2(time_zone=i[1]))
                if int(i[0]) == 3:
                    options.append(self.option_3(router=i[1]))
                if int(i[0]) == 13:
                    options.append(self.option_13(boot_size=i[1]))
                if int(i[0]) == 15:
                    options.append(self.option_15(domain=i[1]))
                if int(i[0]) == 19:
                    options.append(self.option_19(ip_forwarding=i[1]))
                if int(i[0]) == 23:
                    options.append(self.option_23(default_ip_ttl=i[1]))
        options.append('end')
        return options

    @staticmethod
    def option_12(hostname=''):
        return 'hostname', hostname

    @staticmethod
    def option_7(log_server='0.0.0.0'):
        return 'log_server', log_server

    @staticmethod
    def option_60(vendor_class_id=''):
        """
        拼接option60的函数
        :param vendor_class_id:
        :return:
        ./dhcptool v4 -s 192.168.31.134 -o 60=$(radtools passwd mf@liang admin123)
        """
        try:
            hex = vendor_class_id.encode("utf-8")
            vendor_class_id = binascii.unhexlify(hex)
            return 'vendor_class_id', vendor_class_id
        except:
            return 'vendor_class_id', vendor_class_id

    @staticmethod
    def option_82(value='', suboption_index='01'):
        """
        TODO: option82 和别的option同时使用时，sub_option存在顺序错乱的问题
        ./dhcptool v4 -s 192.168.31.116 -o "60=$(radtools passwd user1@itv.com test123)&82=eth 2/1/4:114.12 ZTEOLT001/1/1/5/0/1/000000000000001111111152 XE&12=yamu.com&7=2.2.2.2"
        :param value:
        :param suboption_index:
        :return:
        """
        try:
            hex_value = value.encode("utf-8")
            value = binascii.unhexlify(hex_value)
        except:
            value_len = hex(len(value))[2:]
            hex_value = value.encode("utf-8").hex()
            value = str(suboption_index) + str(value_len) + hex_value
            hex_value = value.encode("utf-8")
            value = binascii.unhexlify(hex_value)
        return 'relay_agent_information', value

    @staticmethod
    def option_55(param_req_list=''):
        param_req_list = [int(i) for i in param_req_list.split(',')]
        return 'param_req_list', param_req_list

    @staticmethod
    def option_50(requested_addr='192.168.0.1'):
        return 'requested_addr', requested_addr

    @staticmethod
    def option_51(lease_time: int=43200) -> tuple:
        """

        :param lease_time: 租约时间
        :return:
        """
        return 'lease_time', int(lease_time)

    @staticmethod
    def option_2(time_zone:int = 500):
        """
        :param times_zone: 时区
        :return:
        """
        return 'time_zone', int(time_zone)

    @staticmethod
    def option_3(router='0.0.0.0'):
        """

        :param router: 路由
        :return:
        """
        return 'router', router

    @staticmethod
    def option_13(boot_size=1000):
        """

        :param boot_size:
        :return:
        """
        return 'boot-size', int(boot_size)

    @staticmethod
    def option_15(domain: Text):
        """

        :param domain: 域名
        :return:
        """
        return 'domain', domain

    @staticmethod
    def option_19(ip_forwarding: bool):
        """

        :param ip_forwarding: ip转发
        :return:
        """
        return 'ip_forwarding', bool(ip_forwarding)

    @staticmethod
    def option_23(default_ttl: int):
        """

        :param default_ip_ttl: 默认ip ttl值
        :return:
        """
        return 'default_ttl', default_ttl


class Dhcp6Options(Options):

    def __init__(self, args):
        self.args = args
        super(Dhcp6Options, self).__init__(args=self.args)

    def make_options_list(self):
        """
        制作 options
        :return:
        """
        options = DHCP6OptStatusCode()
        options_list = self.parse_dhcp6_options()
        if options_list is not None:
            for i in options_list:
                if int(i[0]) == 16:
                    options = self.option_16(i[1]) / options
                if int(i[0]) == 18:
                    if self.args.dhcp_server:
                        options = self.option_18(i[1]) / options
                if int(i[0]) == 6:
                    options = self.option_6(i[1]) / options
                if int(i[0]) == 14:
                    options = self.option_14() / options
                # if int(i[0]) == 5:
                #     options = self.option_5(addr=i[1]) / options
                # if int(i[0]) == 26:
                #     options = self.option_26(prefix=i[1]) / options
        return options

    @staticmethod
    def option_16(account_pwd_hex: str):
        """
        python3 dhcptool.py v6 -s 1000::31:332b:d5ab:4457:fb60 -debug on -o "16=1f31014d65822107fcfd52000000006358c1cc2f31c57f7dd8b43d27edc570aba8e999ed46b5176fb38bb7a407d97010eeebba"
        :return:
        """
        try:
            if "0000" in account_pwd_hex[:5]:
                account_pwd_hex = account_pwd_hex[4:]
            vendor_class_data = VENDOR_CLASS_DATA(data=bytes.fromhex(account_pwd_hex))
            option16_pkt = DHCP6OptVendorClass(vcdata=vendor_class_data)
        except Exception as ex:
            logs.error(ex)
            return None
        return option16_pkt

    @staticmethod
    def option_18(ipoe_value: str):
        """
        suxx@suxx:      eth 2/1/4:80.90 ZTEOLT001/1/1/5/0/1/
        python3 dhcptool.py v6 -s 1000::31:332b:d5ab:4457:fb60 -o "16=1f31014d65822107fcfd52000000006358c1cc2f31c57f7dd8b43d27edc570aba8e999ed46b5176fb38bb7a407d97010eeebba&18=eth 2/1/4:80.90 ZTEOLT001/1/1/5/0/1"
        :return:
        """
        option18_pkt = DHCP6OptIfaceId(ifaceid=ipoe_value)
        return option18_pkt

    @staticmethod
    def option_6(value):
        """
        Option Request
        :return:
        """
        if value:
            value_list = [int(i) for i in value.split(',')]
            option6_pkt = DHCP6OptOptReq(reqopts=value_list)
        else:
            option6_pkt = DHCP6OptOptReq()
        return option6_pkt

    @staticmethod
    def option_14():
        """
        Rapid Commit
        :return:
        """
        option14_pkt = DHCP6OptRapidCommit()
        return option14_pkt

    @staticmethod
    def sub_option_5(addr):
        """
        DHCP6OptIAAddress   二级option,不能与 一级进行 option拼接
        :return:
        """
        option5_pkt = DHCP6OptIAAddress(addr=addr)
        return option5_pkt

    @staticmethod
    def sub_option_26(prefix):
        """
        DHCP6OptIAPrefix  二级option,不能与 一级进行 option拼接
        :return:
        """
        prefix, prefix_len = prefix.split('/')[0], prefix.split('/')[1]
        option26_pkt = DHCP6OptIAPrefix(prefix=prefix, plen=int(prefix_len))
        return option26_pkt
    

    @staticmethod
    def option_39():
        """
        DHCP6OptClientFQDN
        :return:
        """
        option39_pkt = DHCP6OptClientFQDN(flags=0, fqdn="")
        return option39_pkt