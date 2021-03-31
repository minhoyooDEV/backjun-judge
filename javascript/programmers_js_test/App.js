console.log("app is running!");

const LastSearchDataKey = "last_search_data";
class App {
  $target = null;
  data = JSON.parse(sessionStorage.getItem(LastSearchDataKey) || "[]");

  constructor($target) {
    this.$target = $target;

    this.searchInput = new SearchInput({
      $target,
      onSearch: async (keyword) => {
        this.dataLoader.setState({ isLoading: true });
        try {
          const { data } = await api.fetchCats(keyword);
          sessionStorage.setItem(LastSearchDataKey, JSON.stringify(data));
          this.setState(data);
        } catch (error) {
          console.warn(error);
          sessionStorage.setItem(LastSearchDataKey, "[]");
        } finally {
          this.dataLoader.setState({ isLoading: false });
        }
      },
      onRandomSearch: async () => {
        this.dataLoader.setState({ isLoading: true });
        try {
          const { data } = await api.fetchRandom50();
          sessionStorage.setItem(LastSearchDataKey, JSON.stringify(data));
          this.setState(data);
        } catch (error) {
          console.warn(error);
          sessionStorage.setItem(LastSearchDataKey, "[]");
        } finally {
          this.dataLoader.setState({ isLoading: false });
        }
      },
    });
    this.searchResult = new SearchResult({
      $target,
      initialData: this.data,
      onClick: (id) => {
        this.dataLoader.setState({ isLoading: true });
        api.fetchCat(id).then(({ data }) => {
          this.dataLoader.setState({ isLoading: false });
          this.imageInfo.setState({
            visible: true,
            image: data,
          });
        });
      },
    });

    this.imageInfo = new ImageInfo({
      $target,
      data: {
        visible: false,
        image: null,
      },
    });

    this.dataLoader = new DataLoader({
      $target,
      data: {
        isLoading: false,
      },
    });
  }

  setState(nextData) {
    console.log(this);
    this.data = nextData;
    this.searchResult.setState(nextData);
  }
}
