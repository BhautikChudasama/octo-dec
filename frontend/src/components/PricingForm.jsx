import React, { useState } from "react";
import { calculatePricing } from "../api/pricing";

export default function PricingForm({ onResult }) {
  const [tier, setTier] = useState("Free");
  const [features, setFeatures] = useState({
    projects: 0,
    environments: 0,
    build_minutes: 0,
    vcpu_cu: 0,
    vmemory_GB: 0,
  });

  const handleChange = (e) => {
    setFeatures({
      ...features,
      [e.target.name]: Number(e.target.value),
    });
  };

  const handleSubmit = async () => {
    const payload = {
      tier,
      features,
    };

    try {
      const result = await calculatePricing(payload);
      onResult(result);
    } catch (err) {
      alert("Pricing calculation failed");
    }
  };

  return (
    <div className="card">
      <h2>Configure Usage</h2>

      <select value={tier} onChange={(e) => setTier(e.target.value)}>
        <option>Free</option>
        <option>Pro</option>
        <option>Team</option>
        <option>Scale</option>
      </select>

      {Object.keys(features).map((key) => (
        <input
          key={key}
          name={key}
          placeholder={key}
          type="number"
          onChange={handleChange}
        />
      ))}

      <button onClick={handleSubmit}>Calculate</button>
    </div>
  );
}
