# -*- coding: utf-8 -*-
# @Time    : 2022/10/23 19:06
# @Author  : mf.liang
# @File    : dhcp4_controller.py
# @Software: PyCharm
# @desc    :
from queue import Empty
from scapy.layers.dhcp import DHCPTypes
from dhcptool.dhcp_pkt import Dhcp4Pkt
from dhcptool.env_args import summary_result, logs, pkt_result, global_var
from dhcptool.tools import Tools


class Dhcp4Controller(Dhcp4Pkt):

    def __init__(self, args):
        super(Dhcp4Controller, self).__init__(args)
        self.args = args

    def run(self):
        """
        执行 发包测试入口
        :return:
        """
        for i in DHCPTypes.values():

            summary_result[i.upper()] = 0
        for i in range(int(self.args.num)):
            global_var['tag'] = i
            try:
                send_pkts = {
                    self.args.renew: self.send_request if self.args.single else self.send_discover_offer_request_ack_renew,
                    self.args.release: self.send_release if self.args.single else self.send_discover_offer_request_ack_release,
                    self.args.inform: self.send_inform if self.args.single else self.send_discover_offer_request_ack_inform,
                    self.args.request: self.send_request if self.args.single else None,
                    self.args.discover: self.send_discover,
                    self.args.nak: self.send_discover_offer_request_nak,
                    self.args.decline: self.send_decline if self.args.single else self.send_discover_offer_request_ack_decline,
                }
                send_pkts.get(True, self.send_discover_offer_request_ack)()
            except Empty as ex:
                logs.info('没有接收到返回包！')
            except AssertionError as ex:
                logs.info('返回包未包含分配ip！')
            except Exception as ex:
                logs.info(f"warn: {ex}")
            print('-' * 60)
            pkt_result.get('dhcp4_ack').queue.clear()
        str_summary_result = str(summary_result).replace('{', '').replace('}', '').replace("'", '')
        logs.info(str_summary_result)

    def send_discover_offer_request_ack(self):
        """
        发送  dhcp4 完整分配流程
        :return:
        """
        self.__init__(self.args)
        discover_pkt = self.dhcp4_discover()
        res = self.send_dhcp4_pkt(discover_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)
        request_pkt = self.dhcp4_request()
        ack_pkt = self.send_dhcp4_pkt(request_pkt)
        Tools.analysis_results(pkts_list=ack_pkt, args=self.args)

    def send_discover_offer_request_nak(self):
        """
        发送  dhcp4 完整分配流程
        :return:
        """
        self.__init__(self.args)
        discover_pkt = self.dhcp4_discover()
        res = self.send_dhcp4_pkt(discover_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)
        request_pkt = self.dhcp4_exception_request()
        ack_pkt = self.send_dhcp4_pkt(request_pkt)
        Tools.analysis_results(pkts_list=ack_pkt, args=self.args)

    def send_discover_offer_request_ack_renew(self):
        """
        发起 更新租约 请求
        :return:
        """
        self.__init__(self.args)
        discover_pkt = self.dhcp4_discover()
        res = self.send_dhcp4_pkt(discover_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)
        request_pkt = self.dhcp4_request()
        ack_pkt = self.send_dhcp4_pkt(request_pkt)
        Tools.analysis_results(pkts_list=ack_pkt, args=self.args)
        Tools.rate_print('租约更新', self.args.sleep_time)
        ack_pkt = self.send_dhcp4_pkt(request_pkt)
        Tools.analysis_results(pkts_list=ack_pkt, args=self.args)

    def send_discover_offer_request_ack_decline(self):
        """
        发起 冲突租约 请求
        :return:
        """
        self.send_discover_offer_request_ack()
        decline_pkt = self.dhcp4_decline()
        Tools.rate_print('模拟冲突', self.args.sleep_time)
        self.send_dhcp4_pkt(decline_pkt)

    def send_discover_offer_request_ack_release(self):
        """
        发起 释放租约 请求
        :return:
        """
        self.send_discover_offer_request_ack()
        release_pkt = self.dhcp4_release()
        Tools.rate_print('租约释放', self.args.sleep_time)
        self.send_dhcp4_pkt(release_pkt)

    def send_discover_offer_request_ack_inform(self):
        """
        发起 inform 请求
        :return:
        """
        self.send_discover_offer_request_ack()
        inform_pkt = self.dhcp4_inform()
        ack_pkt = self.send_dhcp4_pkt(inform_pkt)
        Tools.analysis_results(pkts_list=ack_pkt, args=self.args)

    def send_discover(self):
        """
        单独的discover包
        :return:
        """
        discover_pkt = self.dhcp4_discover()
        res = self.send_dhcp4_pkt(discover_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_request(self):
        """
        单独的request包
        :return:
        """
        request_pkt = self.dhcp4_request()
        res = self.send_dhcp4_pkt(request_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_inform(self):
        """
        单独的inform包
        :return:
        """
        inform_pkt = self.dhcp4_inform()
        res = self.send_dhcp4_pkt(inform_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_decline(self):
        """
        单独的decline包
        :return:
        """
        decline_pkt = self.dhcp4_decline()
        res = self.send_dhcp4_pkt(decline_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)

    def send_release(self):
        """
        单独的release包
        :return:
        """
        release_pkt = self.dhcp4_release()
        res = self.send_dhcp4_pkt(release_pkt)
        Tools.analysis_results(pkts_list=res, args=self.args)
