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
