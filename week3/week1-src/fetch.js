function getImageUrl(img_urls) {
  let normalized_img_urls = img_urls.replace(/\.JPG/gi, ".jpg");
  let urls = normalized_img_urls.split(".jpg");

  let first_url = urls[0] + ".jpg";
  console.log(first_url);
  return first_url;
}

function getData() {
  fetch(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      dataToUse = data.data.results;

      for (let i = 0; i < 3; i++) {
        let dSmaill = data.data.results[i];
        let container = document.getElementById(`small${i + 1}`);
        let newImageElement = document.createElement("img");
        newImageElement.className = "small-img";
        newImageElement.alt = "";
        url = getImageUrl(dSmaill.filelist);
        newImageElement.src = url;
        container.appendChild(newImageElement);

        let newTextElement = document.createElement("div");
        newTextElement.className = "small-text";
        newTextElement.textContent = dSmaill.stitle;
        container.appendChild(newTextElement);
      }
      for (let i = 3; i < 13; i++) {
        let dBig = data.data.results[i];
        let container = document.getElementById(`big${i - 2}`);

        let newImageElement = document.createElement("img");
        newImageElement.className = "big-img";
        newImageElement.alt = "";
        url = getImageUrl(dBig.filelist);
        newImageElement.src = url;
        container.appendChild(newImageElement);

        let newTextElement = document.createElement("div");
        newTextElement.className = "big-text";
        newTextElement.textContent = dBig.stitle;
        container.appendChild(newTextElement);
      }
    });
}
document.addEventListener("DOMContentLoaded", getData);
