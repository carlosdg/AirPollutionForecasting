/**
 * Hamburger button
 */
const hamburgerButton = document.querySelector(".burger");
const nav = document.getElementById(hamburgerButton.dataset.target);

hamburgerButton.addEventListener("click", e => {
  hamburgerButton.classList.toggle("is-active");
  nav.classList.toggle("is-active");
});

/**
 * Tab switches
 */
const tabLinks = document.querySelectorAll("[data-content-tab]");
const contentTabs = document.querySelectorAll(".content-tab");

tabLinks.forEach(el =>
  el.addEventListener("click", ({ currentTarget }) => {
    for (let i = 0; i < tabLinks.length; i++) {
      tabLinks[i].classList.remove("is-active");
      contentTabs[i].style.display = "none";
    }

    currentTarget.classList.add("is-active");
    document.getElementById(currentTarget.dataset.contentTab).style.display =
      "block";
  })
);

/**
 * Latests measures
 */
const measuresContainer = document.getElementById("measures-container");
const selectVariable = document.getElementById("select-variable");
const prev = document.getElementById("pagination-prev");
const next = document.getElementById("pagination-next");

function fillMeasuresTable({ variable, numberItems, offset }) {
  const uri = `http://localhost:5000/apf/api/v1.0/measures/${variable}/${numberItems}/${offset}`;
  measuresContainer.innerHTML = "Loading...";

  return fetch(uri)
    .then(res => res.json())
    .then(data => {
      measuresContainer.innerHTML = "";

      data.forEach(({ date, value }) => {
        const row = document.createElement("tr");
        const header = document.createElement("th");
        const data = document.createElement("td");

        header.innerText = date;

        if (value !== null && value !== undefined) {
          data.innerText = value.toFixed(2);
        } else {
          data.innerText = "null";
        }

        row.appendChild(header);
        row.appendChild(data);
        measuresContainer.appendChild(row);
      });
    });
}

function fillMeasureVariableSelect() {
  return fetch("http://localhost:5000/apf/api/v1.0/meta")
    .then(res => res.json())
    .then(data => {
      selectVariable.innerHTML = "";
      data.measure_names.forEach(name => {
        const option = document.createElement("option");
        option.value = name;
        option.innerText = name;

        selectVariable.appendChild(option);
      });
    });
}

function initMeasureTable() {
  const measureTableInfo = {
    variable: selectVariable.selectedOptions[0].value,
    numberItems: 12,
    offset: 0
  };

  selectVariable.addEventListener("change", e => {
    measureTableInfo.variable = e.target.selectedOptions[0].value;
    fillMeasuresTable(measureTableInfo);
  });

  prev.addEventListener("click", e => {
    measureTableInfo.offset += measureTableInfo.numberItems;
    fillMeasuresTable(measureTableInfo);
  });

  next.addEventListener("click", e => {
    measureTableInfo.offset -= measureTableInfo.numberItems;
    fillMeasuresTable(measureTableInfo);
  });

  fillMeasuresTable(measureTableInfo);
}

fillMeasureVariableSelect().then(initMeasureTable);
