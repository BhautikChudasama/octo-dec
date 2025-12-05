export async function calculatePricing(payload) {
    const response = await fetch("http://localhost:8000/pricing/calculate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
  
    if (!response.ok) {
      const err = await response.text();
      throw new Error(err);
    }
  
    return response.json();
  }
  