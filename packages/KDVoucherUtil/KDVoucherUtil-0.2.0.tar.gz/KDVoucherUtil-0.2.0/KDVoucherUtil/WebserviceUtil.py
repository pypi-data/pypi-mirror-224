"""
This workingpaper is used for ease the use of kingdee webservice, the webservice is not designed for python,
and is not very friendly for finance based developer.
"""

import re

from suds.client import Client
from suds.sax.element import Element

from . import *


def login(domain, sln_name, dc_name, language, db_type, auth_pattern, user_name, user_pwd) -> str:
    try:
        userName = user_name
        password = user_pwd
        client = Client(domain + '/ormrpc/services/EASLogin?wsdl')
        result = client.service.login(userName, password, sln_name, dc_name, language, db_type, auth_pattern)
        ssid = re.search('sessionId = "' + '(.*?)' + '"', str(result)).group(1)
        print('webservice login successfully， login as ' + userName)
        return ssid
    except Exception as e:
        print(e)
        raise LoginException(str(e))


def import_voucher(voucher_list: list, ssid: str, domain: str) -> dict:
    """
    WARNING: the rollback function of kingdae service seems to be unreliable, STRONGLY RECOMMEND to import one voucher at a time!!!
    :param voucher_list: standard voucher please refer to VoucherUtil - get_standard_voucher
    :param ssid:
    :return: kingdae returns a a list, which is in form of ["error code||voucher type||year||month||chs result||voucher number||result code"]
            the function result should be in form of :
            {
                'result': str,
                'type': str,
                'year': str,
                'month: str,
                'error_msg': str
                'voucher_number': str,
                'origin_result_str': str,
                'desc': str,
            }
    """
    try:
        client = Client(domain + '/ormrpc/services/WSGLWebServiceFacade?wsdl')
        client.set_options(timeout=300)
        ssn = Element('SessionId').setText(ssid).setPrefix(p='ns1', u='http://login.webservice.bos.kingdee.com')
        client.set_options(soapheaders=ssn)
        result = client.service.importVoucher(voucher_list, 1, 0, 0)
        parse_result = result[0].split('||')
        return {
            'result': parse_result[0],
            'type': parse_result[1],
            'year': parse_result[2],
            'month': parse_result[3],
            'invoke_msg': parse_result[4],
            'voucher_number': parse_result[5],
            'origin_result_str': result[0],
        }
    except Exception as e:
        return {
            'result': '-2',
            'type': None,
            'year': None,
            'month': None,
            'invoke_msg': None,
            'voucher_number': None,
            'origin_result_str': str(e),
        }


def delete_voucher(entity_code: str, period: str, voucher_number: str, desc: str, ssid: str, domain: str) -> int:
    try:
        client = Client(domain + '/ormrpc/services/WSGLWebServiceFacade?wsdl')
        client.set_options(timeout=300)
        ssn = Element('SessionId').setText(ssid).setPrefix(p='ns1', u='http://login.webservice.bos.kingdee.com')
        client.set_options(soapheaders=ssn)
        result = client.service.deleteVoucher(entity_code, period, voucher_number, desc)
    except Exception as e:
        result = -1
        print(e)
    return int(result)


def get_account_balance(entity_code: str, str_year: str, str_month: str, ssid: str, domain: str) -> list:
    """
    the kingdea server will only return up to 1000 records once at a time,
    this function will automatically loop and get every balance of certain period
    :param entity_code:
    :param str_year:
    :param str_month:
    :param ssid:
    :return:
    """
    result = []
    try:
        client = Client(domain + '/ormrpc/services/WSGLWebServiceFacade?wsdl')
        client.set_options(timeout=300)
        ssn = Element('SessionId').setText(ssid).setPrefix(p='ns1', u='http://login.webservice.bos.kingdee.com')
        client.set_options(soapheaders=ssn)
        len_of_tb = 1001
        loop = 0
        while len_of_tb == 1001:
            curr_result = client.service.getAccountBalance(entity_code, str(str_year), str(str_month),
                                                           loop * len_of_tb, loop * len_of_tb + len_of_tb)
            result += curr_result if curr_result is not None else []
            len_of_tb = len(curr_result) if curr_result is not None else 0
            loop += 1
        print('Invoke getAccountBalance interface successfully, param: entity_code' + entity_code + '; period: '
              + str(str_year) + '-' + str(str_month) + '; data length: ' + str(len(result) if result else 0))
    except ConnectionResetError:
        result = get_account_balance(entity_code, str_year, str_month, ssid, domain)
    except Exception as e:
        result = [e]
        print('Unexpected error occurred in invoking getAccountBalance interface, param: ' + entity_code + '; period: '
              + str(str_year) + '-' + str(str_month))
        print(e)
    finally:
        return result


def get_assit_balance(entity_code: str, account_number: str, str_year: str, str_month: str, ssid: str, domain: str) -> list:
    """
    the kingdea server will only return up to 1000 records once at a time,
    this function did not consider the case which asst balance longer than 1k
    todo: update the loop function
    :param entity_code:
    :param account_number:
    :param str_year:
    :param str_month:
    :param ssid:
    :return:
    """
    result = []
    try:
        client = Client(domain + '/ormrpc/services/WSGLWebServiceFacade?wsdl')
        client.set_options(timeout=300)
        ssn = Element('SessionId').setText(ssid).setPrefix(p='ns1', u='http://login.webservice.bos.kingdee.com')
        client.set_options(soapheaders=ssn)
        # no loop designed, assit ledger is not supposed to be longer than 1k
        result = client.service.getAssitBalance(entity_code, account_number, str(str_year), str(str_month), 0, 0)
        print('Invoke getAsstBalance interface successfully, param: entity_code:' + entity_code +
              ';account_code:' + str(account_number) + '; period: '
              + str(str_year) + '-' + str(str_month) + '; data length: ' + str(len(result) if result else 0))
    except ConnectionResetError:
        result = get_assit_balance(entity_code, account_number, str_year, str_month, ssid, domain)
    except Exception as e:
        result = [e]
        print('Unexpected error occurred in invoking getAsstBalance interface, param: ' + entity_code +
              ';account_code: ' + str(account_number) + '; period: '
              + str(str_year) + '-' + str(str_month))
        print(e)
    finally:
        return result

