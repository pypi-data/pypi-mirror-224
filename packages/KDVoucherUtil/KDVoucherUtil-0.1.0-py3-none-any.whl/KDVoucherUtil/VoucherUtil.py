import re


class TBLine:
    def __init__(self, tb_line: list):
        self.balance_type = tb_line[0]
        self.entity_code = tb_line[1]
        self.entity_name = tb_line[2]
        self.month = tb_line[3]
        self.year = tb_line[4]
        self.account_code = tb_line[5]
        self.account_name = tb_line[6]
        self.currency_code = tb_line[7]
        self.currency_name = tb_line[8]
        self.begin_balance_ori_currency = tb_line[9]
        self.year_debit_ori_currency = tb_line[10]
        self.year_credit_ori_currency = tb_line[11]
        self.period_debit_ori_currency = tb_line[12]
        self.period_credit_ori_currency = tb_line[13]
        self.end_balance_ori_currency = tb_line[14]
        self.begin_balance_local_currency = tb_line[15]
        self.year_debit_local_currency = tb_line[16]
        self.year_credit_local_currency = tb_line[17]
        self.period_debit_local_currency = tb_line[18]
        self.period_credit_local_currency = tb_line[19]
        self.end_balance_local_currency = tb_line[20]
        self.begin_balance_report_currency = tb_line[21]
        self.year_debit_report_currency = tb_line[22]
        self.year_credit_report_currency = tb_line[23]
        self.period_debit_report_currency = tb_line[24]
        self.period_credit_report_currency = tb_line[25]
        self.end_balance_report_currency = tb_line[26]
        self.year_pl_ori_currency = tb_line[27]
        self.period_pl_ori_currency = tb_line[28]
        self.year_pl_local_currency = tb_line[29]
        self.period_pl_local_currency = tb_line[30]
        self.year_pl_report_currency = tb_line[31]
        self.period_pl_report_currency = tb_line[32]
        self.begin_qty = tb_line[33]
        self.year_debit_qty = tb_line[34]
        self.year_credit_qty = tb_line[35]
        self.period_debit_qty = tb_line[36]
        self.period_credit_qty = tb_line[37]
        self.end_qty = tb_line[38]
        self.asst_code = tb_line[39]
        self.asst_name = tb_line[40]
        self.has_asst = tb_line[41]
        self.has_asst_bool = True if tb_line[41] == '1' else False


class AsstTBLine:
    def __init__(self, tb_line: list):
        self.balance_type = tb_line[0]
        self.entity_code = tb_line[1]
        self.entity_name = tb_line[2]
        self.month = tb_line[3]
        self.year = tb_line[4]
        self.account_code = tb_line[5]
        self.account_name = tb_line[6]
        self.currency_code = tb_line[7]
        self.currency_name = tb_line[8]
        self.begin_balance_ori_currency = tb_line[9]
        self.year_debit_ori_currency = tb_line[10]
        self.year_credit_ori_currency = tb_line[11]
        self.period_debit_ori_currency = tb_line[12]
        self.period_credit_ori_currency = tb_line[13]
        self.end_balance_ori_currency = tb_line[14]
        self.begin_balance_local_currency = tb_line[15]
        self.year_debit_local_currency = tb_line[16]
        self.year_credit_local_currency = tb_line[17]
        self.period_debit_local_currency = tb_line[18]
        self.period_credit_local_currency = tb_line[19]
        self.end_balance_local_currency = tb_line[20]
        self.begin_balance_report_currency = tb_line[21]
        self.year_debit_report_currency = tb_line[22]
        self.year_credit_report_currency = tb_line[23]
        self.period_debit_report_currency = tb_line[24]
        self.period_credit_report_currency = tb_line[25]
        self.end_balance_report_currency = tb_line[26]
        self.year_pl_ori_currency = tb_line[27]
        self.period_pl_ori_currency = tb_line[28]
        self.year_pl_local_currency = tb_line[29]
        self.period_pl_local_currency = tb_line[30]
        self.year_pl_report_currency = tb_line[31]
        self.period_pl_report_currency = tb_line[32]
        self.begin_qty = tb_line[33]
        self.year_debit_qty = tb_line[34]
        self.year_credit_qty = tb_line[35]
        self.period_debit_qty = tb_line[36]
        self.period_credit_qty = tb_line[37]
        self.end_qty = tb_line[38]
        self.asst_code = tb_line[39]
        self.asst_name = tb_line[40]
        self.asst_full_desc = tb_line[41]
        self.asst_full_name = tb_line[42]
        self.asst_full_code = tb_line[43]
        # parse asst information
        asst_type_list = self.asst_full_code.split(';')
        self.asst_type1 = asst_type_list[0].split('_!')[1].split(':')[0]
        self.asst_code1 = asst_type_list[0].split('_!')[1].split(':')[1]
        try:
            self.asst_type2 = asst_type_list[1].split('_!')[1].split(':')[0]
            self.asst_code2 = asst_type_list[1].split('_!')[1].split(':')[1]
        except IndexError:
            self.asst_type2 = None
            self.asst_code2 = None

    def get_main_info_str(self):
        info = ' '.join(['balance_type', self.balance_type,
                         'currency_code', self.currency_code,
                         'account_code', self.account_code,
                         'asst_type', self.asst_type1,
                         'asst_code', self.asst_code1,
                         'year_end_balance', self.end_balance_local_currency])
        return info


class AsstTB:
    def __init__(self, tb: list):
        self.asst_list = []
        if tb:
            for each in tb:
                if not re.match('^\\d', str(each[0])):
                    continue
                self.asst_list.append(AsstTBLine(each))


class TB:
    def __init__(self, tb: list):
        """
        tested the size of one yearly tb, with all asst accounts info, the size was approximately 24.4M
        which should be considered acceptable
        :param tb: the original result from kd webservice
        """
        self.record_list = []
        self.asst_tb_dict = {}
        if tb:
            for line in tb:
                if not re.match('^\\d', str(line[0])):
                    continue
                self.record_list.append(TBLine(line))

    def is_leaf_account(self, account_code) -> bool:
        for each in self.record_list:
            if re.match(account_code + '.+', each.account_code):
                return False
        return True


def seperate_voucher_list(voucher_list: list, renumber=False) -> dict:
    """
    clean the voucher list
    :param voucher_list: use voucher number and company number as unique key to identify voucher,
     the key to result dictionary is 'voucherNumber_companyNumber'
    :param renumber: WARNING! if this args is True,
     the function will comb the list and renumber the sequence of entry, which may lead unknown error.
    :return: the dict of voucher list, the key should be the voucher number
    """
    seperated_voucher_dict = {}
    for voucher in voucher_list:
        voucher_key = '_'.join([str(voucher['voucherNumber']), str(voucher['companyNumber'])])
        if voucher_key not in seperated_voucher_dict:
            seperated_voucher_dict.setdefault(voucher_key, [])
        seperated_voucher_dict[voucher_key].append(voucher)
    if renumber:
        for voucher_key in seperated_voucher_dict:
            for new_entry_int, voucher in enumerate(seperated_voucher_dict[voucher_key]):
                voucher['entrySeq'] = new_entry_int + 1
    return seperated_voucher_dict


def _get_standard_voucher(assit=0):
    standard_voucher = {
        'companyNumber': '',
        'bookedDate': '',
        'bizDate': '',
        'periodYear': 0,
        'periodNumber': 0,
        'voucherType': '',
        'voucherNumber': '',
        'entrySeq': 0,
        'voucherAbstract': '',
        'accountNumber': '',
        'currencyNumber': '',
        'localRate': 1,
        'entryDC': 0,
        'originalAmount': 0.0,
        'debitAmount': 0.0,
        'creditAmount': 0.0,
        'creator': '',
    }
    if assit == 1:
        standard_voucher['asstActType1'] = ''
        standard_voucher['asstActNumber1'] = ''
    elif assit == 2:
        standard_voucher['asstActType1'] = ''
        standard_voucher['asstActNumber1'] = ''
        standard_voucher['asstActType2'] = ''
        standard_voucher['asstActNumber2'] = ''
    return standard_voucher
