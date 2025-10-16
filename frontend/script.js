const API_BASE_URL = "http://127.0.0.1:8000";

const checkRootBtn = document.getElementById("checkRoot");
const checkHealthBtn = document.getElementById("checkHealth");
const systemResponseDiv = document.getElementById("systemResponse");

checkRootBtn.addEventListener("click", async () => {
  systemResponseDiv.textContent = "Loading...";
  try {
    const res = await fetch(`${API_BASE_URL}/`);
    const data = await res.json();
    systemResponseDiv.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    systemResponseDiv.textContent = "Error connecting to API";
  }
});

checkHealthBtn.addEventListener("click", async () => {
  systemResponseDiv.textContent = "Loading...";
  try {
    const res = await fetch(`${API_BASE_URL}/health`);
    const data = await res.json();
    systemResponseDiv.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    systemResponseDiv.textContent = "Error connecting to API";
  }
});

const predictBtn = document.getElementById("predictBtn");
const predictInput = document.getElementById("predictInput");
const predictResponseDiv = document.getElementById("predictResponse");
const useCacheCheckbox = document.getElementById("useCache");

predictBtn.addEventListener("click", async () => {
  const texts = predictInput.value
    .split("\n")
    .map(t => t.trim())
    .filter(t => t.length > 0);

  if (texts.length === 0) {
    predictResponseDiv.textContent = "Please enter at least one complaint.";
    return;
  }

  predictResponseDiv.textContent = "Predicting...";
  try {
    const res = await fetch(`${API_BASE_URL}/predict?use_cache=${useCacheCheckbox.checked}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ texts }),
    });
    const data = await res.json();
    predictResponseDiv.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    predictResponseDiv.textContent = "Error connecting to API";
  }
});
