export default function PricingResult({ data }) {
    return (
      <div className="card">
        <h2>📊 Pricing Breakdown</h2>
  
        <p><b>Tier:</b> {data.tier}</p>
        <p><b>Tier Credits:</b> {data.tier_total_credits}</p>
        <p><b>Total Used:</b> {data.total_actual_credits_required}</p>
        <p><b>Remaining:</b> {data.remaining_tier_credits}</p>
        <p><b>Extra Needed:</b> {data.additional_credits_required}</p>
  
        <h3>Feature Split</h3>
  
        {Object.entries(data.breakdown).map(([feature, value]) => (
          <div key={feature} className="feature-box">
            <h4>{feature}</h4>
            <p>Usage: {value.usage}</p>
            <p>Limit: {value.tier_limit}</p>
            <p>Included: {value.included_credits}</p>
            <p>Spillover Credits: {value.spillover_credits}</p>
          </div>
        ))}
      </div>
    );
  }
  