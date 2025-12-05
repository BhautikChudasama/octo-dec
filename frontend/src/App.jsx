import React, { useState } from "react";
import PricingForm from "./components/PricingForm";
import PricingResult from "./components/PricingResult";

export default function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <h1>⚡ NodeOps Pricing Calculator</h1>
      <PricingForm onResult={setResult} />
      {result && <PricingResult data={result} />}
    </div>
  );
}
