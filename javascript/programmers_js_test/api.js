const API_ENDPOINT =
  "https://oivhcpn8r9.execute-api.ap-northeast-2.amazonaws.com/dev";

const api = {
  fetchCats: (keyword) => {
    return fetch(`${API_ENDPOINT}/api/cats/search?q=${keyword}`).then((res) =>
      res.json()
    );
  },
  fetchCat: async (id) => {
    try {
      const result = await fetch(`${API_ENDPOINT}/api/cats/${id}`);
      return result.json();
    } catch (error) {
      console.warn(error);
    }
  },
  fetchRandom50: async () => {
    try {
      const result = await fetch(`${API_ENDPOINT}/api/cats/random50`);
      return result.json();
    } catch (error) {
      console.warn(error);
    }
  },
};
