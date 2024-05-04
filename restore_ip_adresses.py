from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        list_ips: List[str] = []

        def solve(remain_s: str, list_ip: List[str]) -> None:
            if len(list_ip) == 3:
                if (remain_s[0] == '0' and len(remain_s) > 1) or len(remain_s) > 3 or \
                        (len(remain_s) == 3 and remain_s > '255'):
                    return
                list_ips.append('.'.join(list_ip + [remain_s]))
                return
            for i in range(1, len(remain_s)):
                part_ip: str = remain_s[:i]
                if (part_ip[0] != '0' or len(part_ip) == 1) and (len(part_ip) < 3 or \
                        (len(part_ip) == 3 and part_ip <= '255')):
                    list_ip.append(part_ip)
                    solve(remain_s[i:], list_ip)
                    list_ip.pop()
                elif len(part_ip) > 3 or part_ip > '255':
                    break

        solve(s, [])
        return list_ips


solution: Solution = Solution()
s: str = "25525511135"
assert solution.restoreIpAddresses(s) == ["255.255.11.135", "255.255.111.35"]
s: str = "0000"
assert solution.restoreIpAddresses(s) == ["0.0.0.0"]
s: str = "101023"
assert solution.restoreIpAddresses(s) == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
