import unittest

from ipaddress import IPv4Address
from ethjsonrpc import EthJsonRpc


class Ipv4TestCase(unittest.TestCase):

    def setUp(self):
        with open('compiled.evm') as f:
            compiled = f.read().rstrip()
        self.c = EthJsonRpc()
        self.c._call('evm_reset')
        self.cb = self.c.eth_coinbase()
        self.contract_addr = self.AddressToIPv4(self.cb, compiled)

    def tearDown(self):
        pass

################################################################################

    def test_read(self):
        result = self.get_ip(self.contract_addr, self.cb[2:])
        unchained_ip = self.ip_from_chain(result)
        self.assertEqual('0.0.0.0', unchained_ip)

    def test_set_read(self):
        ip = u'192.168.1.1'
        chained_ip = self.ip_to_chain(ip)
        self.set_ip(self.cb, self.contract_addr, chained_ip)

        result = self.get_ip(self.contract_addr, self.cb[2:])
        unchained_ip = self.ip_from_chain(result)
        self.assertEqual(ip, unchained_ip)

    def test_set_delete_read(self):
        ip = u'192.168.1.1'
        chained_ip = self.ip_to_chain(ip)
        self.set_ip(self.cb, self.contract_addr, chained_ip)

        self.delete_ip(self.cb, self.contract_addr)

        result = self.get_ip(self.contract_addr, self.cb[2:])
        unchained_ip = self.ip_from_chain(result)
        self.assertEqual('0.0.0.0', unchained_ip)


################################################################################

    def ip_to_chain(self, ip):
        return int(IPv4Address(ip))

    def ip_from_chain(self, ip):
        return str(IPv4Address(ip))

################################################################################

    def AddressToIPv4(self, sender, compiled):
        '''
        constructor
        '''
        sig = 'AddressToIPv4()'
        args = []
        tx = self.c.create_contract(sender, compiled, sig, args)
        return self.c.get_contract_address(tx)

    def set_ip(self, sender, contract_addr, ip):
        sig = 'set_ip(uint32)'
        args = [ip]
        self.c.call_with_transaction(sender, contract_addr, sig, args)

    def delete_ip(self, sender, contract_addr):
        sig = 'delete_ip()'
        args = []
        self.c.call_with_transaction(sender, contract_addr, sig, args)

    def get_ip(self, contract_addr, addr):
        sig = 'get_ip(address)'
        args = [addr]
        result_types = ['uint32']
        return self.c.call(contract_addr, sig, args, result_types)[0]


if __name__ == '__main__':
    unittest.main()
