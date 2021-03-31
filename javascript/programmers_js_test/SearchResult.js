class SearchResult {
  $searchResult = null;
  data = null;
  onClick = null;

  constructor({ $target, initialData, onClick }) {
    this.$searchResult = document.createElement("div");
    this.$searchResult.className = "SearchResult";
    $target.appendChild(this.$searchResult);

    this.data = initialData;
    this.onClick = onClick;

    this.render();
  }

  setState(nextData) {
    this.data = nextData;
    this.render();
  }

  render() {
    if (this.data.length) {
      this.$searchResult.innerHTML = this.data
        .map(
          (cat) => `
          <div class="item">
            <img src=${cat.url} alt=${cat.name} />
          </div>
        `
        )
        .join("");
    } else {
      this.$searchResult.innerHTML = `<div> 검색 결과가 없습니다 ㅠ</div>`;
    }

    this.$searchResult.querySelectorAll(".item").forEach(($item, index) => {
      $item.addEventListener("click", () => {
        const image = this.data[index];
        this.onClick(image.id);
      });
    });
  }
}
