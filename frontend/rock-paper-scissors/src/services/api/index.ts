import axios, { AxiosInstance, AxiosRequestConfig } from "axios";

type Request = { url: string; method: string; params: unknown };
type Requests = Record<string, Request>;
type Client = { [key: string]: any };

const config: AxiosRequestConfig = {
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 1000,
};
const requests: Requests = {
  login: { url: "login/", method: "post", params: {} },
  register: { url: "register/", method: "post", params: {} },
};

class Api {
  private requests: Requests;
  private client: Client;

  constructor(requests: Requests, config: AxiosRequestConfig) {
    this.requests = requests;

    this.client = axios.create(config);
  }

  async createRequest(requestName: string, body = {}) {
    const request = this.requests[requestName];
    const requestParams = Object.assign(request.params, body);

    if (request) {
      const response = await this.client[request.method](
        request.url,
        requestParams
      );

      return response;
    }
  }
}

export default new Api(requests, config);
