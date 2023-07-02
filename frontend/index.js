let Year = document.getElementById("textbox1");
let Present_Price = document.getElementById("textbox2");
let Kms_Driven = document.getElementById("textbox3");
let Fuel_Type = document.getElementById("textbox4");
let Seller_Type = document.getElementById("textbox5");
let Transmission = document.getElementById("textbox6");
let Owner = document.getElementById("textbox7");

var result = document.getElementById("result");
console.log(
  Year.value,
  Present_Price.value,
  Kms_Driven.value,
  Fuel_Type.value,
  Seller_Type.value,
  Transmission.value,
  Owner.value
);

async function send_data() {
  console.log(
    Year.value,
    Present_Price.value,
    Kms_Driven.value,
    Fuel_Type.value,
    Seller_Type.value,
    Transmission.value,
    Owner.value
  );
  const url = "http://127.0.0.1:8000/predict_price";
  // POST request using fetch()
  const response = await fetch(url, {
    // Adding method type
    method: "POST",

    // Adding body or contents to send
    body: JSON.stringify({
      Year: Year.value,
      Present_Price: Present_Price.value,
      Kms_Driven: Kms_Driven.value,
      Fuel_Type: Fuel_Type.value,
      Seller_Type: Seller_Type.value,
      Transmission: Transmission.value,
      Owner: Owner.value,
    }),

    // Adding headers to the request
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  // Converting to JSON
  // .then((response) => response.json())

  // // Displaying results to console
  // .then((json) => (result.innerHTML = json));
  const data = await response.json();
  console.log(data["Selling_Price"]);
  result.innerText += data["Selling_Price"];
}
