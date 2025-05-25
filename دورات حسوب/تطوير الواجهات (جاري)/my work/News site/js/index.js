// main
// Initialize Swiper
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 20,
  autoplay: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    768: {
      slidesPerView: 2,
      spaceBetween: 30,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 50,
    },
  },
});

// footer
document.getElementById("current-year").textContent = new Date().getFullYear();

// ----------------------- fetch -------------------------------
const API_URL = "http://127.0.0.1:4010/";

// fetch videos
const video = `
<div class="swiper-img">
    <img src="" alt="">
    <i class="fas fa-play"></i>
</div>
<h5 href="" class="video-title"></h5>
`;

class VideoCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = video;
    this.classList.add("swiper-slide");
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("title"));
    this.querySelector("h5").setAttribute("href", this.getAttribute("href"));
    this.querySelector("h5").innerHTML = this.getAttribute("title");
  }
}

window.customElements.define("video-element", VideoCombonent);
async function videoFetch() {
  let res = await fetch(API_URL + "videos");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("video-element");
    element.setAttribute("src", item.img_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    document.getElementById("swiper-wrapper").appendChild(element);
  });
}
videoFetch();

// fetch slider
const slider = `
      <img src="" class="d-block w-100" alt="">
      <div class="carousel-caption d-none d-md-block">
          <a href=""></a>
      </div>
`;

class SliderCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = slider;
    this.classList.add("carousel-item");
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("title"));
    this.querySelector("a").setAttribute("href", this.getAttribute("href"));
    this.querySelector("a").innerHTML = this.getAttribute("title");
  }
}

window.customElements.define("slider-element", SliderCombonent);
async function sliderFetch() {
  let res = await fetch(API_URL + "videos");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("slider-element");
    element.setAttribute("src", item.img_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    document.getElementById("carousel-inner").appendChild(element);
  });
  document
    .getElementById("carousel-inner")
    .firstElementChild.classList.add("active");
}
sliderFetch();

// fetch header-articles
const headerArticles = `
    <div class="col-5"><img src="" alt=""></div>
    <div class="col-7 mx-0">
        <a href="" class="article-title">
        </a>
    </div>
`;

class HeaderArticlesCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = headerArticles;
    this.classList.add("row", "mb-5");
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("title"));
    this.querySelector("a").setAttribute("href", this.getAttribute("href"));
    this.querySelector(
      "a"
    ).innerHTML = `<span class="article-classification me-2 px-2">${this.getAttribute(
      "category"
    )}</span> ${this.getAttribute("title")}`;
  }
}

window.customElements.define(
  "header-articles-element",
  HeaderArticlesCombonent
);
async function headerArticlesFetch() {
  let res = await fetch(API_URL + "header-articles");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("header-articles-element");
    element.setAttribute("src", item.img_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    element.setAttribute("category", item.category);
    document.getElementById("header-articles").appendChild(element);
  });
  document
    .getElementById("header-articles")
    .lastElementChild.classList.remove("mb-5");
}
headerArticlesFetch();

// fetch news-articles
const news = `
    <div><img src="" alt=""></div>
    <div class="mt-2 mx-0">
        <a href="" class="article-title"></a>
    </div>
`;

class NewsCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = news;
    this.classList.add("col-lg-3", "col-md-6", "col-12", "mb-5");
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("title"));
    this.querySelector("a").setAttribute("href", this.getAttribute("href"));
    this.querySelector(
      "a"
    ).innerHTML = `<span class="article-classification me-2 px-2">${this.getAttribute(
      "category"
    )}</span> ${this.getAttribute("title")}`;
  }
}

window.customElements.define("news-element", NewsCombonent);
async function newsFetch() {
  let res = await fetch(API_URL + "news");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("news-element");
    element.setAttribute("src", item.img_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    element.setAttribute("category", item.category);
    document.getElementById("news-articles").appendChild(element);
  });
}
newsFetch();

// fetch most-read
const mostRead = `
    <div class="col-lg-5 col-12"><img src="" alt=""></div>
    <div class="col-lg-7 col-12 mx-0">
        <div class="d-flex row gap-3">
            <a href="" class="article-title"></a>
            <p class="article-body"></p>
            <div class="article-footer"></div>
        </div>
    </div>
`;

class MostReadCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = mostRead;
    this.classList.add("most-read-card", "row", "mb-5", "p-5");
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("title"));
    this.querySelector("a").setAttribute("href", this.getAttribute("href"));
    this.querySelector("a").innerHTML = this.getAttribute("title");
    this.querySelector("p").innerHTML = this.getAttribute("paragraph");
    this.querySelector(".article-footer").innerHTML = moment(parseInt(this.getAttribute("date"))).format("Do MMMM YYYY");
  }
}

window.customElements.define("most-read-element", MostReadCombonent);
async function mostReadFetch() {
  let res = await fetch(API_URL + "most-read");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("most-read-element");
    element.setAttribute("src", item.img_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    element.setAttribute("paragraph", item.paragraph);
    element.setAttribute("date", item.date);
    document.getElementById("most-read-articles").appendChild(element);
  });
  document.getElementById("most-read-articles").children[1].children[0].setAttribute("class", "col-12");
  document.getElementById("most-read-articles").children[1].children[1].setAttribute("class", "col-12");

}
mostReadFetch();



// fetch opinion-articles
const opinionArticles = `
  <div class="card text-center">
      <div class="card-body">
          <h5 class="card-title"></h5>
          <p class="card-text"></p>
          <div class="card-person d-flex flex-column align-items-center">
              <img class="col-3" src="" alt="">
              <h6></h6>
          </div>
      </div>
      <div class="card-footer">
      </div>
  </div>
`;

class OpinionArticlesCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = opinionArticles;
    this.classList.add("col-lg-3", "col-md-6", "col-12");
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("name"));
    this.querySelector(".card-title").innerHTML = this.getAttribute("title");
    this.querySelector("h6").innerHTML = this.getAttribute("name");
    this.querySelector(".card-footer").innerHTML = this.getAttribute("date");
  }
}

window.customElements.define("opinion-articles-element", OpinionArticlesCombonent);
async function opinionArticlesFetch() {
  let res = await fetch(API_URL + "opinion-articles");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("opinion-articles-element");
    element.setAttribute("src", item.user_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    element.setAttribute("name", item.user_name);
    element.setAttribute("date", item.date);
    document.getElementById("opinion-articles-items").appendChild(element);
  });
}
opinionArticlesFetch();



// fetch latest-news
// const latestNews = `
//   <div class="card text-center">
//       <div class="card-body">
//           <h5 class="card-title"></h5>
//           <p class="card-text"></p>
//           <div class="card-person d-flex flex-column align-items-center">
//               <img class="col-3" src="" alt="">
//               <h6></h6>
//           </div>
//       </div>
//       <div class="card-footer">
//       </div>
//   </div>
// `;

// class LatestNewsCombonent extends HTMLElement {
//   constructor() {
//     super();
//   }
//   connectedCallback() {
//     this.innerHTML = latestNews;
//     this.classList.add("col-lg-3", "col-md-6", "col-12");
//     this.querySelector("img").setAttribute("src", this.getAttribute("src"));
//     this.querySelector("img").setAttribute("alt", this.getAttribute("name"));
//     this.querySelector(".card-title").innerHTML = this.getAttribute("title");
//     this.querySelector("h6").innerHTML = this.getAttribute("name");
//     this.querySelector(".card-footer").innerHTML = this.getAttribute("date");
//   }
// }

// window.customElements.define("latest-news-element", LatestNewsCombonent);
// async function latestNewsFetch() {
//   let res = await fetch(API_URL + "latest-news");
//   let data = await res.json();

//   data.map((item) => {
//     let element = document.createElement("latest-news-element");
//     element.setAttribute("src", item.user_uri);
//     element.setAttribute("href", item.link);
//     element.setAttribute("title", item.title);
//     element.setAttribute("name", item.user_name);
//     element.setAttribute("date", item.date);
//     document.getElementById("latest-news-items").appendChild(element);
//   });
// }
// latestNewsFetch();


// =================================== seacrch =============================
// =================================== seacrch =============================
// fetch seacrch-artile
const seacrchArtile = `
  <div class="row mb-5">
      <div class="col-md-5 col-12"><img src="" alt=""></div>
      <div class="col-md-7 col-12 mx-0">
          <div class="d-flex row gap-3">
              <a href="" class="article-title"></a>
              <p class="article-body"></p>
              <div class="article-footer"></div>
          </div>
      </div>
  </div>
  <hr class="mt-3">
`;

class SeacrchArtileCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = seacrchArtile;
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("title"));
    this.querySelector(".article-title").setAttribute("href", this.getAttribute("href"));
    this.querySelector(".article-title").innerHTML = this.getAttribute("title");
    this.querySelector(".article-body").innerHTML = this.getAttribute("paragraph");
    this.querySelector(".article-footer").innerHTML = moment(parseInt(this.getAttribute("date"))).format("Do MMMM YYYY");
  }
}
window.customElements.define("seacrch-artile-element", SeacrchArtileCombonent);
async function seacrchArtileFetch() {
  let res = await fetch(API_URL + "seacrch-artile");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("seacrch-artile-element");
    element.setAttribute("src", item.img_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    element.setAttribute("paragraph", item.paragraph);
    element.setAttribute("date", item.date);
    document.getElementById("search-result").appendChild(element);
  });
}
seacrchArtileFetch();


// =================================== single-article =============================
// =================================== single-article =============================
// fetch seacrch-artile
const suggestedArticles = `
<div><img src=".jpg" alt=""></div>
<div class="mt-2 mx-0">
    <a href="" class="article-title"></a>
</div>
`;

class SuggestedArticlesCombonent extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = suggestedArticles;
    this.classList.add("col-lg-4", "mb-5", "col-12");
    this.querySelector("img").setAttribute("src", this.getAttribute("src"));
    this.querySelector("img").setAttribute("alt", this.getAttribute("title"));
    this.querySelector(".article-title").setAttribute("href", this.getAttribute("href"));
    this.querySelector(".article-title").innerHTML = this.getAttribute("title");
  }
}

window.customElements.define("suggested-articles-element", SuggestedArticlesCombonent);
async function suggestedArticlesFetch() {
  let res = await fetch(API_URL + "suggested-articles");
  let data = await res.json();

  data.map((item) => {
    let element = document.createElement("suggested-articles-element");
    element.setAttribute("src", item.img_uri);
    element.setAttribute("href", item.link);
    element.setAttribute("title", item.title);
    document.getElementById("suggested-articles-result").appendChild(element);
  });
}
suggestedArticlesFetch();