from scripts import main

# pytestを実行するには、関数の始まりの語句をtestにする必要があります
def test_f_pattern1():
    # 'assert'を使って、正しさをチェックできます
    assert main.f(1) == 4
    assert main.f(0) == 1
    assert main.f(-1) == None


def test_f_pattern2():
    assert main.f(1) != 1