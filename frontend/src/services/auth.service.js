import axios from "axios";

const API_URL = "http://127.0.0.1:80/accounts/";

class AuthService {
  login(username, password) {
    var bodyFormData = new FormData();
    bodyFormData.append("username", username)
    bodyFormData.append("password", password)
    return axios
      .post(API_URL + "token", bodyFormData)
      .then(response => {
        if (response.data.access_token) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }

  register(username, email, password) {
    return axios.post(API_URL + "user", {
      username,
      email,
      password
    });
  }

  getCurrentUser() {
    return JSON.parse(localStorage.getItem('user'));;
  }
}

export default new AuthService();
