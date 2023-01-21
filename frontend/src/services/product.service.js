import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://127.0.0.1:80/products/';

class ProductService {
    createProduct(title, description, price) {
        return axios.post(API_URL, { title, description, price }, { headers: authHeader() });
    }

    getProduct(productId) {
        return axios.get(API_URL + productId)
    }

    listProducts() {
        return axios.get(API_URL);
    }

    deleteProduct(productId) {
        return axios.delete(API_URL + toString(productId), { headers: authHeader() })
    }

    updateProduct(productId, description, price, title) {
        return axios.patch(API_URL + toString(productId), { headers: authHeader() })
    }
}

export default new ProductService();
