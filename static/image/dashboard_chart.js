document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("ipoPieChart");

  if (ctx) {
    const data = {
      labels: ["Upcoming", "Ongoing", "Listed"],
      datasets: [{
        label: "IPO Status",
        data: [
          {{ upcoming_count }},
          {{ ongoing_count }},
          {{ listed_count }}
        ],
        backgroundColor: ['#ffc107', '#0d6efd', '#198754'],
        hoverOffset: 4
      }]
    };

    const config = {
      type: "pie",
      data: data,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "bottom",
            labels: {
              color: "#ffffff",
              font: {
                size: 14
              }
            }
          }
        }
      }
    };

    // ✅ Initialize chart only once
    new Chart(ctx, config);
  }
});
