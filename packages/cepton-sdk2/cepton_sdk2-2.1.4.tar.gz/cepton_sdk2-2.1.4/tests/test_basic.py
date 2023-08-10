#!/usr/bin/env python3
"""
Sample script for getting points from a pcap.
"""
import cepton_sdk2.utils as utils

if __name__ == "__main__":
    # Variables
    capture_path = "../../tests/test_parse/data_files/novaB1_short.pcap" # put path to pcap here
    x = len(list(utils.ReadPcap(capture_path, 0)))
    assert x >= 200, f"expected something >= 200, instead got {x}"

    x = len(list(utils.ReadPcap(capture_path, 1)))
    assert x >= 10000, f"expected something >= 10000, instead got {x}"

    x = len(list(utils.ReadPcap(capture_path, 10)))
    assert x >= 1000, f"expected something >= 1000, instead got {x}"

    x = len(list(utils.ReadPcap(capture_path, 100)))
    assert x >= 100, f"expected something >= 100, instead got {x}"

    x = len(list(utils.ReadPcap(capture_path, 1000)))
    assert x >= 10, f"expected something >= 10, instead got {x}"