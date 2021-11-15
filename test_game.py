from drawFigure import save

def test_tmp_dir(tmpdir):
    data_in = "13213"
    fpath = f"{tmpdir}/test.txt"
    save(fpath,data_in)

    with open(fpath) as file_out:
        data_out = file_out.read()

    assert data_in == 'data_out'