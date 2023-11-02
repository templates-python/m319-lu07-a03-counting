from main import main

def test_main(monkeypatch, capsys):
    """Testet die Hauptfunktion durch Überprüfung des Outputs."""
    monkeypatch.setattr('builtins.input', lambda _: '4')
    main()
    captured = capsys.readouterr()
    assert captured.out == '0\n1\n2\n3\n'