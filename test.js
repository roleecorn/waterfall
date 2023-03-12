function chart(container, path = '/chart') {
    fetch(path)
        .then(response => response.json())
        .then(c_data => {
            c_data = c_data.data;
            var canvas = document.createElement("canvas");
            canvas.className = "item";
            container.appendChild(canvas);
            var example = new Chart(canvas.getContext("2d"), {
                type: "bar",
                data: {
                    labels: c_data.labels,
                    datasets: [
                        {
                            label: c_data.datasetLabel,
                            data: c_data.data,
                            backgroundColor: c_data.backgroundColor,
                            borderWidth: c_data.borderWidth
                        }
                    ]
                }
            });
        })
        .catch(error => {
            console.error("Error fetching chart data:", error);
        });
}
function search(container) {
    fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "searchCompanys": searchCompanys,
            "inputs": inputs
        })
    })
        .then(response => response.json())
        .then(c_data => {
            c_data = c_data.data;
            var canvas = document.createElement("canvas");
            canvas.className = "item";
            container.appendChild(canvas);
            var example = new Chart(canvas.getContext("2d"), {
                type: "bar",
                data: {
                    labels: c_data.labels,
                    datasets: [
                        {
                            label: c_data.datasetLabel,
                            data: c_data.data,
                            backgroundColor: c_data.backgroundColor,
                            borderWidth: c_data.borderWidth
                        }
                    ]
                }
            });
        })
        .catch(error => {
            console.error("Error fetching chart data:", error);
        });
}