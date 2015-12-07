## About
The AddressToIP contracts are a pair of Ethereum contracts that map Ethereum addresses to IP addresses. The transaction sender can set and delete his, and only his, IP address entry. The data is public, so that anyone can obtain an IP for an Ethereum address (assuming the mapping exists).

The IPv4 contract is at address 0x018f8d3c03c09298c358af2c9119ba5c0d5423fe .

The IPv6 contract is at address 0x7c26014679a5888f4bb24517789e79bdb03b4ccd .

## Features
* IPv4 and IPv6 support
* immortal (no one can delete the contract)
* written in Solidity

## API and gas estimate
### AddressToIPv4
``get_ip(address addr) returns (uint32)`` (no gas)
- Gets an IP address for an Ethereum address.  If the entry does not exist, returns 0.

``set_ip(uint32 ip)`` (20,318 gas)
- Sets the sender's IP address to ``ip``

``delete_ip()`` (20,295 gas)
- Deletes the sender's IP address

### AddressToIPv6
``get_ip(address addr) returns (uint128)`` (no gas)
- Gets an IP address for an Ethereum address.  If the entry does not exist, returns 0.

``set_ip(uint128 ip)`` (20,362 gas)
- Sets the sender's IP address to ``ip``

``delete_ip()`` (20,273 gas)
- Deletes the sender's IP address

## Source Code

```
contract AddressToIPv4 {

    mapping (address => uint32) ips;

    function AddressToIPv4() {
    }

    function set_ip(uint32 ip) {
        ips[msg.sender] = ip;
    }

    function delete_ip() {
        delete ips[msg.sender];
    }

    function get_ip(address addr) returns (uint32) {
        return ips[addr];
    }
}
```

```
contract AddressToIPv6 {

    mapping (address => uint128) ips;

    function AddressToIPv6() {
    }

    function set_ip(uint128 ip) {
        ips[msg.sender] = ip;
    }

    function delete_ip() {
        delete ips[msg.sender];
    }

    function get_ip(address addr) returns (uint128) {
        return ips[addr];
    }
}
```

## Compiler Version
0.1.6-0/Release-Linux/g++/int linked to libethereum-0.9.93-0/Release-Linux/g++/int
