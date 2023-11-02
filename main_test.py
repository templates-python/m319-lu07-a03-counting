from main import main

def test_counting_for_loop(monkeypatch, capsys):
    """Testet das Zählen mit einer Schleife durch Überprüfung des Outputs."""
    monkeypatch.setattr('builtins.input', lambda: '4')
    main()
    captured = capsys.readouterr()
    assert captured.out == '0\n1\n2\n3\n4\n'
