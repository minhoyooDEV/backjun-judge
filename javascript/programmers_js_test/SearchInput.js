const TEMPLATE = '<input type="text">';

class SearchInput {
  history = [];
  onSearch = null;

  constructor({ $target, onSearch, onRandomSearch }) {
    const $searchInputWrap = document.createElement("div");
    $searchInputWrap.className = "SearchInput";
    const $searchInput = document.createElement("input");
    const $searchRandomBtn = document.createElement("button");
    $searchRandomBtn.innerText = "오늘의냥";
    this.$searchInput = $searchInput;
    this.$searchInput.focus();
    this.$searchInput.placeholder = "고양이를 검색해보세요.|";

    $searchInputWrap.appendChild($searchInput);
    $searchInputWrap.appendChild($searchRandomBtn);
    $target.appendChild($searchInputWrap);

    this.onSearch = onSearch;

    $searchInput.addEventListener("click", (e) => {
      if (e.target.value) {
        e.target.value = "";
      }
    });
    $searchInput.addEventListener("keyup", (e) => {
      if (e.keyCode === 13) {
        const keyword = e.target.value;
        onSearch(keyword);
        this.updateHistory(keyword);
      }
    });
    $searchRandomBtn.addEventListener("click", (e) => {
      onRandomSearch();
    });

    console.log("SearchInput created.", this);

    const $serachHistory = document.createElement("div");
    this.$serachHistory = $serachHistory;
    $target.appendChild($serachHistory);

    this.render();
  }

  updateHistory(keyword) {
    if (this.history.length < 5) {
      this.history.push(keyword);
    } else {
      this.history.shift();
      this.history.push(keyword);
    }
    this.render();
  }

  render() {
    if (this.history.length) {
      this.$serachHistory.innerHTML = `${this.history
        .map((keyword) => `<span class="keyword" > ${keyword}</span > `)
        .join(", ")}`;
    } else {
      this.$serachHistory.innerHTML = "";
    }

    this.$serachHistory.querySelectorAll(".keyword").forEach(($item, index) => {
      $item.addEventListener("click", () => {
        this.onSearch(this.history[index]);
      });
    });
  }
}
