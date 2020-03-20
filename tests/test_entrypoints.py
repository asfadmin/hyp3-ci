def test_proc_insar_isce(script_runner):
    ret = script_runner.run('hyp3_ci', '-h')
    assert ret.success


def test_proc_insar_isce(script_runner):
    ret = script_runner.run('proc_ci', '-h')
    assert ret.success

