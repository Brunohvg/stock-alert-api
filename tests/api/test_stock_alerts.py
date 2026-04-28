def test_create_stock_alert(client):
    response = client.get('/api/v1/stock-alerts')
    assert response.status_code == 200
    assert response.json() == {'message': 'Lista de alertas de estoque'}
