from netaddr import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input")
parser.add_argument("-o", "--output")

args = parser.parse_args()
cidr_file = args.input
ips_file = args.output

filename = cidr_file
output = open(ips_file, "w")

with open(filename) as file:
    for cidr in file:
        ip = IPNetwork(cidr)
        for addr in ip:
            output.write(str(addr) + '\n')

output.close()
