from urllib.parse import urljoin


class ServiceAPI:
    """Service API endpoints."""
    host = 'http://127.0.0.1:8080'
    add_entity = urljoin(host, '/api/create')
    delete_entity = urljoin(host, '/api/delete/{id}')
    get_entity = urljoin(host, '/api/get/{id}')
    get_all_entities = urljoin(host, '/api/getAll')
    patch_entity = urljoin(host, '/api/patch/{id}')
