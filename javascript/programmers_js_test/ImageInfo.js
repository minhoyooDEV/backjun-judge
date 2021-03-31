class ImageInfo {
  $imageInfo = null;
  data = null;

  constructor({ $target, data }) {
    const $imageInfo = document.createElement("div");
    $imageInfo.className = "ImageInfo";
    this.$imageInfo = $imageInfo;
    this.$imageInfo.addEventListener("click", () => {
      this.closeModal();
    });
    $target.appendChild($imageInfo);
    document.addEventListener("keydown", (e) => {
      if (this.data?.visible && e.keyCode === 27) {
        this.closeModal();
      }
    });
    this.data = data;

    this.render();
  }
  closeModal() {
    this.setState({
      visible: false,
      image: null,
    });
  }

  setState(nextData) {
    this.data = nextData;
    this.render();
  }

  render() {
    if (this.data.visible) {
      const { name, url, temperament, origin } = this.data.image;

      this.$imageInfo.innerHTML = `
        <div class="content-wrapper">
          <div class="title">
            <span>${name}</span>
            <div class="close">x</div>
          </div>
          <img src="${url}" alt="${name}"/>        
          <div class="description">
            <div>성격: ${temperament}</div>
            <div>태생: ${origin}</div>
          </div>
        </div>`;
      this.$imageInfo.style.display = "block";
      this.$imageInfo.children[0].addEventListener("click", (e) => {
        e.stopPropagation();
      });
      this.$imageInfo
        .getElementsByClassName("close")[0]
        .addEventListener("click", () => {
          this.closeModal();
        });
    } else {
      this.$imageInfo.style.display = "none";
    }
  }
}
