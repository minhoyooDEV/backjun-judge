class DataLoader {
  $dataLoader = null;
  data = null;
  
  constructor({$target, data}) {
      const $dataLoader = document.createElement("div");
      $dataLoader.className = "DataLoader";
      this.$dataLoader = $dataLoader;
      $dataLoader.innerText = '로~ 딩 ~ 중'
      $target.appendChild($dataLoader);

      this.data = data;
      this.render();
      console.log("datLoader created.", this);

  }

  close() {

  }

  setState(nextData) {
      this.data = nextData
      this.render();
  }
  render() {
      if (this.data.isLoading) {
          this.$dataLoader.style.display = "block";
      } else {
          this.$dataLoader.style.display = "none";
      }
  }
}