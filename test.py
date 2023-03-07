from pylint import epylint as lint
import os

def test_flask_app():
    (pylint_stdout, pylint_stderr) = lint.py_run("app.py", return_std=True)
    expected_return_code = os.environ.get('PYLINT_RETVAR', '0')
    assert pylint_stdout.getvalue() == ''
    assert pylint_stderr.getvalue() == ''
    assert pylint_stdout.returncode == int(expected_return_code)
