'''
https://leetcode.com/problems/validate-ip-address/
468. Validate IP Address
Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.



Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
Example 4:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
Output: "Neither"
Example 5:

Input: IP = "1e1.4.5.6"
Output: "Neither"


Constraints:

IP consists only of English letters, digits and the characters '.' and ':'.
'''


def check_ipv4(parts):
    for part in parts:
        if len(part) < 1 or len(part) > 3 or not part.isnumeric() or (len(part) > 1 and part[0] == '0'):
            return "Neither"

        if int(part) > 255:
            return "Neither"

    return "IPv4"


def check_ipv6(parts):
    for part in parts:
        if len(part) < 1 or len(part) > 4 or not part.isalnum():
            return "Neither"

        valid = "abcdefABCDED0123456789"

        for ch in part:
            ch_int = ord(ch)
            if ch not in valid:
                return "Neither"

    return "IPv6"


def validIPAddress(IP):
    parts = IP.split('.')

    if len(parts) == 4:
        return check_ipv4(parts)
    elif len(parts) == 1:
        parts = IP.split(':')
        if len(parts) == 8:
            return check_ipv6(parts)

    return "Neither"


if __name__ == "__main__":
    print(validIPAddress("172.16.254.1"))
    print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(validIPAddress("256.256.256.256"))    # Neither
    print(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))  # Neither
