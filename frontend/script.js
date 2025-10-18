// Base API URL
const API_BASE_URL = "/api";

// Elements
const apiDot = document.getElementById("apiDot");
const healthDot = document.getElementById("healthDot");
const complaintsInput = document.getElementById("complaintsInput");
const predictBtn = document.getElementById("predictBtn");
const predictionsEl = document.getElementById("predictions");
const errorMsg = document.getElementById("errorMsg");
const useCacheCheckbox = document.getElementById("useCache");

let apiStatus = { running: false, healthy: false };

// Update API/Health Dots
function updateStatusDots() {
    apiDot.style.backgroundColor = apiStatus.running ? "#34D399" : "#EF4444"; // green or red
    healthDot.style.backgroundColor = apiStatus.healthy ? "#34D399" : "#EF4444"; // green or red
}

// Check API Status
async function checkApiStatus() {
    try {
        const statusRes = await fetch(`${API_BASE_URL}/`);
        const statusData = await statusRes.json();

        const healthRes = await fetch(`${API_BASE_URL}/health`);
        const healthData = await healthRes.json();

        apiStatus.running = statusData.status === "success";
        apiStatus.healthy = healthData.data?.status === "OK";
    } catch (err) {
        apiStatus.running = false;
        apiStatus.healthy = false;
    }

    updateStatusDots();
    predictBtn.disabled = !apiStatus.running || !apiStatus.healthy;
}

// Predict Complaints
predictBtn.addEventListener("click", async () => {
    const rawTexts = complaintsInput.value.trim();
    if (!rawTexts) return;

    predictionsEl.innerHTML = "";
    errorMsg.textContent = "";
    predictBtn.textContent = "Predicting...";
    predictBtn.disabled = true;

    const texts = rawTexts.split("\n").filter(line => line.trim() !== "");
    const useCache = useCacheCheckbox.checked;

    try {
        const res = await fetch(`${API_BASE_URL}/predict?use_cache=${useCache}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ texts }),
        });

        const data = await res.json();

        if (data.status === "success") {
            const results = data.data.predictions;

            predictionsEl.innerHTML = results
                .map((p, idx) => {
                    return `
                    <div class="p-4 rounded-lg border border-gray-700 bg-gray-800 shadow">
                        <p class="font-medium"><strong>Complaint:</strong> ${texts[idx]}</p>
                        <p><strong>Severity:</strong> ${p.severity}</p>
                        <p><strong>Confidence:</strong> ${p.confidence.toFixed(2)}%</p>
                        <p><strong>Prediction Time:</strong> ${p.prediction_time_ms.toFixed(2)} ms</p>
                    </div>
                    `;
                })
                .join("");
        } else {
            errorMsg.textContent = data.errors.join(", ") || "Unknown error";
        }
    } catch (err) {
        errorMsg.textContent = "Failed to fetch predictions. Make sure the API is running.";
    }

    predictBtn.textContent = "Predict Severity";
    predictBtn.disabled = !apiStatus.running || !apiStatus.healthy;
});

// Initial API check
checkApiStatus();
setInterval(checkApiStatus, 30000); // Re-check every 30s
