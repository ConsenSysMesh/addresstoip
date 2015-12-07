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
