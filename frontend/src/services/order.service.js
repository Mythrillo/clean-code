import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://127.0.0.1:80/orders/';

class OrderService {
    createNewOrder() {
        return axios.post(API_URL, { headers: authHeader() });
    }

    getOrder(orderId) {
        return axios.get(API_URL + toString(orderId), { headers: authHeader() })
    }

    listOrders() {
        return axios.get(API_URL, { headers: authHeader() });
    }

    deleteOrder(orderId) {
        return axios.delete(API_URL + toString(orderId), { headers: authHeader() })
    }

    getOrderItems(orderId) {
        return axios.get(API_URL + toString(orderId) + "/products", { headers: authHeader() })
    }

    addProductToOrder(orderId, productId, amount) {
        return axios.post(API_URL + "add_product", { order_id: orderId, product_id: productId, amount: amount }, { headers: authHeader() })
    }

}

export default new OrderService();
