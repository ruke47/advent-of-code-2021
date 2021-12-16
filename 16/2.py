import itertools

class Packet:
    def __init__(self, bitstream):
        self.version = consume_to_int(bitstream, 3)
        self.type = consume_to_int(bitstream, 3)

        print(f"Got packet version: {self.version} type: {self.type}")

        if self.type == 4:
            self.literal = get_literal(bitstream)
            self.children = None
        else:
            self.literal = None
            self.children = get_children(bitstream)
        print(f"Decoded: {self}")

    def value(self):
        if self.type == 0:
            return sum(self.child_values())
        if self.type == 1:
            product = 1
            for child in self.children:
                product *= child.value()
            return product
        if self.type == 2:
            return min(self.child_values())
        if self.type == 3:
            return max(self.child_values())
        if self.type == 4:
            return self.literal
        if self.type == 5:
            if self.children[0].value() > self.children[1].value():
                return 1
            else:
                return 0
        if self.type == 6:
            if self.children[0].value() < self.children[1].value():
                return 1
            else:
                return 0
        if self.type == 7:
            if self.children[0].value() == self.children[1].value():
                return 1
            else:
                return 0

    def child_values(self):
        return [child.value() for child in self.children]

    def __str__(self):
        return f'Version: {self.version} Type: {self.type} Literal: {self.literal} Children: {self.children}'

    def __repr__(self):
        return self.__str__()


def hex_to_bin(single_char) -> str:
    return bin(int(single_char, 16))[2:].zfill(4)


def consume(bitstream, byte_count) -> list[str]:
    arr = list(itertools.islice(bitstream, byte_count))
    if len(arr) != byte_count:
        print(f"Expected: {byte_count}, Got: {arr}")
        raise EOFError
    return arr


def list_to_int(bit_array) -> int:
    return int("".join(bit_array), 2)


def consume_to_int(bitstream, byte_count) -> int:
    bit_array = consume(bitstream, byte_count)
    return list_to_int(bit_array)


def get_literal(bitstream) -> int:
    bits = []
    while True:
        keep_going = consume_to_int(bitstream, 1)
        bits.extend(consume(bitstream, 4))
        print(f"Bits: {bits}")
        if keep_going == 0:
            break

    return list_to_int(bits)


def get_children(bitstream) -> list[Packet]:
    length_type = consume_to_int(bitstream, 1)
    if length_type == 0:
        subpacket_byte_count = consume_to_int(bitstream, 15)
        subpacket_bytes = consume(bitstream, subpacket_byte_count)
        subpacket_iter = iter(subpacket_bytes)
        return get_all_packets(subpacket_iter)
    else:
        child_count = consume_to_int(bitstream, 11)
        children = []
        for i in range(child_count):
            children.append(Packet(bitstream))
        return children


def get_all_packets(bitstream) -> list[Packet]:
    packets = []
    try:
        while True:
            packets.append(Packet(bitstream))
    except EOFError:
        pass
    return packets


bin_str = []

with open("input.txt") as file:
    for char in file.readline().strip():
        bin_vals = hex_to_bin(char)
        bin_str.extend(bin_vals)


def sum_versions(packets):
    sum = 0
    for packet in packets:
        sum += packet.version
        if packet.children:
            sum += sum_versions(packet.children)

    return sum


all_packets = get_all_packets(iter(bin_str))

print(f"All Packets[{len(all_packets)}]: {all_packets}")

print(f"Outer Value: {all_packets[0].value()}")


