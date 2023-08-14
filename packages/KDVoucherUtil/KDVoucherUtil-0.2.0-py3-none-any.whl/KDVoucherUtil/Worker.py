from WebserviceUtil import *
from VoucherUtil import *
from . import *


class KDUser:
    def __init__(self, user, pwd, domain, sln_name, dc_name, language, db_type, auth_pattern):
        self.ssid = login(domain, sln_name, dc_name, language, db_type, auth_pattern, user, pwd)
        self.domain = domain

    def get_account_balance(self, entity_code, str_year, str_month) -> list:
        return get_account_balance(entity_code, str_year, str_month, self.ssid, self.domain)

    def get_assit_balance(self, entity_code, account_code, str_year, str_month) -> list:
        return get_assit_balance(entity_code, account_code, str_year, str_month, self.ssid, self.domain)

    def import_raw_voucher(self, voucher_list):
        """
        DO NOT RECOMMEND
        :param voucher_list:
        :return:
        """
        return import_voucher(voucher_list, self.ssid, self.domain)

    def import_voucher(self, voucher_list, renumber=False) -> list:
        """
        this function will separate the voucher list and try to import once at a time.
        :param voucher_list:
        :param renumber:
        :return:
        """
        voucher_dict = separate_voucher_list(voucher_list, renumber=renumber)
        result_list = []
        for voucher in voucher_dict:
            result_list.append(self.import_raw_voucher(voucher_dict[voucher]))
        return result_list

    def delete_voucher(self, entity_code, period, voucher_number, desc):
        return delete_voucher(entity_code, period, voucher_number, desc, self.ssid, self.domain)