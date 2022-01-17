from tackle.main import tackle


def test_min(change_base_dir, read_fixture):
    create = tackle(**read_fixture('min.yaml'), no_input=True)
    assert len(create['demo']) == 0


def test_monty(change_base_dir, read_fixture):
    create = tackle(**read_fixture('monty.yaml'), no_input=True)
    assert len(create['demo']) == 1
    assert create['do_demo'][0]['wingspeed'] == 'I donno'
    # TODO: There is an error here - https://github.com/robcxyz/tackle-box/issues/11
    # assert create['do_demo'][0]['name'] == 'stuff'


def test_providers(change_base_dir, read_fixture):
    create = tackle(**read_fixture('providers.yaml'), no_input=True)
    assert len(create['demo']) == 1


def test_jinja(change_base_dir, read_fixture):
    create = tackle(**read_fixture('jinja.yaml'), no_input=True)
    assert len(create['demo']) == 1


def test_embedded(change_base_dir, read_fixture):
    create = tackle(**read_fixture('embedded.yaml'), no_input=True)
    assert len(create['demo']) == 1
