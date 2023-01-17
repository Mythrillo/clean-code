import axios from 'axios';
import authHeader from './auth-header';

const API_URL = 'http://127.0.0.1:80/accounts/';

class UserService {
  getPublicContent() {
    return axios.get(API_URL + 'user/me', { headers: authHeader() });
  }
}

export default new UserService();
