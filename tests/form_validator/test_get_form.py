def test_get_form_with_correct_data(client, request_data, get_form_url):
    res = client.post(get_form_url, json=request_data)

    assert res.status_code == 200


def test_get_form_with_incorrect_email(client, request_data, incorrect_email, get_form_url):
    request_data.update(incorrect_email)

    res = client.post(get_form_url, json=request_data)

    assert res.status_code == 400
    assert 'email' in res.json()


def test_get_form_with_incorrect_date(client, request_data, incorrect_date, get_form_url):
    request_data.update(incorrect_date)

    res = client.post(get_form_url, json=request_data)
    print(res.json())

    assert res.status_code == 400
    assert 'date_of_birth' in res.json()


def test_get_form_with_incorrect_phone(client, request_data, incorrect_phone, get_form_url):
    request_data.update(incorrect_phone)

    res = client.post(get_form_url, json=request_data)

    assert res.status_code == 400
    assert 'phone' in res.json()
