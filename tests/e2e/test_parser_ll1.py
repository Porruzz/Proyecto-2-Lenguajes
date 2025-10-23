import subprocess

def test_parser_ll1_accepts_valid():
    result = subprocess.run(["python3", "-m", "src.main", "--parse", "examples/ok/expresion1.txt"], capture_output=True, text=True)
    assert "ACCEPT" in result.stdout

def test_parser_ll1_rejects_invalid():
    result = subprocess.run(["python3", "-m", "src.main", "--parse", "examples/bad/error1.txt"], capture_output=True, text=True)
    assert "REJECT" in result.stdout
