from scanner.core import scan_ports

def test_scan_ports():
    results = scan_ports("127.0.0.1", [80, 443])
    assert isinstance(results, list)
    for port, status in results:
        assert isinstance(port, int)
        assert status in ["Open", "Closed"]
