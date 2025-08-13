import sender_stand_request as api
import request_data as data   # здесь лежит data.order_body и data.headers (если нужно)

def test_track_order():
    # 1) создаём заказ
    create_resp = api.post_new_order(data.order_body)
    assert create_resp.status_code in (200, 201)

    create_json = create_resp.json()
    assert "track" in create_json
    track = create_json["track"]

    # 2) получаем заказ по треку
    track_resp = api.get_track_order(track)
    assert track_resp.status_code == 200

    