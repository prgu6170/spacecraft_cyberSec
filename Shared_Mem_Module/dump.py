import subprocess as sub
import math


class TcpDump():
    def get_dump(self):
        p = sub.Popen(('sudo', 'tcpdump', '-AlX','-q','-i', 'enx3c18a09c230e', 'udp', 'port', '4444', '--direction', 'in'), stdout=sub.PIPE)
        i = 0
        for row in iter(p.stdout.readline, b''):
            if i == 2:
                str1 = row.rstrip()[40:49].replace(' ', '')
            if i == 3:
                str2 = row.rstrip()[10:49].replace(' ', '')
                hex_str = "".join([str1, str2])
                print self.convert_hex_to_bin(hex_str)
            if 'IP' in row.strip():
                i = 0
            i += 1

    def convert_hex_to_bin(self, hex_str):
        """
        input: hex_num -> str
        output: binary -> str
        """
        string = []
        for i in range(0, len(hex_str), 2):
            string.append(''.join([hex_str[i], hex_str[i+1]]).decode("hex"))
        try:
            res = "{0:020b}".format(int(''.join(string), 2))
            return str(res)
        except ValueError:
            return None


if __name__ == '__main__':
    tcpdump = TcpDump()
    tcpdump.get_dump()