// axios#request(config)
// axios#get(url[, config])
// axios#delete(url[, config])
// axios#head(url[, config])
// axios#options(url[, config])
// axios#post(url[, data[, config]])
// axios#put(url[, data[, config]])
// axios#patch(url[, data[, config]])
// axios#getUri([config])


import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

const getaxios = () => {
  const axiosInstance = axios.create({
    baseURL: `${API_URL}/api/v1/articles`,
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
  });

  return axiosInstance.get('');
};

export default getaxios;
