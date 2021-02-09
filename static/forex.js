const codeList = document.getElementById("codelist");
const fromInput = document.getElementById("convertfrom");
const toInput = document.getElementById("convertto");
const inputContainer = document.querySelector("form");


const fillEmpty = (code) => {
  if (!fromInput.value) {
    fromInput.value = code;
  } else if (!toInput.value) {
    toInput.value = code;
  } else {
    return;
  }
};


codeList.addEventListener("click", function(event) {
  if (event.target.tagName === "LI") {
    let code = event.target.textContent.substring(0, 3);
    fillEmpty(code);
  }
});

inputContainer.addEventListener("click", function(event) {
  if (event.target.tagName === "I") {
    event.target.previousElementSibling.value = "";
  }
})


