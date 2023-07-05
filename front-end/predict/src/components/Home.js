import React, { useState } from "react";
import "./style.css";

const Home = () => {
  const [year, setYear] = useState("");
  const [presentPrice, setPresentPrice] = useState("");
  const [kmsDriven, setKmsDriven] = useState("");
  const [fuelType, setFuelType] = useState("");
  const [sellerType, setSellerType] = useState("");
  const [transmission, setTransmission] = useState("");
  const [owner, setOwner] = useState("");
  const [result, setResult] = useState(0);

  const send_data = async () => {
    console.log(
      year,
      presentPrice,
      kmsDriven,
      fuelType,
      sellerType,
      transmission,
      owner
    );

    try {
      const url = "http://127.0.0.1:8000/predict_price";
      // POST request using fetch()
      const response = await fetch(url, {
        // Adding method type
        method: "POST",

        // Adding body or contents to send
        body: JSON.stringify({
          Year: year,
          Present_Price: presentPrice,
          Kms_Driven: kmsDriven,
          Fuel_Type: fuelType,
          Seller_Type: sellerType,
          Transmission: transmission,
          Owner: owner,
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
      setResult(data["Selling_Price"]);
      console.log(data["Selling_Price"]);
      // result.innerText += data["Selling_Price"];
    } catch (e) {
      console.log("error =", e);
    }
  };

  return (
    <div className="main">
      <div className="heading">
        <h1>Car Price Prediction</h1>
      </div>
      <div className="inputs">
        <input
          type="number"
          name="year"
          id="year"
          placeholder="Enter Year of Car Purchased:"
          value={year}
          onChange={(e) => setYear(e.target.value)}
        />
        <input
          type="number"
          name="present_price"
          id="pres_price"
          placeholder="Enter Present Price of a Car(In terms of Lakhs only):"
          value={presentPrice}
          onChange={(e) => setPresentPrice(e.target.value)}
        />
        <input
          type="number"
          name="KmsDriven"
          id="kms"
          placeholder="Enter Kilometers of Car Driven:"
          value={kmsDriven}
          onChange={(e) => setKmsDriven(e.target.value)}
        />
        <input
          type="number"
          name="fuel-type"
          id="fuel"
          placeholder="Enter Fuel Type(0 - Petrol, 1 - Diesel, 2 - CNG):"
          value={fuelType}
          onChange={(e) => setFuelType(e.target.value)}
        />
        <input
          type="number"
          name="seller_type"
          id="seller"
          placeholder="Enter Seller Type(0 - Dealer, 1 - Individual):"
          value={sellerType}
          onChange={(e) => setSellerType(e.target.value)}
        />
        <input
          type="number"
          name="transmission"
          id="transmission"
          placeholder="Enter Transmission Type(0 - Manual, 1 - Automatic):"
          value={transmission}
          onChange={(e) => setTransmission(e.target.value)}
        />
        <input
          type="number"
          name="owner"
          id="owner"
          placeholder="Enter Owner Type:"
          value={owner}
          onChange={(e) => setOwner(e.target.value)}
        />
      </div>
      <div className="buttons">
        <input
          className="btn1"
          onClick={send_data}
          type="button"
          value="Submit"
        />
        <input className="btn2" type="reset" value="Reset" />
      </div>
      <div className="output">
        Expected Price: <span className="amt">{result}</span>
      </div>
    </div>
  );
};

export default Home;
