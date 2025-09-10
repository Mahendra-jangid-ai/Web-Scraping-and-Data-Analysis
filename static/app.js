const form = document.getElementById("stockForm");
const chartSection = document.getElementById("chartSection");
const summarySection = document.getElementById("summarySection");
const summaryTable = document.getElementById("summaryTable");
const errorDiv = document.getElementById("error");

let chart;

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  errorDiv.hidden = true;

  const ticker = document.getElementById("ticker").value.trim() || "TCS.NS";

  try {
    const res = await fetch(`/api/stock?ticker=${ticker}&period=1mo&interval=1d`);
    const data = await res.json();
    if (!res.ok || data.error) throw new Error(data.error || "Failed to fetch stock data");

    const labels = data.map(row => row.Date.split("T")[0]);
    const closes = data.map(row => row.Close);

    if (chart) chart.destroy();
    const ctx = document.getElementById("stockChart").getContext("2d");
    chart = new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [{
          label: `${ticker} Closing Price (INR)`,
          data: closes,
          borderColor: "blue",
          fill: false
        }]
      },
      options: { responsive: true }
    });
    chartSection.hidden = false;

    const summaryRes = await fetch(`/api/stock/summary?ticker=${ticker}&period=1mo&interval=1d`);
    const summary = await summaryRes.json();
    if (!summaryRes.ok || summary.error) throw new Error(summary.error || "Failed to fetch summary");

    summaryTable.innerHTML = "";
    Object.entries(summary).forEach(([k, v]) => {
      const row = document.createElement("tr");
      row.innerHTML = `<td>${k}</td><td>${v}</td>`;
      summaryTable.appendChild(row);
    });
    summarySection.hidden = false;

  } catch (err) {
    errorDiv.textContent = err.message;
    errorDiv.hidden = false;
  }
});
